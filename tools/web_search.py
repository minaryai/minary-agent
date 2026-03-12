"""Web search tool — placeholder for external search API."""


async def search(query: str, limit: int = 10) -> list[dict]:
    """Search the web. Wire up your preferred search API."""
    # placeholder: integrate with Tavily, SerpAPI, or similar
    return [{"title": "placeholder", "url": "https://example.com", "snippet": f"result for: {query}"}]
