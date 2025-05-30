# 🦜LangChain Summarizer for YouTube & Websites

This is a **Streamlit web application** that allows users to **summarize the content** of any YouTube video or web page using **LangChain**, **Groq LLM**, and **LangChain's document loaders**.

## Features

* Summarizes YouTube videos or any website content
* Uses `LangChain` and `ChatGroq` with `gemma2-9b-it` model
* User-friendly Streamlit interface
* Secure input for your Groq API key
* Approximately 300-word summary in simple, easy-to-understand language

## Requirements

* Groq API Key

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/langchain-summarizer.git
   cd langchain-summarizer
   ```

2. **Create a virtual environment and activate it**

   ```bash
   conda activate venv/
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

## Run the App

```bash
streamlit run app.py
```

## How to Use

1. Enter your **Groq API key** in the sidebar.
2. Paste a **YouTube or Website URL** in the input box.
3. Click the **"Summarize Content"** button.
4. The app will fetch and summarize the content in a readable 300-word format.

## Technologies Used

* [Streamlit](https://streamlit.io/) – for web UI
* [LangChain](https://python.langchain.com/) – to build the summarization chain
* [LangChain-Groq](https://github.com/langchain-ai/langchain-groq) – for LLM integration
* [YoutubeLoader](https://api.python.langchain.com/en/latest/loaders/langchain_community.document_loaders.YoutubeLoader.html) – for YouTube transcript
* [UnstructuredURLLoader](https://api.python.langchain.com/en/latest/loaders/langchain_community.document_loaders.UnstructuredURLLoader.html) – for webpage content

## Notes

* You must have a **valid Groq API key** to use this app.
* Summarization quality depends on the content length and clarity of the source.
* This app does not store or share any user data.
