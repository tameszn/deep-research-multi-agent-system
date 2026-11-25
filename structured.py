"""Reliable structured output on Groq, which can intermittently fail JSON validation for gpt-oss."""
import json
import logging
from typing import TypeVar

from agents import Agent, ModelBehaviorError, Runner
from openai import BadRequestError
from pydantic import BaseModel

logger = logging.getLogger(__name__)

T = TypeVar("T", bound=BaseModel)

STRICT_ATTEMPTS = 2


async def run_structured(agent: Agent, prompt: str, schema: type[T]) -> T:
    """Try strict structured output, then fall back to prompted JSON validated locally."""
    for attempt in range(1, STRICT_ATTEMPTS + 1):
        try:
            return (await Runner.run(agent, prompt)).final_output
        except BadRequestError as e:
            if e.code != "json_validate_failed":
                raise
            logger.warning("%s: JSON validation failed (attempt %d)", agent.name, attempt)
        except ModelBehaviorError:  # truncated or malformed JSON
            logger.warning("%s: unparseable output (attempt %d)", agent.name, attempt)

    logger.warning("%s: falling back to prompted JSON", agent.name)
    fallback = agent.clone(
        output_type=None,
        instructions=(
            f"{agent.instructions}\n"
            "Reply with only a JSON object, without code fences, matching this JSON schema:\n"
            f"{json.dumps(schema.model_json_schema())}"
        ),
    )
    text = (await Runner.run(fallback, prompt)).final_output
    return parse_json(text, schema)


def parse_json(text: str, schema: type[T]) -> T:
    """Parse the outermost JSON object, tolerating surrounding text and raw newlines."""
    start, end = text.find("{"), text.rfind("}")
    if start == -1 or end < start:
        raise ValueError(f"Model returned no JSON object: {text[:200]!r}")
    return schema.model_validate(json.loads(text[start : end + 1], strict=False))