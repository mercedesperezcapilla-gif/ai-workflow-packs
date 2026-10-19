"""Fictional two-process comparison. Python 3.10+, standard library only."""
import csv
import json
import re
import sys
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CATEGORIES = ('Matched', 'Unmatched', 'Missing', 'Position difference')
ALIASES = {c: c for c in CATEGORIES} | {'UNMATCHED': 'Unmatched', 'Position Difference': 'Position difference'}
DETAIL = ['record_id', 'account', 'instrument_code', 'category', 'quantity', 'amount_gbp', 'status']
SUMMARY = ['category', 'record_count', 'amount_gbp']


class InvalidInput(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise InvalidInput(message)


def money(value):
    require(bool(re.fullmatch(r'-?\d+\.\d{2}', value)), 'amount_gbp must be a finite GBP amount with 2 decimal places')
    return Decimal(value)


def label(value):
    require(value in ALIASES, 'Unknown category label: ' + value)
    return ALIASES[value]


def rows(path, schema):
    with path.open(encoding='utf-8', newline='') as stream:
        reader = csv.DictReader(stream)
        require(reader.fieldnames == schema, f'Schema mismatch: {path}')
        result = list(reader)
    require(all(set(row) == set(schema) and all(v is not None and v != '' for v in row.values()) for row in result), f'Incomplete row: {path}')
    return result


def load(folder, process):
    detail = rows(folder / process / 'detail.csv', DETAIL)
    require(0 < len(detail) < 40, f'Expected 1 to 39 detail rows: {process}')
    indexed, keys = {}, set()
    totals = {c: {'count': 0, 'amount_gbp': Decimal('0.00')} for c in CATEGORIES}
    for row in detail:
        rid = row['record_id']
        require(rid not in indexed, f'Duplicate record_id: {process}/{rid}')
        key = (row['account'], row['instrument_code'])
        require(key not in keys, f'Duplicate position key: {process}/{rid}')
        require(bool(re.fullmatch(r'FIC-\d{4}', row['instrument_code'])), f'Invalid instrument: {rid}')
        require(bool(re.fullmatch(r'-?\d+', row['quantity'])), f'Invalid quantity: {rid}')
        require(row['status'] == 'Open' or row['status'] == 'Closed', f'Invalid status: {rid}')
        row = dict(row, category=label(row['category']), quantity=int(row['quantity']), amount_gbp=money(row['amount_gbp']))
        require((row['category'] == 'Matched') == (row['status'] == 'Closed'), f'Category/status conflict: {rid}')
        indexed[rid] = row
        keys.add(key)
        totals[row['category']]['count'] += 1
        totals[row['category']]['amount_gbp'] += row['amount_gbp']
    summary = {}
    for row in rows(folder / process / 'summary.csv', SUMMARY):
        cat = label(row['category'])
        require(cat not in summary, f'Duplicate summary category: {process}/{cat}')
        require(bool(re.fullmatch(r'\d+', row['record_count'])), 'Invalid record_count')
        summary[cat] = {'count': int(row['record_count']), 'amount_gbp': money(row['amount_gbp'])}
    require(set(summary) == set(CATEGORIES), f'Incomplete summary categories: {process}')
    require(summary == totals, f'Summary-detail mismatch: {process}')
    return indexed, totals


def compare(folder):
    folder = Path(folder).resolve()
    require(bool(re.fullmatch(r'2026-\d{2}-\d{2}', folder.name)), 'Select a dated folder, for example data/2026-10-15')
    required = [folder / p / f for p in ('process-a', 'process-b') for f in ('summary.csv', 'detail.csv')]
    missing = [p.relative_to(folder).as_posix() for p in required if not p.is_file()]
    require(not missing, 'Missing required file(s): ' + ', '.join(missing))
    a, ta = load(folder, 'process-a')
    b, tb = load(folder, 'process-b')
    differences = []
    for rid in sorted(a.keys() | b.keys()):
        left, right = a.get(rid), b.get(rid)
        if left == right:
            continue
        fields = [f for f in DETAIL if left is None or right is None or left[f] != right[f]]
        definition = (left is not None and right is not None and
                      left['category'] == 'Missing' and right['category'] == 'Unmatched' and
                      all(left[f] == right[f] for f in DETAIL if f != 'category'))
        differences.append({'record_id': rid, 'kind': 'category-definition difference' if definition else 'record difference',
                            'fields': fields, 'process_a': left, 'process_b': right})
    categories = []
    for cat in CATEGORIES:
        refs = [d['record_id'] for d in differences if any(d[p] and d[p]['category'] == cat for p in ('process_a', 'process_b'))]
        categories.append({'category': cat, 'process_a': ta[cat], 'process_b': tb[cat],
                           'difference_b_minus_a': {'count': tb[cat]['count'] - ta[cat]['count'], 'amount_gbp': tb[cat]['amount_gbp'] - ta[cat]['amount_gbp']},
                           'record_ids': refs})
    return {'date': folder.name, 'source_folder': folder.relative_to(ROOT).as_posix(), 'rules': 'rules.md v1; definitions.md v1; B minus A; GBP; tolerance 0.00',
            'required_inputs': [p.relative_to(ROOT).as_posix() for p in required], 'missing_inputs': [],
            'categories': categories, 'record_differences': differences,
            'unresolved_questions': ['Are record differences caused by timing, mapping or source completeness? Confirm with the fictional process owner.'],
            'definition_note': 'Process B includes absent counterpart positions in Unmatched. Process A calls these Missing. This is not label normalisation.'}


def serialise(result):
    return json.dumps(result, indent=2, default=lambda v: format(v, '.2f'), ensure_ascii=False) + '\n'


def markdown(result):
    lines = [f"# Comparison {result['date']}", '', result['rules'], '', result['definition_note'], '',
             '| Category | A count | A GBP | B count | B GBP | B minus A count | B minus A GBP | Record references |',
             '|---|---:|---:|---:|---:|---:|---:|---|']
    for c in result['categories']:
        a, b, d = (c[k] for k in ('process_a', 'process_b', 'difference_b_minus_a'))
        lines.append(f"| {c['category']} | {a['count']} | {a['amount_gbp']:.2f} | {b['count']} | {b['amount_gbp']:.2f} | {d['count']} | {d['amount_gbp']:.2f} | {', '.join(c['record_ids']) or 'None'} |")
    lines += ['', '## Record differences', '']
    def cell(value):
        return str(value).replace('&', '&amp;').replace('|', '&#124;').replace('<', '&lt;').replace('>', '&gt;').replace('\n', ' ')

    def value(row, field):
        if row is None:
            return 'Absent'
        item = row[field]
        return format(item, ',.2f') if isinstance(item, Decimal) else str(item)

    for kind in ('category-definition difference', 'record difference'):
        lines += ['### ' + kind.capitalize(), '',
                  '| record_id | Account | Instrument | What differs | Process A value | Process B value |',
                  '|---|---|---|---|---|---|']
        selected = [d for d in result['record_differences'] if d['kind'] == kind]
        if not selected:
            lines.append('| None | | | | | |')
        for d in selected:
            left, right = d['process_a'], d['process_b']
            row = left or right
            fields = d['fields'] if left and right else [f for f in DETAIL if f != 'record_id']
            for field in fields:
                cells = [d['record_id'], row['account'], row['instrument_code'],
                         field, value(left, field), value(right, field)]
                lines.append('| ' + ' | '.join(cell(v) for v in cells) + ' |')
        lines.append('')
    lines += ['', '## Source references', ''] + ['- ' + p for p in result['required_inputs']]
    lines += ['', 'Missing inputs: none. All four files validated and both summaries cross-checked.', '', '## Unresolved questions', '']
    lines += result['unresolved_questions']
    return '\n'.join(lines) + '\n'


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    try:
        require(len(argv) == 1, 'Usage: python compare.py data/2026-10-15')
        result = compare(argv[0])
        output = ROOT / 'reports'
        output.mkdir(exist_ok=True)
        stem = output / ('comparison-' + result['date'])
        stem.with_suffix('.md').write_text(markdown(result), encoding='utf-8')
        stem.with_suffix('.json').write_text(serialise(result), encoding='utf-8')
        print(f"OK {result['date']}: 4 files validated; {len(result['record_differences'])} record differences; reports/{stem.name}.md and .json")
        return 0
    except (InvalidInput, OSError, csv.Error, UnicodeError) as error:
        print(f'STOP: {error}. No report written for this run.', file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
