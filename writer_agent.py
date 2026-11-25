from agents import Agent
from pydantic import BaseModel, Field

from model_config import settings, writer_model

INSTRUCTIONS = """
You are a senior researcher tasked with writing a cohesive report for a research query.
You will be provided with the original query, and some research.
Generate a comprehensive report based on the research and the query.
The final output should be in markdown format, between 1000 and 1500 words.
"""


class ReportData(BaseModel):
    short_summary: str = Field(description="A short 2-3 sentence summary of the findings.")
    markdown_report: str = Field(description="The final report")
    follow_up_questions: list[str] = Field(description="Suggested topics to research further")


writer_agent = Agent(
    name="Writer Agent",
    instructions=INSTRUCTIONS,
    model=writer_model,
    # Input (~2.5K) + this cap must stay under the 8K tokens-per-minute free limit.
    model_settings=settings(5000),
    output_type=ReportData,
)