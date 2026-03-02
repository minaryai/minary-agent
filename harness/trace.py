"""Trace data structures."""

from dataclasses import dataclass, field
from typing import Any


@dataclass
class Turn:
    role: str  # "user" | "assistant" | "tool"
    content: Any = None
    tool_name: str | None = None
    tool_args: dict | None = None
    tool_result: Any = None
    model: str | None = None
    tokens_in: int = 0
    tokens_out: int = 0
    cache_hit: bool = False
    thinking: str | None = None


@dataclass
class Trace:
    task: str
    turns: list[Turn] = field(default_factory=list)
    model: str = "claude-4.7-sonnet"
    total_tokens_in: int = 0
    total_tokens_out: int = 0
    cache_hit_rate: float = 0.0
    duration_ms: int = 0
    status: str = "pending"
