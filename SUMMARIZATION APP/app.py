import streamlit as st
import validators
import warnings
from langchain.prompts import PromptTemplate
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import YoutubeLoader, UnstructuredURLLoader
from langchain_groq import ChatGroq

warnings.filterwarnings("ignore")

# Streamlit UI Setup
st.set_page_config(page_title="LangChain Summarizer For YouTube & Websites", page_icon="🦜")
st.title("🦜LangChain: Summarize Any Website or YouTube Video")
st.subheader("Enter Website URL or YT URL to summarize the content")

# Sidebar for API Key
with st.sidebar:
    groq_api_key = st.text_input("🔑 Groq API Key", type="password")

# URL Input
url_input = st.text_input("Paste URL Here")

# Prompt Template
prompt_template = """
Provide simple understandable summary in around 300 words for the following content:
Content: {text}
"""
prompt = PromptTemplate(template=prompt_template, input_variables=["text"])

# Button Action
if st.button("Summarize Content"):

    # Input Validation
    if not groq_api_key.strip():
        st.error("🚨 Please enter your Groq API Key.")
    elif not url_input.strip():
        st.error("🚨 Please paste a URL.")
    elif not validators.url(url_input):
        st.error("❌ Invalid URL format. Please enter a valid YouTube or website URL.")
    else:
        try:
            st.info("📥 Loading content...")

            # Initialize LLM
            llm = ChatGroq(model="gemma2-9b-it", groq_api_key=groq_api_key)  # fallback to "gemma-7b-it" if needed

            # Load Documents
            if "youtube.com" in url_input or "youtu.be" in url_input:
                loader = YoutubeLoader.from_youtube_url(url_input, add_video_info=False)
            else:
                loader = UnstructuredURLLoader(
                    urls=[url_input],
                    ssl_verify=False,
                    headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}
                )

            docs = loader.load()

            # Load summarization chain
            chain = load_summarize_chain(llm, chain_type="stuff", prompt=prompt)

            # Generate Summary
            with st.spinner("⏳ Generating summary..."):
                summary = chain.run(docs)

            st.success("✅ Summary Generated:")
            st.write(summary)

        except Exception as e:
            st.error(f"An error occurred: {e}")