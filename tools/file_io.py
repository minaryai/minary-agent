"""File I/O tools for the agent."""

from pathlib import Path


def read_file(path: str) -> str:
    """Read a file and return its contents."""
    return Path(path).read_text()


def write_file(path: str, content: str) -> str:
    """Write content to a file."""
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content)
    return f"wrote {len(content)} bytes to {path}"
