"""Plan generation for multi-step tasks."""

from dataclasses import dataclass, field


@dataclass
class Plan:
    """Execution plan produced by the planner."""
    steps: list[dict] = field(default_factory=list)
    model: str = "claude-4.7-sonnet"
    thinking_budget: int = 10000


class Planner:
    """Generate structured plans from natural language tasks."""

    def __init__(self, model: str = "claude-4.7-sonnet"):
        self.model = model

    async def plan(self, task: str, constraints: list[str] | None = None) -> Plan:
        """Generate a plan. Override in subclass or inject via config."""
        raise NotImplementedError("planner.plan() is a scaffold — wire up your LLM client")
