import copy
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import compare

class ComparisonTests(unittest.TestCase):
    def test_clean_success(self):
        r = compare.compare(compare.ROOT / 'data/2026-10-14')
        self.assertEqual([d['record_id'] for d in r['record_differences']], ['R003'])
        self.assertEqual(r['record_differences'][0]['kind'], 'category-definition difference')

    def test_expected_differences(self):
        r = compare.compare(compare.ROOT / 'data/2026-10-15')
        expected = [('Matched',1,'500000.00'),('Unmatched',1,'500000.00'),('Missing',-1,'-300000.00'),('Position difference',-1,'-3250.00')]
        self.assertEqual([(c['category'],c['difference_b_minus_a']['count'],str(c['difference_b_minus_a']['amount_gbp'])) for c in r['categories']],expected)
        self.assertEqual([d['record_id'] for d in r['record_differences']],['R003','R004','R005','R006','R007'])
        self.assertEqual(r['categories'][1]['record_ids'],['R003','R005','R007'])

    def test_population_and_tables(self):
        import json
        for folder in (compare.ROOT/'data').iterdir():
            for detail in folder.glob('*/detail.csv'):
                records = compare.rows(detail, compare.DETAIL)
                self.assertTrue(20 <= len(records) <= 30)
                for row in records:
                    amount = abs(compare.money(row['amount_gbp']))
                    if row['category'] == 'Position difference':
                        self.assertTrue(100 <= amount <= 50000)
                    else:
                        self.assertTrue(10000 <= amount <= 5000000)
        result = compare.compare(compare.ROOT/'data/2026-10-15')
        report = compare.markdown(result)
        self.assertEqual(report.count('| record_id | Account | Instrument |'), 2)
        self.assertNotIn('process_a:', report)
        self.assertIn('| R004 | SIM-004 | FIC-0004 | amount_gbp | 2,400.00 | 2,750.00 |', report)
        self.assertIn('| R006 | SIM-006 | FIC-0006 | amount_gbp | 3,600.00 | Absent |', report)
        self.assertIn('| R007 | SIM-007 | FIC-0007 | amount_gbp | Absent | 700,000.00 |', report)
        self.assertEqual(len(json.loads(compare.serialise(result))['record_differences']), 5)
        changed = copy.deepcopy(result)
        changed['record_differences'][0]['process_a']['category'] = '<test|value>'
        self.assertIn('&lt;test&#124;value&gt;', compare.markdown(changed))

    def assert_stop(self, path, message):
        result = subprocess.run([sys.executable, str(compare.ROOT/'compare.py'), str(compare.ROOT/path)],capture_output=True,text=True)
        self.assertEqual(result.returncode,1)
        self.assertIn(message,result.stderr)
        self.assertIn('No report written',result.stderr)

    def test_missing_file_stop(self):
        self.assert_stop('data/2026-10-16','Missing required file(s): process-b/summary.csv')

    def test_summary_mismatch_stop(self):
        self.assert_stop('extra/summary-mismatch/2026-10-15','Summary-detail mismatch: process-a')

    def test_duplicates_stop(self):
        self.assert_stop('extra/duplicates/2026-10-15','Duplicate record_id: process-b/R002')

    def test_label_normalisation(self):
        a=compare.compare(compare.ROOT/'data/2026-10-14')
        b=compare.compare(compare.ROOT/'extra/inconsistent-labels/2026-10-15')
        self.assertEqual(a['categories'],b['categories'])
        self.assertEqual(a['record_differences'],b['record_differences'])
        with self.assertRaises(compare.InvalidInput): compare.label('unmatched')

    def test_precision_and_tolerance(self):
        self.assertNotEqual(compare.money('1.00'),compare.money('1.01'))
        for invalid in ['NaN','1.001','1','Infinity']:
            with self.assertRaises(compare.InvalidInput): compare.money(invalid)

    def test_duplicate_position_key(self):
        import shutil
        with tempfile.TemporaryDirectory(dir=compare.ROOT) as temporary:
            folder=Path(temporary)/'2026-10-14'
            shutil.copytree(compare.ROOT/'data/2026-10-14',folder)
            p=folder/'process-a/detail.csv'
            p.write_text(p.read_text().replace('SIM-002,FIC-0002','SIM-001,FIC-0001'))
            with self.assertRaisesRegex(compare.InvalidInput,'Duplicate position key'): compare.compare(folder)


class IntegrityTests(unittest.TestCase):
    def test_calendar_dates_and_preservation(self):
        import contextlib
        import io
        import shutil
        from unittest.mock import patch
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            reports = root / 'reports'
            reports.mkdir()
            for name in ['2026-02-30', '2026-13-01', '2026-02-29', '2026-00-10']:
                stem = reports / ('comparison-' + name)
                for suffix in ['.md', '.json']:
                    stem.with_suffix(suffix).write_text('previous ' + suffix)
                error = io.StringIO()
                with patch.object(compare, 'ROOT', root), contextlib.redirect_stderr(error):
                    self.assertEqual(compare.main([str(root / name)]), 1)
                self.assertIn('STOP: Invalid ISO calendar date', error.getvalue())
                for suffix in ['.md', '.json']:
                    self.assertEqual(stem.with_suffix(suffix).read_text(), 'previous ' + suffix)
            for name in ['2028-02-29', '2027-01-01']:
                folder = root / name
                shutil.copytree(compare.ROOT / 'data/2026-10-14', folder)
                with patch.object(compare, 'ROOT', root):
                    self.assertEqual(compare.compare(folder)['date'], name)

    def test_second_write_failure_preserves_pair(self):
        import contextlib
        import io
        from unittest.mock import patch
        result = compare.compare(compare.ROOT / 'data/2026-10-15')
        original = Path.write_text
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / 'reports').mkdir()
            stem = root / 'reports/comparison-2026-10-15'
            for suffix in ['.md', '.json']:
                stem.with_suffix(suffix).write_text('previous ' + suffix)
            def fail_second(path, *args, **kwargs):
                if path.name == '1':
                    raise OSError('forced second write failure')
                return original(path, *args, **kwargs)
            error = io.StringIO()
            with patch.object(compare, 'ROOT', root), patch.object(compare, 'compare', return_value=result), patch.object(Path, 'write_text', fail_second), contextlib.redirect_stderr(error):
                self.assertEqual(compare.main(['unused']), 1)
            self.assertIn('STOP:', error.getvalue())
            self.assertIn('No report changed', error.getvalue())
            for suffix in ['.md', '.json']:
                self.assertEqual(stem.with_suffix(suffix).read_text(), 'previous ' + suffix)

    def test_second_replacement_failure_rolls_back(self):
        from unittest.mock import patch
        original = Path.replace
        with tempfile.TemporaryDirectory() as temporary:
            stem = Path(temporary) / 'comparison-2026-10-15'
            for suffix in ['.md', '.json']:
                stem.with_suffix(suffix).write_text('previous ' + suffix)
            def fail_second(path, target):
                if path.name == '1':
                    raise OSError('forced second replacement failure')
                return original(path, target)
            with patch.object(Path, 'replace', fail_second):
                with self.assertRaisesRegex(compare.ReportWriteError, 'No report changed'):
                    compare.write_reports(stem, ('new markdown', 'new json'))
            for suffix in ['.md', '.json']:
                self.assertEqual(stem.with_suffix(suffix).read_text(), 'previous ' + suffix)

if __name__ == '__main__': unittest.main()
