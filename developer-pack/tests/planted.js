// Run the same cases against the alternative without replacing src/.
process.env.LIFECYCLE_PLANTED = '1';
await import('./lifecycle.test.ts');
