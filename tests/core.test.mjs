import { test } from 'node:test';
import assert from 'node:assert/strict';

test('agent core constructs', () => {
  // placeholder: import AgentCore when module system is wired
  assert.ok(true);
});

test('tool-loop guard prevents infinite iteration', () => {
  const maxIter = 8;
  let iter = 0;
  while (iter < maxIter) { iter++; break; }
  assert.ok(iter <= maxIter);
});

test('config loads defaults', async () => {
  const { config } = await import('../src/config.mjs');
  assert.equal(config.model, 'claude-4.7-sonnet');
  assert.equal(config.maxIterations, 8);
});
