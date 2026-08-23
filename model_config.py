import os
from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import OpenAIChatCompletionsModel

load_dotenv(override=True)

GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GROQ_BASE_URL = "https://api.groq.com/openai/v1"
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

groq_client = AsyncOpenAI(
    base_url=GROQ_BASE_URL,
    api_key=GROQ_API_KEY
)

gemini_client = AsyncOpenAI(
    base_url=GEMINI_BASE_URL,
    api_key=GEMINI_API_KEY
)

openrouter_client = AsyncOpenAI(
    base_url=OPENROUTER_BASE_URL,
    api_key=OPENROUTER_API_KEY,
    default_headers={
        "HTTP-Referer": "http://localhost:7860",
        "X-Title": "Deep Research Multi-Agent"
    },
    default_query={"max_tokens": 4096}
)

gemini_model = OpenAIChatCompletionsModel(
    model="qwen/qwen3.6-27b",
    openai_client=groq_client
)





# 1. Planner Model: Fast schema generation & JSON compliance
planner_model = OpenAIChatCompletionsModel(
    model="qwen/qwen3.6-27b",
    openai_client=groq_client,
    
)

# 2. Search Agent Model: Rapid parallel tool calling & snippet extraction
search_model = OpenAIChatCompletionsModel(
    model="openrouter/free",
    openai_client=openrouter_client,
  
)

# 3. Writer Model: Deep reasoning & high-quality long-form markdown synthesis
writer_model = OpenAIChatCompletionsModel(
    model="openai/gpt-oss-120b",
    openai_client=openrouter_client,
  
)

# 4. Email / Messenger Model: Fast formatting & concise summarization
email_model = OpenAIChatCompletionsModel(
    model="nvidia/nemotron-3-super-120b-a12b:free",
    openai_client=openrouter_client,
   
)