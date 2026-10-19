// Fictional review exercise: intentionally wrong identity when amounts change.
import { validateReport } from '../../src/report.ts';
import type { Report } from '../../src/report.ts';
export type Lifecycle = { new: string[]; continuing: string[]; resolved: string[] };
export function classify(yesterday: Report, today: Report): Lifecycle {
  validateReport(yesterday); validateReport(today);
  if (Date.parse(today.date) - Date.parse(yesterday.date) !== 86400000) throw new Error('Baseline must be the immediately previous calendar day');
  const before = new Map(yesterday.record_differences.map(row => [row.record_id, row]));
  const now = new Map(today.record_differences.map(row => [row.record_id, row]));
  const same = (id: string) => before.has(id) && JSON.stringify(before.get(id)) === JSON.stringify(now.get(id));
  return {
    new: [...now.keys()].filter(id => !same(id)).sort(),
    continuing: [...now.keys()].filter(same).sort(),
    resolved: [...before.keys()].filter(id => !now.has(id)).sort()
  };
}
