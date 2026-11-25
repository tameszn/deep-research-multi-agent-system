from agents import Agent, function_tool
from ddgs import DDGS

from model_config import search_model, settings

INSTRUCTIONS = """
You are a research assistant. Given a search term, call web_search once, then
produce a concise summary of the results. The summary must be 2-3 paragraphs and less than 250 words.
Capture the main points and be succinct. Reply only with the summary.
"""


@function_tool
def web_search(query: str) -> str:
    """Search the web for a given query and return top results with titles, snippets, and URLs."""
    try:
        results = DDGS().text(query, max_results=5)
    except Exception as e:
        return f"Search failed: {e}"

    if not results:
        return "No results found."

    return "\n\n".join(
        f"Title: {r['title']}\nSnippet: {r.get('body', '')[:500]}\nURL: {r['href']}"
        for r in results
    )


search_agent = Agent(
    name="Search Agent",
    instructions=INSTRUCTIONS,
    tools=[web_search],
    model=search_model,
    # The SDK resets tool_choice after the first call, so the summary turn is free text.
    model_settings=settings(1200, tool_choice="required"),
)
