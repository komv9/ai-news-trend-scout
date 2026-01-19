# agent/analyze.py
from agent.llm import run_llm

def analyze_articles(articles):
    prompt = f"""
You are an AI trend analyst.

Analyze the following news articles and:
1. Identify key technology trends
2. Say if they are new or recurring

Return a concise summary.

Articles:
{articles[:5]}
"""
    return run_llm(prompt)
