import type { Report } from './report.ts';
export type Lifecycle = { new: string[]; continuing: string[]; resolved: string[] };
// Implement REQ-1 against docs/acceptance.md, including the previous calendar day rule.
export function classify(yesterday: Report, today: Report): Lifecycle {
  throw new Error("Not implemented: REQ-1");
}

// Implement approved REQ-2 after REQ-1.
export function changedContinuing(yesterday: Report, today: Report): string[] {
  throw new Error("Not implemented: REQ-2");
}
