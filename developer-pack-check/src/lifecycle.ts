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
