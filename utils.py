import requests
from textblob import TextBlob
from gtts import gTTS
from deep_translator import GoogleTranslator
from transformers import pipeline

# Load summarization model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# API key for NewsAPI
NEWS_API_KEY = "ddd025facff54a1f8c90c804042968cb"


def fetch_news(company):
    """Fetch news articles, summarize them, and return structured data."""
    url = (
        f"https://newsapi.org/v2/everything?"
        f"q={company}&apiKey={NEWS_API_KEY}&language=en&pageSize=15"
    )

    response = requests.get(url)

    if response.status_code != 200:
        return []

    data = response.json()
    articles = data.get("articles", [])

    news_list = []
    for article in articles[:10]:
        full_text = article.get("content", article.get("description", "No full article available."))

        try:
            summary = summarizer(full_text, max_length=80, min_length=30, do_sample=False)[0]['summary_text']
        except Exception:
            summary = "Summary not available."

        news_list.append({
            "title": article["title"],
            "summary": summary,  # Store summarized text
            "url": article["url"]
        })

    return news_list


def analyze_sentiment(text):
    """Classify sentiment as Positive, Negative, or Neutral."""
    sentiment = TextBlob(text).sentiment.polarity

    if sentiment > 0:
        return "Positive"
    elif sentiment < 0:
        return "Negative"
    return "Neutral"


def comparative_analysis(articles):
    """Analyze sentiment distribution across multiple articles."""
    sentiment_count = {"Positive": 0, "Negative": 0, "Neutral": 0}

    for article in articles:
        sentiment = analyze_sentiment(article["summary"])
        article["sentiment"] = sentiment
        sentiment_count[sentiment] += 1

    return sentiment_count


def text_to_speech(text):
    """Convert text into both English and Hindi speech using gTTS."""
    
    # Generate English speech
    english_tts = gTTS(text=text, lang="en")
    english_file = "output_english.mp3"
    english_tts.save(english_file)

    # Translate text to Hindi
    translated_text = GoogleTranslator(source="en", target="hi").translate(text)

    # Generate Hindi speech
    hindi_tts = gTTS(text=translated_text, lang="hi")
    hindi_file = "output_hindi.mp3"
    hindi_tts.save(hindi_file)

    return english_file, hindi_file