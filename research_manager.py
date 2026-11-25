import asyncio
import logging
import os

from agents import Runner, gen_trace_id, trace

from email_agent import email_agent
from model_config import TRACING_ENABLED
from planner_agent import WebSearchItem, WebSearchPlan, planner_agent
from search_agent import search_agent
from structured import run_structured
from writer_agent import ReportData, writer_agent

logger = logging.getLogger(__name__)

SEARCH_CONCURRENCY = int(os.getenv("SEARCH_CONCURRENCY", 2))


class ResearchManager:

    async def run(self, query: str):
        """ Run the deep research process, yielding the status updates and the final report"""
        trace_id = gen_trace_id()
        with trace("Research trace", trace_id=trace_id):
            if TRACING_ENABLED:
                yield f"Starting research. Trace: https://platform.openai.com/traces/trace?trace_id={trace_id}"
            stage = "planning"
            try:
                yield "Planning searches..."
                search_plan = await self.plan_searches(query)
                stage = "searching"
                yield f"Searches planned, starting {len(search_plan.searches)} searches..."
                search_results = await self.perform_searches(search_plan)
                stage = "writing"
                yield "Searches complete, writing report..."
                report = await self.write_report(query, search_results)
            except Exception as e:
                logger.exception("Research failed while %s", stage)
                yield f"**Research failed while {stage}:** `{type(e).__name__}: {e}`"
                return

            yield "Report written, sending email..."
            try:
                await self.send_email(report)
                status = "Email sent, research complete"
            except Exception as e:
                logger.exception("Email failed")
                status = f"**Email failed:** `{type(e).__name__}: {e}`"
            # Always show the report, even if delivery failed.
            yield f"{status}\n\n---\n\n{report.markdown_report}"

    async def plan_searches(self, query: str) -> WebSearchPlan:
        """ Plan the searches to perform for the query """
        return await run_structured(planner_agent, f"Query: {query}", WebSearchPlan)

    async def perform_searches(self, search_plan: WebSearchPlan) -> list[str]:
        """ Run the planned searches with bounded concurrency, tolerating partial failure """
        limit = asyncio.Semaphore(SEARCH_CONCURRENCY)

        async def bounded(item: WebSearchItem) -> str | None:
            async with limit:
                return await self.search(item)

        results = await asyncio.gather(*(bounded(i) for i in search_plan.searches))
        successful = [r for r in results if r]
        if not successful:
            raise RuntimeError("Every search failed. Check the terminal log for the cause.")
        return successful

    async def search(self, item: WebSearchItem) -> str | None:
        """ Perform a search for the query """
        input_message = f"Search term: {item.query}\nReason for searching: {item.reason}"
        try:
            result = await Runner.run(search_agent, input_message)
        except Exception:
            logger.exception("Search failed: %s", item.query)
            return None
        return result.final_output

    async def write_report(self, query: str, search_results: list[str]) -> ReportData:
        """ Write the report for the query """
        research = "\n\n---\n\n".join(search_results)
        input_message = f"Original query: {query}\n\nSummarized search results:\n\n{research}"
        return await run_structured(writer_agent, input_message, ReportData)

    async def send_email(self, report: ReportData) -> None:
        await Runner.run(email_agent, f"Report summary: {report.short_summary}", context=report)