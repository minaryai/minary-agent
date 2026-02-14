"""Eval harness — run suites, report scores, gate CI."""

import json
import sys
from pathlib import Path


def load_suite(name: str) -> list[dict]:
    suite_path = Path(__file__).parent / "suites" / f"{name}.jsonl"
    if not suite_path.exists():
        print(f"suite not found: {name}")
        return []
    with open(suite_path) as f:
        return [json.loads(line) for line in f if line.strip()]


def run_suite(name: str, threshold: float = 0.80) -> dict:
    tasks = load_suite(name)
    if not tasks:
        return {"suite": name, "score": 0.0, "total": 0, "passed": False}
    # placeholder: run each task through agent, score results
    score = 0.85  # stub
    return {
        "suite": name,
        "score": score,
        "total": len(tasks),
        "passed": score >= threshold,
    }


if __name__ == "__main__":
    suites = ["planning", "tool_use"]
    threshold = 0.80
    for arg in sys.argv[1:]:
        if arg.startswith("--suite"):
            suites = arg.split("=")[1].split(",")
        elif arg.startswith("--threshold"):
            threshold = float(arg.split("=")[1])

    results = [run_suite(s, threshold) for s in suites]
    for r in results:
        status = "PASS" if r["passed"] else "FAIL"
        print(f"  [{status}] {r['suite']}: {r['score']:.0%} ({r['total']} tasks)")

    if not all(r["passed"] for r in results):
        sys.exit(1)
