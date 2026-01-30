// main entry point — agent runtime
import { log } from './log.mjs';

const TOOL_LOOP_MAX_N = parseInt(process.env.TOOL_LOOP_MAX_N || '8', 10);

export async function runAgent(task, tools = {}, opts = {}) {
  const maxIter = opts.maxIterations || TOOL_LOOP_MAX_N;
  let iteration = 0;

  while (iteration < maxIter) {
    iteration++;
    log.info({ iteration, maxIter }, 'agent loop tick');
    // placeholder: wire up LLM client + tool execution here
    break;
  }

  if (iteration >= maxIter) {
    log.warn({ maxIter }, 'agent hit max iteration guard');
  }

  return { iterations: iteration, status: 'complete' };
}

export function main() {
  runAgent('hello world').then(r => console.log(r));
}
