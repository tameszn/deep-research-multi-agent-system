import os

from agents import ModelSettings, OpenAIChatCompletionsModel, set_tracing_disabled
from dotenv import load_dotenv
from openai import AsyncOpenAI
from openai.types.shared import Reasoning

load_dotenv(override=True)

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise RuntimeError("GROQ_API_KEY is missing. Add it to your .env file.")

# Traces upload to OpenAI, so they need an OpenAI key.
TRACING_ENABLED = bool(os.getenv("OPENAI_API_KEY"))
set_tracing_disabled(not TRACING_ENABLED)

groq_client = AsyncOpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=GROQ_API_KEY,
    max_retries=8,  # rides out 429s; the client honours Retry-After
)

FAST_MODEL = os.getenv("FAST_MODEL", "openai/gpt-oss-20b")
# Separate rate-limit bucket from FAST_MODEL, and better long-form output.
WRITER_MODEL = os.getenv("WRITER_MODEL", "openai/gpt-oss-120b")


def _groq(model: str) -> OpenAIChatCompletionsModel:
    return OpenAIChatCompletionsModel(model=model, openai_client=groq_client)


def settings(max_tokens: int, **kwargs) -> ModelSettings:
    """Low reasoning effort and capped output, to fit Groq's tokens-per-minute limit."""
    return ModelSettings(max_tokens=max_tokens, reasoning=Reasoning(effort="low"), **kwargs)


planner_model = _groq(FAST_MODEL)
search_model = _groq(FAST_MODEL)
email_model = _groq(FAST_MODEL)
writer_model = _groq(WRITER_MODEL)