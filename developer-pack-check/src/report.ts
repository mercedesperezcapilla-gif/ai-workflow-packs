import { readFileSync } from 'node:fs';
export type Difference = { record_id: string; kind: string; fields: string[]; process_a: Record<string, unknown> | null; process_b: Record<string, unknown> | null };
export type Report = { date: string; record_differences: Difference[]; [key: string]: unknown };
function requireValue(ok: unknown, message: string): asserts ok { if (!ok) throw new Error(message); }
function object(v: unknown): v is Record<string, unknown> { return !!v && typeof v === 'object' && !Array.isArray(v); }
const fields = ['record_id','account','instrument_code','category','quantity','amount_gbp','status'];
const allowedCategories = ['Matched','Unmatched','Missing','Position difference'];
const moneyPattern = /^-?\d+\.\d{2}$/;
const pence = (value: string) => BigInt(value.replace('.', ''));
export function validateReport(value: unknown): Report {
  requireValue(object(value), 'Report must be an object');
  requireValue(typeof value.date === 'string' && /^\d{4}-\d{2}-\d{2}$/.test(value.date) && !Number.isNaN(Date.parse(value.date)) && new Date(value.date).toISOString().slice(0,10) === value.date, 'Invalid comparison date');
  for (const key of ['source_folder','rules','definition_note']) requireValue(typeof value[key] === 'string' && value[key].length > 0, 'Missing or invalid ' + key);
  for (const key of ['required_inputs','missing_inputs','unresolved_questions']) requireValue(Array.isArray(value[key]) && value[key].every((v: unknown) => typeof v === 'string'), 'Missing or invalid ' + key);
  requireValue((value.required_inputs as string[]).length === 4 && new Set(value.required_inputs as string[]).size === 4, 'Expected four unique required_inputs');
  requireValue((value.missing_inputs as string[]).length === 0, 'Missing source inputs');
  requireValue(Array.isArray(value.categories) && value.categories.length === 4, 'Expected four categories');
  const categories = new Set<string>();
  for (const row of value.categories) {
    requireValue(object(row) && typeof row.category === 'string' && ['Matched','Unmatched','Missing','Position difference'].includes(row.category) && !categories.has(row.category), 'Invalid or duplicate category');
    categories.add(row.category);
    for (const key of ['process_a','process_b','difference_b_minus_a']) {
      const totals = row[key];
      requireValue(object(totals) && Number.isSafeInteger(totals.count) && typeof totals.amount_gbp === 'string' && /^-?\d+\.\d{2}$/.test(totals.amount_gbp), 'Invalid category totals');
    }
    const a = row.process_a as {count: number; amount_gbp: string};
    const b = row.process_b as {count: number; amount_gbp: string};
    const delta = row.difference_b_minus_a as {count: number; amount_gbp: string};
    requireValue(a.count >= 0 && b.count >= 0, 'Negative source count');
    requireValue(BigInt(delta.count) === BigInt(b.count) - BigInt(a.count) && pence(delta.amount_gbp) === pence(b.amount_gbp) - pence(a.amount_gbp), 'Inconsistent category delta');
    requireValue(Array.isArray(row.record_ids) && row.record_ids.every((id: unknown) => typeof id === 'string'), 'Invalid category references');
  }
  requireValue(Array.isArray(value.record_differences), 'Missing record_differences');
  const ids = new Set<string>();
  for (const row of value.record_differences) {
    requireValue(object(row) && typeof row.record_id === 'string' && row.record_id.length > 0, 'Invalid record_id');
    requireValue(!ids.has(row.record_id), 'Duplicate record_id: ' + row.record_id); ids.add(row.record_id);
    requireValue(['record difference','category-definition difference'].includes(String(row.kind)), 'Invalid difference kind');
    requireValue(Array.isArray(row.fields) && row.fields.length > 0 && row.fields.every((f: unknown) => typeof f === 'string' && fields.includes(f)) && new Set(row.fields).size === row.fields.length, 'Invalid differing fields');
    for (const side of ['process_a','process_b']) {
      const record = row[side];
      if (record === null) continue;
      requireValue(object(record) && Object.keys(record).length === fields.length && fields.every(key => Object.hasOwn(record, key)), 'Incomplete or invalid ' + side);
      requireValue(record.record_id === row.record_id, 'Invalid ' + side + ' record_id');
      requireValue(typeof record.account === 'string' && record.account.length > 0 && typeof record.instrument_code === 'string' && /^FIC-\d{4}$/.test(record.instrument_code), 'Invalid side account or instrument');
      requireValue(Number.isSafeInteger(record.quantity), 'Invalid side quantity');
      requireValue(typeof record.amount_gbp === 'string' && moneyPattern.test(record.amount_gbp), 'Invalid side amount_gbp');
      requireValue(typeof record.category === 'string' && allowedCategories.includes(record.category), 'Invalid side category');
      requireValue(typeof record.status === 'string' && ['Open','Closed'].includes(record.status) && (record.category === 'Matched') === (record.status === 'Closed'), 'Invalid side status');
    }
    requireValue(row.process_a !== null || row.process_b !== null, 'Both process sides absent');
  }
  for (const row of value.categories) requireValue(row.record_ids.every((id: string) => ids.has(id)), 'Unknown category record reference');
  return value as Report;
}
export function loadReport(file: string): Report {
  try { return validateReport(JSON.parse(readFileSync(file, 'utf8'))); }
  catch (error) { throw new Error(file + ': ' + (error as Error).message); }
}
