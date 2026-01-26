# router prompt

given a task, classify its complexity:
- **low**: single tool call, factual lookup, simple formatting
- **medium**: 2-5 tool calls, requires reasoning, standard workflow
- **high**: 6+ tool calls, multi-step planning, novel problem solving

respond with JSON: {"complexity": "low|medium|high", "reasoning": "..."}
