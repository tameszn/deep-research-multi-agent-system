import html

import gradio as gr
from dotenv import load_dotenv

from research_manager import ResearchManager
from styles import CSS, EXAMPLES, HEAD, HEADER_HTML, REMINDER_HTML

load_dotenv(override=True)

# Separates the status line from the report in ResearchManager's final update.
REPORT_SEPARATOR = "\n\n---\n\n"
DONE_STATUS = "Email sent, research complete"


def status_pill(message: str) -> str:
    """Render a ResearchManager status line as a pill with a state dot."""
    if message.startswith(("**Research failed", "**Email failed")):
        kind = "error"
    elif message == DONE_STATUS:
        kind, message = "done", "Research complete · Email sent"
    else:
        kind = "busy"

    # Escape: error text can contain model output.
    text = html.escape(" ".join(message.replace("**", "").replace("`", "").split()))
    prefix = "Starting research. Trace: "
    if text.startswith(prefix):
        url = text.removeprefix(prefix)
        text = f'Starting research · <a href="{url}" target="_blank" rel="noopener">View trace</a>'

    return (
        f'<div class="dr-status dr-status-{kind}" role="status">'
        f'<span class="dr-dot"></span><span>{text}</span></div>'
    )


async def run(query: str):
    if not query.strip():
        gr.Warning("Type a research question first.")
        return
    async for update in ResearchManager().run(query):
        status, separator, body = update.partition(REPORT_SEPARATOR)
        yield status_pill(status) + (f"\n\n{body}" if separator else "")


with gr.Blocks(title="Deep Research") as ui:
    gr.HTML(HEADER_HTML, padding=False)

    with gr.Row(elem_id="dr-search", elem_classes="dr-query-row", equal_height=True):
        query_textbox = gr.Textbox(
            placeholder="Type a research question...",
            show_label=False,
            container=False,
            autofocus=True,
            max_lines=1,
            elem_id="dr-query",
            scale=5,
        )
        run_button = gr.Button("Run", variant="primary", elem_id="dr-run", scale=0)

    gr.HTML('<div class="dr-examples-label">Try one</div>', padding=False)
    # Plain buttons rather than gr.Examples, which cuts off long prompts.
    # Both sets are rendered; CSS shows the one matching the active theme.
    with gr.Column(elem_id="dr-examples"):
        for theme_name, prompts in EXAMPLES.items():
            with gr.Row(elem_id=f"dr-examples-{theme_name}"):
                for prompt in prompts:
                    gr.Button(prompt, elem_classes="dr-example", scale=0).click(
                        lambda value=prompt: value,
                        outputs=query_textbox,
                        show_progress="hidden",
                    )

    # The status pill shows progress, so Gradio's loading overlay is hidden.
    report = gr.Markdown(elem_id="dr-report")

    gr.HTML(REMINDER_HTML, elem_id="dr-reminder", padding=False)

    run_button.click(run, inputs=query_textbox, outputs=report, show_progress="hidden")
    query_textbox.submit(run, inputs=query_textbox, outputs=report, show_progress="hidden")


if __name__ == "__main__":
    # Gradio 6 takes css/head in launch() rather than in gr.Blocks().
    ui.launch(server_name="0.0.0.0", css=CSS, head=HEAD, theme=gr.themes.Base())
    # test locally at this link- http://127.0.0.1:7860/