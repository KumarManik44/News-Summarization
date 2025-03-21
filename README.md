# News Summarization & Sentiment Analysis with TTS
A web-based application that fetches news articles for a given company, summarizes them, analyzes their sentiment, and provides an audio summary in Hindi.

Project Overview:

This project is a news summarization and sentiment analysis application with text-to-speech (TTS) functionality. It allows users to fetch news articles about a company, summarize them, analyze their sentiment, and convert the summary into English and Hindi speech.

The application is built using FastAPI for the backend and Streamlit for the frontend, with Hugging Face models for summarization and sentiment analysis.

Features:
- Fetch real-time news articles about a company
- Summarize articles using a transformer-based model
- Perform sentiment analysis (Positive, Negative, Neutral)
- Convert summarized news to English and Hindi speech
- Accessible via API (FastAPI) and Web UI (Streamlit)

Tech Stack:
- fastapi - For building the API.
- uvicorn - ASGI server to run FastAPI.
- requests - To fetch data from NewsAPI.
- streamlit - To create the web interface.
- textblob - For sentiment analysis.
- gtts - For text-to-speech (TTS) conversion.
- deep-translator - To translate text into Hindi.
- transformers - For text summarization (BART model).
- torch - Required for running the transformer model.
- pydantic - For data validation in FastAPI

Project Setup:
1. Clone the Repository
2. Install Dependencies
3. Run the FastAPI Backend
4. Run the Streamlit Frontend

Model Details:
1. Summarization Model
  - Uses facebook/bart-large-cnn from Hugging Face Transformers.
  - Extracts the most relevant information from news articles and generates a short summary.
2. Sentiment Analysis
  - Uses TextBlob to classify sentiment into Positive, Negative, or Neutral.
  - Sentiment polarity is determined based on the summary text.
3. Text-to-Speech (TTS)
  - English Speech: Uses gTTS (Google Text-to-Speech) to generate English audio.
  - Hindi Translation & Speech: Uses GoogleTranslator to translate text to Hindi and then convert it into speech using gTTS.

API Development & Usage:
1. Fetch News & Analyze Sentiment
2. Convert Text to Speech
3. Testing with Postman

Third-Party API Integrations:
- NewsAPI	- Fetches real-time news articles based on the given company name.
- Hugging Face Transformers -	Provides the facebook/bart-large-cnn model for text summarization.
- TextBlob	- Performs sentiment analysis on summarized text.
- GoogleTranslator	- Translates English summaries into Hindi.
- gTTS - (Google Text-to-Speech)	Converts English and Hindi text into speech.

License:
- This project is licensed under the MIT License.

Credits:
- Developed by Kumar Manik
- NewsAPI.org for real-time news
- Hugging Face Spaces for easy deployment

This README.md is detailed and contains all necessary steps for setup, deployment, and usage.
