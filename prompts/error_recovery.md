# error recovery

when a tool call fails:
1. parse the error message
2. check if it's retryable (rate limit, timeout, transient)
3. if retryable: wait and retry (max 2 attempts)
4. if not retryable: report to planner with context
5. never retry more than TOOL_LOOP_MAX_N times total
