#!/usr/bin/env node
import { main } from './index.mjs';
import { log } from './log.mjs';

const task = process.argv.slice(2).join(' ') || 'help';
log.info({ task }, 'cli invoked');
main();
