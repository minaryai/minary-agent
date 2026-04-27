// runtime config — loaded from env + defaults
export const config = {
  model: process.env.MINARY_MODEL || 'claude-4.7-sonnet',
  fallbackModel: process.env.MINARY_FALLBACK || 'claude-4.6-opus',
  maxIterations: parseInt(process.env.TOOL_LOOP_MAX_N || '8', 10),
  thinkingBudget: parseInt(process.env.THINKING_BUDGET || '10000', 10),
  enableCache: process.env.ENABLE_CACHE !== 'false',
  enableThinking: process.env.ENABLE_THINKING !== 'false',
  enableTraceDump: process.env.ENABLE_TRACE_DUMP === 'true',
  logLevel: process.env.LOG_LEVEL || 'warn',
  traceDir: process.env.TRACE_DIR || './traces',
  // multi-chain
  chains: {
    base: { rpc: process.env.BASE_RPC || 'https://mainnet.base.org' },
    solana: { rpc: process.env.SOLANA_RPC || 'https://api.mainnet-beta.solana.com' },
  },
};
