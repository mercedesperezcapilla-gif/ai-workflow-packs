import test from 'node:test';
import assert from 'node:assert/strict';
import { spawnSync } from 'node:child_process';
import { loadReport, validateReport } from '../src/report.ts';
const { classify } = await import(process.env.LIFECYCLE_PLANTED === '1' ? '../extra/planted/lifecycle-planted.ts' : '../src/lifecycle.ts');
const read = (name: string) => loadReport('fixtures/' + name + '.json');
const yesterday = read('comparison-2026-10-14');
const today = read('comparison-2026-10-15');
const expected = { new: ['R004','R005','R006','R007'], continuing: ['R003'], resolved: [] };
function ready() { assert.deepEqual(classify(yesterday,today),expected); }
const cli = (...args: string[]) => spawnSync(process.execPath, [...process.execArgv,'src/cli.ts',...args], {encoding:'utf8'});
test('EVAL-01: exact exclusive and complete lifecycle sets', () => {
  ready(); const result=classify(yesterday,today); const ids=Object.values(result).flat();
  assert.equal(ids.length,5); assert.equal(new Set(ids).size,5);
});
test('EVAL-03: R003 continuing, zero false-new records', () => { ready(); assert.ok(!classify(yesterday,today).new.includes('R003')); });
test('EVAL-04: changed amounts do not change identity', () => { ready(); assert.deepEqual(classify(yesterday,read('eval-04-changed-r003-amount')),expected); });
test('EVAL-08: no new differences still retains all sections', () => {
  assert.deepEqual(classify(yesterday,read('eval-08-today-same-as-yesterday')), {new:[],continuing:['R003'],resolved:[]});
  // The alternative exports classify only; its no-New lists were checked above.
  // Normal implementation tests also verify the production CLI rendering.
  if (process.env.LIFECYCLE_PLANTED === '1') return;
  const run=cli('fixtures/comparison-2026-10-14.json','fixtures/eval-08-today-same-as-yesterday.json');
  assert.equal(run.status,0); assert.match(run.stdout,/No new differences/); assert.match(run.stdout,/Continuing: R003/);assert.match(run.stdout,/Resolved: None/);
});
test('EVAL-10: no older baseline fallback, including first run', () => {
  ready(); assert.throws(()=>read('eval-10-missing-baseline'),/eval-10-missing-baseline/);
  assert.throws(()=>classify(read('eval-16-earlier-sighting'),today),/previous calendar day/);
});
test('EVAL-11: reject duplicated JSON identity, not legitimate multiple fields', () => {
  ready(); assert.equal(today.record_differences.find(r=>r.record_id==='R004')!.fields.length,2);
  assert.throws(()=>read('eval-11-duplicate-r004'),/Duplicate record_id: R004/);
});
test('EVAL-16: earlier sighting cannot prevent New after an absent day', () => {
  ready(); const prior=classify(read('eval-16-earlier-sighting'),yesterday);
  assert.deepEqual(prior.resolved,['R004','R005','R006','R007']); assert.deepEqual(classify(yesterday,today),expected);
});
test('CLI stops on missing baseline without success output', () => {
  const run=cli('fixtures/eval-10-missing-baseline.json','fixtures/comparison-2026-10-15.json');
  assert.equal(run.status,1); assert.match(run.stderr,/STOP:.*eval-10-missing-baseline.json/);assert.equal(run.stdout,'');
});
test('report validation rejects bad dates and missing fields', () => {
  assert.throws(()=>validateReport({...today,date:'2026-02-30'}),/date/);
  assert.throws(()=>validateReport({...today,record_differences:undefined}),/record_differences/);
});
test('CLI stops on invalid current file and names it', () => {
  const run=cli('fixtures/comparison-2026-10-14.json','fixtures/eval-11-duplicate-r004.json');
  assert.equal(run.status,1);assert.match(run.stderr,/eval-11-duplicate-r004.json.*Duplicate record_id/);assert.equal(run.stdout,'');
});
