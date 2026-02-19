# usage

## quickstart

```bash
git clone https://github.com/minaryai/minary-agent
cd minary-agent
npm i
pip install -e ".[dev]"
```

## run the agent

```bash
node src/cli.mjs "your task here"
```

## environment variables

| var | default | description |
|-----|---------|-------------|
| `MINARY_MODEL` | claude-4.7-sonnet | primary model |
| `MINARY_FALLBACK` | claude-4.6-opus | fallback model |
| `TOOL_LOOP_MAX_N` | 8 | max tool iterations |
| `THINKING_BUDGET` | 10000 | extended thinking token budget |
| `ENABLE_CACHE` | true | prompt caching |
| `ENABLE_THINKING` | true | extended thinking |
| `LOG_LEVEL` | warn | pino log level |
| `TRACE_DIR` | ./traces | trace output directory |

## eval suite

```bash
python -m evals.harness --suite planning,tool_use --threshold 0.80
```
