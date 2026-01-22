"""Model routing with fallback chains."""

from dataclasses import dataclass


@dataclass
class ModelConfig:
    name: str
    max_tokens: int = 8192
    thinking_budget: int | None = None
    cache_system: bool = True


# default chain: claude-4.7 -> claude-4.6 -> haiku
DEFAULT_CHAIN = [
    ModelConfig("claude-4.7-sonnet", thinking_budget=10000),
    ModelConfig("claude-4.6-opus"),
    ModelConfig("claude-4.5-haiku", max_tokens=4096),
]


class Router:
    """Select model based on task complexity and availability."""

    def __init__(self, chain: list[ModelConfig] | None = None):
        self.chain = chain or DEFAULT_CHAIN

    def route(self, task_complexity: str = "medium") -> ModelConfig:
        if task_complexity == "low":
            return self.chain[-1]
        return self.chain[0]
