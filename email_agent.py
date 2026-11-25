import os

import markdown
from agents import Agent, RunContextWrapper, function_tool
from dotenv import load_dotenv

from messenger import push, send_email
from model_config import email_model, settings
from writer_agent import ReportData

load_dotenv(override=True)


USE_EMAIL = os.getenv("USE_EMAIL", "true").lower() == "true"

EMAIL_TEMPLATE = (
    '<html><body style="font-family:Arial,sans-serif;line-height:1.6;'
    'max-width:720px;margin:auto;padding:16px">{body}</body></html>'
)


# failure_error_function=None: an SMTP error must raise, not be reported to the model as text.
@function_tool(failure_error_function=None)
def send_email_tool(ctx: RunContextWrapper[ReportData], subject: str) -> str:
    """
    Email the finished report with the given subject line.

    Args:
        subject: The subject of the email
    """
    report = ctx.context.markdown_report
    if USE_EMAIL:
        body = markdown.markdown(report, extensions=["tables", "fenced_code", "sane_lists"])
        send_email(subject, report, EMAIL_TEMPLATE.format(body=body))
    else:
        push(f"Subject: {subject}\n\n{report}")
    return "Email sent successfully"


INSTRUCTIONS = """
You are given the summary of a research report. Call send_email_tool once with a clear,
specific subject line. The report body is attached automatically.
"""

email_agent = Agent[ReportData](
    name="Email Agent",
    instructions=INSTRUCTIONS,
    tools=[send_email_tool],
    model=email_model,
    model_settings=settings(500, tool_choice="required"),
    tool_use_behavior="stop_on_first_tool",
)