import streamlit as st
import os
from groq import Groq

from src.agents.video_summarizer_agent import summarize_video
from src.agents.chat_agent import get_groq_response
from src.ui.components import display_chat_history, chat_input_logic

# --- 1. Main Page Configuration ---
st.set_page_config(
    page_title="Visual Understanding Agentic Chat Assistant",
    layout="wide"
)
st.title("🎬 Visual Understanding Agentic Chat Assistant")
st.markdown("Upload a video (max 2 minutes) and ask questions about its content.")

# --- API KEY & CLIENT INITIALIZATION ---
# This block is moved to the top to ensure Groq client is ready before any functions are called.
try:
    if "groq_client" not in st.session_state:
        groq_client = Groq(api_key=st.secrets["GROQ_API_KEY"])
        st.session_state.groq_client = groq_client
except KeyError as e:
    st.error(f"API key not found for {e}. Please check `secrets.toml`.")
    st.stop()

# --- 2. Video Upload and Summarization ---
uploaded_file = st.file_uploader(
    "Choose a video file...",
    type=["mp4", "mov"],
    accept_multiple_files=False,
    help="Maximum video duration is 2 minutes."
)

if uploaded_file:
    UPLOAD_FOLDER = "uploaded_videos"
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    video_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
    
    with open(video_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    if "video_path" not in st.session_state or st.session_state.video_path != video_path:
        st.session_state.video_path = video_path
        st.session_state.video_summary = None
        st.session_state.messages = []
        
        st.video(video_path)

        with st.spinner("Analyzing and summarizing the video..."):
            st.session_state.video_summary = summarize_video(video_path)
        
        st.success("Video analysis complete!")
    
    # --- 3. Display Video, Summary, and Download Button ---
    if "video_summary" in st.session_state and st.session_state.video_summary:
        st.video(st.session_state.video_path)
        st.subheader("Video Summary")
        st.markdown(st.session_state.video_summary)
        
        st.download_button(
            label="Download Summary",
            data=st.session_state.video_summary,
            file_name="video_summary.txt",
            mime="text/plain"
        )
        
    # --- 4. Chat Interface ---
    if "video_summary" in st.session_state and st.session_state.video_summary:
        st.subheader("Chat with the Assistant")
        if "messages" not in st.session_state:
            st.session_state.messages = []

        display_chat_history()
        chat_input_logic()

else:
    if "video_path" in st.session_state:
        del st.session_state.video_path
        if "video_summary" in st.session_state:
            del st.session_state.video_summary
        if "messages" in st.session_state:
            del st.session_state.messages

    st.info("Please upload a video to begin.")