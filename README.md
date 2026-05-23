<div align="center">
  <a href="https://github.com/minaryai/minary-agent">
    <img src="https://raw.githubusercontent.com/minaryai/minary-agent/main/assets/banner.jpg" alt="minary" width="100%" />
  </a>
</div>

<div align="center">

[![License](https://img.shields.io/badge/license-MIT-blue.svg?style=for-the-badge)](LICENSE)
[![Node](https://img.shields.io/badge/node-%E2%89%A520-339933.svg?style=for-the-badge&logo=node.js&logoColor=white)](#install)
[![CI](https://img.shields.io/badge/ci-passing-4cd964.svg?style=for-the-badge&logo=githubactions&logoColor=white)](https://github.com/minaryai/minary-agent/actions)
[![Version](https://img.shields.io/badge/version-0.5.0--beta-cd5cff.svg?style=for-the-badge)](https://github.com/minaryai/minary-agent/releases)
[![Models](https://img.shields.io/badge/models-200+-ffb340.svg?style=for-the-badge&logo=openai&logoColor=white)](#model-routing)
[![Tools](https://img.shields.io/badge/tools-40+-88e1f2.svg?style=for-the-badge&logo=stackblitz&logoColor=white)](#built-in-tools)

<br/>

[![GitHub stars](https://img.shields.io/github/stars/minaryai/minary-agent?style=flat-square&color=ffb340&labelColor=0a0a0a)](https://github.com/minaryai/minary-agent/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/minaryai/minary-agent?style=flat-square&color=88e1f2&labelColor=0a0a0a)](https://github.com/minaryai/minary-agent/network)
[![Open Issues](https://img.shields.io/github/issues/minaryai/minary-agent?style=flat-square&color=cd5cff&labelColor=0a0a0a)](https://github.com/minaryai/minary-agent/issues)
[![Closed Issues](https://img.shields.io/github/issues-closed/minaryai/minary-agent?style=flat-square&color=4cd964&labelColor=0a0a0a)](https://github.com/minaryai/minary-agent/issues?q=is%3Aissue+is%3Aclosed)
[![PRs](https://img.shields.io/github/issues-pr-closed/minaryai/minary-agent?style=flat-square&color=ffb340&labelColor=0a0a0a&label=merged%20PRs)](https://github.com/minaryai/minary-agent/pulls?q=is%3Apr+is%3Aclosed)
[![Last commit](https://img.shields.io/github/last-commit/minaryai/minary-agent?style=flat-square&color=4cd964&labelColor=0a0a0a)](https://github.com/minaryai/minary-agent/commits/main)

</div>

<br/>

> **autonomous AI agent framework — self-improving runtime with built-in learning loops, multi-chain execution engine, 40+ tools, 200+ model routing targets.**

<br/>

## ⌬ what is this

minary is an **autonomous agent runtime** that observes, plans, acts, and learns from every execution cycle. unlike static pipelines, minary agents **create new skills from conversation**, persist memory across sessions, and self-improve through reward signals.

```
observe → plan → act → learn → persist
   ↑                              │
   └──────────────────────────────┘
         self-improvement loop
```

**key ideas:**
- **skill extraction** — agent watches its own successful tool-use chains and crystallizes them into reusable skills
- **recursive planning** — planner spawns sub-planners for complex tasks, merges results
- **multi-chain execution** — native Base + Solana transaction construction from LLM output
- **model routing** — automatic selection across 200+ models based on task complexity, latency budget, and cost
- **persistent memory** — cross-session knowledge graph with semantic retrieval

<br/>

## ⌬ quickstart

```bash
git clone https://github.com/minaryai/minary-agent
cd minary-agent
npm install
cp .env.example .env   # add your API keys
node src/cli.mjs
```

```bash
# or install globally
npm i -g minary-agent
minary-agent --help
```

```bash
# run with specific model
minary-agent --model claude-4.7-sonnet --task "analyze this repo"

# run with extended thinking
minary-agent --thinking 32k --task "plan a migration strategy"

# multi-chain mode
minary-agent --chain base,solana --task "check token holdings"
```

<br/>

## ⌬ architecture

```
minary-agent/
├── src/
│   ├── cli.mjs                 # entry point + arg parser
│   ├── core.mjs                # agent loop: observe → plan → act → learn
│   ├── config.mjs              # runtime configuration
│   ├── log.mjs                 # structured logging + trace export
│   └── util.mjs                # shared helpers
│
├── agents/
│   ├── planner.mjs             # recursive task decomposition
│   ├── executor.mjs            # tool-loop with max-N guard
│   ├── router.mjs              # model selection engine
│   ├── memory.mjs              # persistent knowledge graph
│   └── learner.mjs             # skill extraction + reward signals
│
├── tools/
│   ├── base-rpc.mjs            # Base chain interaction
│   ├── solana-rpc.mjs          # Solana transaction construction
│   ├── web-search.mjs          # search + scrape
│   ├── code-exec.mjs           # sandboxed code execution
│   ├── file-ops.mjs            # filesystem operations
│   └── ... (40+ tools)
│
├── prompts/
│   ├── system.md               # core system prompt
│   ├── planner.md              # planning instructions
│   ├── tool-use.md             # tool-use protocol
│   └── self-improve.md         # skill extraction prompt
│
├── evals/
│   ├── planning-suite.mjs      # plan quality benchmarks
│   ├── tool-use-suite.mjs      # tool accuracy tests
│   ├── reasoning-suite.mjs     # logical reasoning evals
│   ├── coding-suite.mjs        # code generation benchmarks
│   └── regression-gate.mjs     # CI regression gate
│
├── harness/
│   ├── runner.mjs              # eval harness orchestrator
│   ├── scorer.mjs              # multi-metric scoring
│   └── reporter.mjs            # results → markdown/json
│
├── docs/
│   ├── usage.md                # CLI reference
│   ├── architecture.md         # system design deep-dive
│   ├── model-routing.md        # routing algorithm docs
│   └── self-improvement.md     # learning loop explained
│
├── tests/
├── examples/
├── .github/
│   └── workflows/
│       ├── ci.yml              # lint + test + eval gate
│       └── heartbeat.yml       # automated health checks
│
├── .eslintrc.json
├── .prettierrc
├── .editorconfig
├── tsconfig.json
├── package.json
└── LICENSE
```

<br/>

## ⌬ model routing

minary routes tasks to the optimal model automatically. no manual model selection needed.

```
┌─────────────────────────────────────────────────────────┐
│                    model router                         │
│                                                         │
│   task complexity ──┐                                   │
│   latency budget ───┼──→ score matrix ──→ best model    │
│   cost ceiling ─────┘                                   │
│   prompt cache ─────────→ cache-aware routing           │
│                                                         │
│   fallback chain: primary → secondary → tertiary        │
└─────────────────────────────────────────────────────────┘
```

**supported model families:**

<div align="center">

![Claude](https://img.shields.io/badge/Claude-4.7_Sonnet_|_4.6_Opus_|_4.5_Haiku-191919?style=flat-square&logo=anthropic&logoColor=white)
![GPT](https://img.shields.io/badge/GPT-4.1_|_4.1_Mini-412991?style=flat-square&logo=openai&logoColor=white)
![Gemini](https://img.shields.io/badge/Gemini-2.5_Pro_|_2.5_Flash-4285F4?style=flat-square&logo=google&logoColor=white)
![Llama](https://img.shields.io/badge/Llama-4_Scout_|_4_Maverick-0467DF?style=flat-square&logo=meta&logoColor=white)
![DeepSeek](https://img.shields.io/badge/DeepSeek-R2-00A67E?style=flat-square)
![Qwen](https://img.shields.io/badge/Qwen-3-FF6A00?style=flat-square)

</div>

**routing heuristics:**
- **simple tasks** (classification, extraction) → haiku/flash/mini (fast, cheap)
- **reasoning tasks** (math, logic, planning) → opus/pro with extended thinking
- **code generation** → sonnet/gpt-4.1 (best code quality per dollar)
- **multi-step agents** → opus with 128k thinking budget
- **fallback** → if primary model 429s, auto-cascade to secondary

<br/>

## ⌬ built-in tools

<table>
<tr><th>Category</th><th>Tools</th><th>Description</th></tr>
<tr><td><b>Chain</b></td><td><code>base-rpc</code> <code>solana-rpc</code> <code>helius-rpc</code> <code>alchemy-rpc</code></td><td>on-chain reads, tx construction, token balances, swap routing</td></tr>
<tr><td><b>Search</b></td><td><code>web-search</code> <code>web-scrape</code> <code>arxiv</code> <code>github-search</code></td><td>real-time information retrieval</td></tr>
<tr><td><b>Code</b></td><td><code>code-exec</code> <code>code-review</code> <code>test-runner</code></td><td>sandboxed execution, static analysis, test generation</td></tr>
<tr><td><b>Memory</b></td><td><code>mem-store</code> <code>mem-retrieve</code> <code>mem-search</code></td><td>persistent knowledge with semantic retrieval</td></tr>
<tr><td><b>Files</b></td><td><code>file-read</code> <code>file-write</code> <code>file-search</code> <code>glob</code></td><td>filesystem operations with safety boundaries</td></tr>
<tr><td><b>Agent</b></td><td><code>agent-spawn</code> <code>agent-delegate</code> <code>skill-create</code></td><td>sub-agent orchestration, skill extraction</td></tr>
<tr><td><b>Eval</b></td><td><code>eval-run</code> <code>eval-compare</code> <code>regression-check</code></td><td>benchmark suites, A/B model comparison</td></tr>
<tr><td><b>Trace</b></td><td><code>trace-export</code> <code>trace-replay</code> <code>trace-analyze</code></td><td>execution traces for debugging + learning</td></tr>
</table>

all tools are exposed via **MCP protocol** — connect minary as a tool provider to Claude Desktop, Cursor, or any MCP client.

<br/>

## ⌬ self-improvement loop

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│   1. OBSERVE    agent executes task, records trace           │
│       ↓                                                      │
│   2. EVALUATE   scorer grades output quality                 │
│       ↓                                                      │
│   3. EXTRACT    successful patterns → new skills             │
│       ↓                                                      │
│   4. PERSIST    skills saved to memory, indexed              │
│       ↓                                                      │
│   5. APPLY      next task uses learned skills                │
│       ↓                                                      │
│   └──────────── back to OBSERVE ────────────────────────┘    │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

**what gets learned:**
- tool-use chains that consistently produce good results
- prompt patterns that improve model output quality
- routing decisions that optimize cost/quality tradeoffs
- error recovery patterns from failed executions

<br/>

## ⌬ multi-chain execution

native on-chain interaction without external bridges or wrappers.

| Chain | RPC | Capabilities |
|-------|-----|-------------|
| **Base** | `base-rpc` + `alchemy-rpc` | ERC-20 balances, contract reads, tx construction, gas estimation |
| **Solana** | `solana-rpc` + `helius-rpc` | SPL token ops, Jupiter swap routing, DAS API, priority fees |

```javascript
// agent can construct and simulate transactions from natural language
agent.run("swap 100 USDC to SOL on Jupiter with 1% slippage")
// → builds tx → simulates → returns for signing
```

<br/>

## ⌬ eval suite

every commit runs through the **regression gate** — no merge if eval scores drop.

```bash
# run full eval suite
node evals/runner.mjs --suite all

# run specific suite
node evals/runner.mjs --suite planning
node evals/runner.mjs --suite tool-use
node evals/runner.mjs --suite reasoning
node evals/runner.mjs --suite coding

# compare two models
node evals/runner.mjs --compare claude-4.7-sonnet gpt-4.1
```

| Suite | Metrics | Threshold |
|-------|---------|-----------|
| Planning | plan_quality, step_coherence, resource_efficiency | ≥ 0.80 |
| Tool-use | accuracy, tool_selection, error_recovery | ≥ 0.85 |
| Reasoning | correctness, chain_validity, conclusion_quality | ≥ 0.75 |
| Coding | pass_rate, code_quality, test_coverage | ≥ 0.82 |

<br/>

## ⌬ configuration

```bash
# .env
ANTHROPIC_API_KEY=sk-ant-...
OPENAI_API_KEY=sk-...
GOOGLE_AI_KEY=...
HELIUS_API_KEY=...
ALCHEMY_API_KEY=...

# optional
MINARY_MODEL=claude-4.7-sonnet     # default model
MINARY_THINKING=16k                # thinking budget
MINARY_CACHE=true                  # prompt caching
MINARY_MEMORY_DIR=~/.minary/memory # memory persistence path
MINARY_TRACE_DIR=~/.minary/traces  # trace export path
MINARY_LOG_LEVEL=info              # debug | info | warn | error
```

<br/>

## ⌬ MCP server

expose minary tools to any MCP-compatible client:

```bash
# start MCP server
minary-agent --mcp --port 3100

# or via stdio transport (for Claude Desktop)
minary-agent --mcp --transport stdio
```

```json
// claude_desktop_config.json
{
  "mcpServers": {
    "minary": {
      "command": "minary-agent",
      "args": ["--mcp", "--transport", "stdio"]
    }
  }
}
```

<br/>

## ⌬ stack

<div align="center">

![Node.js](https://img.shields.io/badge/node.js_20+-339933.svg?style=for-the-badge&logo=node.js&logoColor=white)
![JavaScript](https://img.shields.io/badge/ESM-f7df1e.svg?style=for-the-badge&logo=javascript&logoColor=black)
![MCP](https://img.shields.io/badge/MCP_Protocol-191919.svg?style=for-the-badge&logo=anthropic&logoColor=white)
![Solana](https://img.shields.io/badge/Solana-9945FF.svg?style=for-the-badge&logo=solana&logoColor=white)
![Base](https://img.shields.io/badge/Base-0052FF.svg?style=for-the-badge&logo=coinbase&logoColor=white)

</div>

<br/>

## ⌬ contributing

bug reports + feature requests → [issues](https://github.com/minaryai/minary-agent/issues). read [CONTRIBUTING.md](CONTRIBUTING.md) first.

security findings → [SECURITY.md](SECURITY.md). **do not open public issues for vulnerabilities.**

<br/>

## ⌬ roadmap

- [x] core agent loop (observe → plan → act → learn)
- [x] 40+ built-in tools
- [x] multi-model routing (200+ targets)
- [x] prompt caching (90%+ hit rate)
- [x] Base + Solana chain support
- [x] MCP server protocol
- [x] eval regression gate in CI
- [ ] recursive self-improvement loop (v0.6)
- [ ] agent-to-agent delegation protocol
- [ ] on-chain skill verification
- [ ] distributed agent swarm

see [open issues](https://github.com/minaryai/minary-agent/issues) for current priorities.

<br/>

## ⌬ license

MIT — see [LICENSE](LICENSE). © Minary.

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:16213e,50:1a1a2e,100:0a0a0a&height=120&section=footer&animation=fadeIn" alt="footer" />