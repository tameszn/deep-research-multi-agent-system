

# InQuery 🌐🧑‍💻

> A multi-agent research tool that searches the web, analyzes data, and emails detailed reports directly to you.

---

## 🎯 The Problem It Solves

InQuery automates web research. It is built for people who need accurate, well-organized information without spending hours manually collecting it:

* **Market Researchers & Analysts:** Get quick, structured, and deep summaries on industry trends without manually reading and saving multiple sources.
* **Executives & Founders:** Receive fast, accurate intelligence briefs delivered straight to your inbox, providing the facts needed for high-stakes decision-making.
* **Academics & Writers:** Gather verified source data and outlines to start research papers or long-form articles.
## ✨ Key Features

* **⚡ Parallel Agent Pipeline:** Multi-threaded agents search, analyze, and write simultaneously, cutting down hours of manual research into mere minutes.
* **🧠 Data Verification:** The analytical agent intelligently filters out noise and cross-references data points to ensure the final intelligence report is highly accurate and fact-checked.
* **📬 Hands-Off Inbox Delivery:** The system automatically formats, proofreads, and emails the final report to you—no need to keep the app open while it works.

## 🛠 Tech Stack

Built with a modern, scalable Python ecosystem leveraging cutting-edge LLMs and agentic frameworks:

* **Language:** Python
* **Agent Frameworks:** `openai-agents`
* **AI Models:** Google GenAI (Gemini)
* **Search Engine:** DuckDuckGo Search (`ddgs`)
* **Data Validation:** `Pydantic`
* **Web Interface:** `Gradio`
* **Formatting & Delivery:** `Requests`, `Markdown`, `Resend API`

## 🚀 Getting Started

### Prerequisites
* Python 3.10 or higher
* `pip` (Python package installer)

### Installation & Run Instructions

**1. Navigate to the project directory:**
```bash
cd inquery
```

**2. Create and activate a virtual environment:**
```bash
python -m venv venv

# On Linux/macOS:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

**3. Install dependencies:**
```bash
pip install gradio openai-agents pydantic google-genai duckduckgo_search requests markdown resend python-dotenv
```

**4. Set up environment variables:**
Create a `.env` file in the root of your project directory and add the necessary API keys for the services being used:
```env
# Example .env configuration
GEMINI_API_KEY="your-gemini-api-key"

# Add any other required agent keys
```

**5. Start the application:**
```bash
python main.py  # Replace with the actual name of your entry Python script
```

**6. Test Locally:**
Once the server is running, open your browser and navigate to the local Gradio interface:
[http://127.0.0.1:7860](http://127.0.0.1:7860)

---






