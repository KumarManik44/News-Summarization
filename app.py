import streamlit as st
from utils import fetch_news, text_to_speech, analyze_sentiment, comparative_analysis

# Set page title
st.title("News Summarization & Sentiment Analysis with TTS")

# Input for company name
company = st.text_input("Enter Company Name")

# Button to fetch news
if st.button("Fetch News"):
    articles = fetch_news(company)

    if not articles:
        st.error("No news articles found. Try a different company.")
    else:
        sentiment_summary = comparative_analysis(articles)

        full_text = ""
        for news in articles:
            title = news["title"]
            summary = news["summary"]
            sentiment = analyze_sentiment(summary)

            # Display news title, summary, and sentiment
            st.subheader(title)
            st.write(summary)
            st.write(f"**Sentiment:** {sentiment}")
            st.write(f"[Read Full Article]({news['url']})")

            # Append summary for speech synthesis
            full_text += f"{title}: {summary}. "

        # Display sentiment summary
        st.subheader("Sentiment Analysis Summary")
        st.json(sentiment_summary)

        # Convert summarized text to speech (English & Hindi)
        english_speech, hindi_speech = text_to_speech(full_text)

        # Display and play English news audio
        st.subheader("English News")
        st.audio(english_speech)

        # Display and play Hindi news audio
        st.subheader("Hindi News")
        st.audio(hindi_speech)