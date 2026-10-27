import { loadReport } from './report.ts';
import { classify, changedContinuing } from './lifecycle.ts';
try {
  const [baseline, current] = process.argv.slice(2);
  if (!baseline || !current || process.argv.length !== 4) throw new Error('Usage: node src/cli.ts <yesterday.json> <today.json>; both files required');
  const yesterday = loadReport(baseline); const today = loadReport(current);
  const result = classify(yesterday, today);
  const changed = changedContinuing(yesterday, today);
  if (!result.new.length) console.log('No new differences');
  console.log('New: ' + (result.new.join(', ') || 'None'));
  console.log('Continuing: ' + (result.continuing.join(', ') || 'None'));
  console.log('Resolved: ' + (result.resolved.join(', ') || 'None'));
  console.log('Changed since yesterday: ' + (changed.join(', ') || 'None'));
} catch (error) {
  console.error('STOP: ' + (error as Error).message + '. No classification produced. Riley must decide any missing baseline.');
  process.exitCode = 1;
}
