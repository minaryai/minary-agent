"""Execute tool calls from a plan or model response."""

import json
from typing import Any


class Executor:
    """Run tools returned by the model."""

    def __init__(self, tool_registry: dict | None = None, max_iterations: int = 8):
        self.tools = tool_registry or {}
        self.max_iterations = max_iterations

    def register(self, name: str, handler: Any, schema: dict | None = None):
        self.tools[name] = {"handler": handler, "schema": schema}

    async def execute(self, tool_name: str, args: dict) -> dict:
        if tool_name not in self.tools:
            return {"error": f"unknown tool: {tool_name}"}
        try:
            result = await self.tools[tool_name]["handler"](**args)
            return {"result": result}
        except Exception as e:
            return {"error": str(e)}
