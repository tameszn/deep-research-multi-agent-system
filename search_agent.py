from agents import Agent, WebSearchTool, ModelSettings,function_tool
from ddgs import DDGS
from model_config import search_model, gemini_model

INSTRUCTIONS = """
You are a research assistant. Given a search term, you search the web for that term and 
produce a concise summary of the results. The summary must 2-3 paragraphs and less than 300 words.
Capture the main points and be succinct. Reply only with the summary.
"""

settings = ModelSettings(tool_choice="required")

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
        f"Title: {r['title']}\nSnippet: {r.get('body', '')}\nURL: {r['href']}"
        for r in results
    )
tools = [web_search]

search_agent = Agent(name="Search Agent", instructions=INSTRUCTIONS, tools=tools, model=search_model, model_settings=settings)