"""Run agent on a task and collect trace."""

import json
import time
from pathlib import Path


class Runner:
    def __init__(self, trace_dir: str = "./traces"):
        self.trace_dir = Path(trace_dir)
        self.trace_dir.mkdir(parents=True, exist_ok=True)

    def run(self, task: str, agent=None) -> dict:
        start = time.time()
        trace = {
            "task": task,
            "start": start,
            "turns": [],
            "status": "pending",
        }
        # placeholder: run agent, collect turns
        trace["status"] = "complete"
        trace["duration_ms"] = int((time.time() - start) * 1000)
        return trace

    def save_trace(self, trace: dict, name: str = "run"):
        ts = int(time.time())
        path = self.trace_dir / f"{name}-{ts}.jsonl"
        with open(path, "w") as f:
            f.write(json.dumps(trace) + "\n")
        return str(path)
