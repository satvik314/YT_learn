import streamlit as st
import os
import time
from langchain.document_loaders import YoutubeLoader
from langchain.indexes import VectorstoreIndexCreator
from pytube import YouTube
from dotenv import load_dotenv
import openai

import pysqlite3
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

load_dotenv()
# openai.api_key = os.environ["OPENAI_API_KEY"]
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

def check_video_duration(video_url):
    try:
        # Create a YouTube object with the video URL
        yt = YouTube(video_url)

        # Get the duration of the video in seconds
        duration_seconds = yt.length

        # Convert duration to minutes
        duration_minutes = duration_seconds // 60

        # Check if duration is less than 15 minutes
        if duration_minutes < 15:
            return True
        else:
            return False
        
    except Exception as e:
        print("An error occurred:", e)



st.title("Learn from YouTube 🤖")
st.write("🚀 A GPT-powered tool to help you learn efficiently from YT.")



# Create two columns for the text input and the button
col1, col2 = st.columns([2,1])

# Place the text input in the first column
with col1:
    yt_url = st.text_input("Enter YouTube URL", placeholder= "video length < 15 min")

# Place the Load video button in the second column
with col2:
    st.write("")
    st.write("")
    if st.button("Load video"):
        if check_video_duration(yt_url):
            loader = YoutubeLoader.from_youtube_url(yt_url, add_video_info=False)
            index = VectorstoreIndexCreator().from_loaders([loader])
            st.session_state.index = index
            load_success = st.success("Video loaded!")
            time.sleep(2.3)
            load_success.empty()
        else:
            st.error("Video duration should be less than 15 minutes.")

bcol1 , bcol2, bcol3 = st.columns([1.3,1,1.2])

with bcol1:
    if st.button("What can I learn from this video?"):
        if 'index' in st.session_state:
            st.session_state.response = st.session_state.index.query("What can I learn from this video?")
            # st.write(response, max_width=100)
        else:
            st.write("Please load the video first.")

with bcol2:
    if st.button("Give me a summary"):
        if 'index' in st.session_state:
            st.session_state.response = st.session_state.index.query("Give me the summary of the video.")
            # st.write(response, max_width=100)
        else:
            st.write("Please load the video first.")



with bcol3:
    custom_query = st.text_input("Enter your query", placeholder = "Ask a custom query" ,label_visibility="collapsed")
    if custom_query:
        if 'index' in st.session_state:
            st.session_state.response = st.session_state.index.query(custom_query)
        else:
            st.write("Please load the video first.")


if "response" not in st.session_state:
    st.session_state['response'] = ''

if st.session_state.response:
    st.write(st.session_state.response)


st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")

linkedin_url = "https://www.linkedin.com/in/satvik-paramkusham-76a33610a/"
st.markdown(f"Reach out to me on [LinkedIn]({linkedin_url})")
