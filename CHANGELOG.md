# changelog

## 0.1.0 — 2026-05-23

initial public scaffold.

- agent loop with tool execution + max-N guard
- planner / executor / router modules
- prompt management via .md files
- eval harness with planning + tool-use suites
- structured logging (pino)
- JSONL trace dump
- prompt caching (78% hit rate on eval suite)
- MCP server scaffold (4 tools)
- model router with fallback chain
- CI + evals workflow
- heartbeat workflow
