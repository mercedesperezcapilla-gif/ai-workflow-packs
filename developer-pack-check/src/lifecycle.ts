import { validateReport } from './report.ts';
import type { Report } from './report.ts';
export type Lifecycle = { new: string[]; continuing: string[]; resolved: string[] };
export function classify(yesterday: Report, today: Report): Lifecycle {
  validateReport(yesterday); validateReport(today);
  if (Date.parse(today.date) - Date.parse(yesterday.date) !== 86400000) throw new Error('Baseline must be the immediately previous calendar day: ' + yesterday.date + ' -> ' + today.date);
  const before = new Set(yesterday.record_differences.map(row => row.record_id));
  const now = new Set(today.record_differences.map(row => row.record_id));
  return {
    new: [...now].filter(id => !before.has(id)).sort(),
    continuing: [...now].filter(id => before.has(id)).sort(),
    resolved: [...before].filter(id => !now.has(id)).sort()
  };
}

// Compare values structurally: object property order is not a value change.
export function changedContinuing(yesterday: Report, today: Report): string[] {
  const continuing = classify(yesterday, today).continuing;
  const before = new Map(yesterday.record_differences.map(row => [row.record_id, row]));
  const now = new Map(today.record_differences.map(row => [row.record_id, row]));
  const canonical = (value: unknown): string => {
    if (Array.isArray(value)) return '[' + value.map(canonical).join(',') + ']';
    if (value !== null && typeof value === 'object') return '{' + Object.entries(value).sort(([a], [b]) => a.localeCompare(b)).map(([key, val]) => JSON.stringify(key) + ':' + canonical(val)).join(',') + '}';
    return JSON.stringify(value);
  };
  return continuing.filter(id => {
    const a = before.get(id)!; const b = now.get(id)!;
    return canonical(a.process_a) !== canonical(b.process_a) || canonical(a.process_b) !== canonical(b.process_b);
  });
}
