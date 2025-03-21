from fastapi import FastAPI
from pydantic import BaseModel
from utils import fetch_news, analyze_sentiment, comparative_analysis, text_to_speech

# Initialize FastAPI app
app = FastAPI()

# Define request model for API requests
class ArticlesRequest(BaseModel):
    company: str  # Expected company name input


@app.get("/scrape")
def get_news(company: str):
    """Fetch news articles for a given company and analyze sentiment."""
    articles = fetch_news(company)

    if not articles:
        return {"error": "No news articles found."}

    sentiment_summary = comparative_analysis(articles)

    return {
        "company": company,
        "articles": articles,
        "sentiment_summary": sentiment_summary
    }


@app.get("/tts")
def get_tts(text: str):
    """Convert summarized text to Hindi speech and return filename."""
    filename = text_to_speech(text)
    return {"audio_file": filename}