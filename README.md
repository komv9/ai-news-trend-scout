# ai-news-trend-scout

# AI News & Trend Scout 🤖🗞️

An autonomous AI agent that monitors real-world news data, detects emerging technology trends, and stores insights over time using structured memory.

## Why This Project Matters
This project demonstrates how to build a real-world AI agent using live data, structured memory, and LLM reasoning — without relying on paid APIs. It reflects production-style system design rather than toy examples.

## 🚀 What This Project Does
- Ingests real-time news via public APIs
- Uses LLM reasoning to identify and summarize trends
- Detects recurring vs emerging topics
- Stores insights in a persistent SQLite database
- Designed with pluggable LLM providers

## 🧠 Architecture Overview
Data Ingestion → AI Reasoning → Decision Logic → Memory Storage

The agent is LLM-agnostic and supports multiple inference modes.

## 🔌 LLM Providers
This project supports interchangeable LLM backends:

- **Ollama (Local, Free)** – Default for development
- **Mock LLM** – Used for cloud demos (no GPU required)
- **Cloud LLM** – Extendable to Groq / HuggingFace / OpenAI

Switch providers using environment variables:
```bash
export LLM_PROVIDER=ollama   # local
export LLM_PROVIDER=mock     # cloud/demo


ai-news-trend-scout/
│
├── agent/
│   ├── __init__.py
│   ├── fetch_news.py        # News API ingestion
│   ├── analyze.py           # Agent reasoning logic
│   ├── memory.py            # SQLite storage
│   └── llm.py               # ⭐ LLM adapter (IMPORTANT)
│
├── data/
│   └── trends.db            # SQLite DB (auto-created)
│
├── config/
│   └── settings.py          # API keys, env vars
│
├── main.py                  # Agent loop entry point
├── requirements.txt
├── .env.example
├── README.md
└── .gitignore
