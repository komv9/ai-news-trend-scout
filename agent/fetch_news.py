# agent/fetch_news.py
import requests
from config import NEWS_API_KEY

def fetch_news():
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": "artificial intelligence OR data engineering",
        "language": "en",
        "pageSize": 5,
        "apiKey": NEWS_API_KEY,
    }

    response = requests.get(url, params=params)
    data = response.json()
    return data.get("articles", [])
