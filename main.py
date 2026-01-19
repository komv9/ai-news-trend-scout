# main.py
from datetime import date
from agent.fetch_news import fetch_news
from agent.analyze import analyze_articles
from agent.memory import init_db, save_insight

def run_agent():
    init_db()
    articles = fetch_news()
    insight = analyze_articles(articles)
    save_insight(str(date.today()), insight)
    print("Agent insight:\n", insight)

if __name__ == "__main__":
    run_agent()
