import os
import streamlit as st
import google.generativeai as genai
import tempfile
import time
from groq import Groq


# --- Configuration ---
# Configure API keys from Streamlit secrets
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    groq_client = Groq(api_key=st.secrets["GROQ_API_KEY"])
    GROQ_MODEL = "llama-3.3-70b-versatile"
except KeyError as e:
    st.error(f"API key not found for {e}. Please check `secrets.toml`.")
    st.stop()

# --- Functions for Agents ---

@st.cache_data
def summarize_video(video_path: str) -> str:
    """Summarizes a video using the Gemini 1.5 Flash model."""
    st.info("Starting video summarization. This may take a few minutes...")
    try:
        # Upload the video file
        video_file = genai.upload_file(path=video_path)

        # Wait for processing to complete
        status_placeholder = st.empty()
        while video_file.state.name == "PROCESSING":
            status_placeholder.info("Waiting for video processing...")
            time.sleep(10)
            video_file = genai.get_file(video_file.name)
        
        status_placeholder.empty()

        if video_file.state.name == "FAILED":
            return f"Error: Video processing failed. State: {video_file.state.name}"

        model = genai.GenerativeModel(model_name="gemini-1.5-flash")
        
        # Craft a specific prompt for detailed summarization and event recognition
        prompt = (
        '''
            "You are a highly detailed visual understanding and forensic analysis agent. Your task is to provide a minute-by-minute, comprehensive log of all events and objects present in the video.

            Follow these instructions precisely:

        1.  **Detailed Object and Person Tracking**: For every distinct object and person that appears in the video, note its entry timestamp, exit timestamp, and a brief description of its appearance.
            * **Format**: 'Object ID: [ID], Appearance: [Description], Enters: [timestamp], Exits: [timestamp].'
            * **Example**: 'Object ID: Car_01, Appearance: Red sedan with a dent on the passenger side, Enters: 00:03, Exits: 01:15.'

        2.  **Event Analysis**: Log every significant event or interaction that occurs, no matter how small. For each event, provide a timestamp and a detailed description.
            * **Format**: 'At [timestamp], [Detailed event description].'
            * **Example**: 'At 00:12, a pedestrian with a blue jacket and a backpack crosses the street, looking at their phone and not at the traffic lights.'

        3.  **Action and Violation Identification**: Identify all actions, movements, and interactions, noting any potential guideline violations, safety concerns, or unusual behavior.
            * **Format**: 'At [timestamp], [Action or behavior]. Potential issue: [Violation or concern type].'
            * **Example**: 'At 00:45, the red sedan (Car_01) accelerates through the intersection while the traffic light is yellow. Potential issue: Exceeding speed limit / Running a yellow light.'

        4.  **Scene and Environment Description**: Provide a thorough description of the video's setting and changes in the environment over time. This includes weather, time of day, lighting, and any notable features of the location.
            * **Example**: 'The video begins on a sunny afternoon in a suburban intersection. The road is dry. At 01:30, a large cloud passes over, slightly dimming the light.'

        5.  **Final Comprehensive Summary**: Conclude with a detailed, narrative summary of the entire video, combining all the logged information into a cohesive and chronological report.

        Your final output should be structured as a comprehensive report, not just a simple list. Break it down into clear sections for **Object Tracking**, **Event Log**, **Scene Description**, and **Final Summary**."
        '''
        )

        response = model.generate_content([video_file, prompt])
        return response.text

    except Exception as e:
        st.error(f"An error occurred during video summarization: {str(e)}")
        return f"An error occurred: {str(e)}"

def get_groq_response(system_prompt: str, chat_history: list, user_question: str) -> str:
    """Gets a response from Llama 3.1 70B via Groq API."""
    messages = [
        {"role": "system", "content": system_prompt}
    ]
    # Add chat history
    for message in chat_history:
        messages.append({"role": message["role"], "content": message["content"]})
    # Add the current user question
    messages.append({"role": "user", "content": user_question})

    try:
        response = groq_client.chat.completions.create(
            messages=messages,
            model=GROQ_MODEL,
            temperature=0.7,
            max_tokens=4096,
        )
        return response.choices[0].message.content
    except Exception as e:
        st.error(f"Error calling Groq API: {e}")
        return "Sorry, I am unable to connect to the Groq API at the moment. Please try again later."


# --- Streamlit UI Components and Logic ---
st.set_page_config(
    page_title="Visual Understanding Agentic Chat Assistant",
    layout="wide"
)

st.title("🎬 Visual Understanding Agentic Chat Assistant")
st.markdown("Upload a video (max 2 minutes) and ask questions about its content.")

# --- File Uploader and Summarization Logic ---
uploaded_file = st.file_uploader(
    "Choose a video file...",
    type=["mp4", "mov"],
    accept_multiple_files=False,
    help="Maximum video duration is 2 minutes."
)

if uploaded_file is not None:
    # Use a temporary file to save the uploaded video
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_file:
        temp_file.write(uploaded_file.read())
        video_path = temp_file.name

    # Check if a new video has been uploaded
    if "video_path" not in st.session_state or st.session_state.video_path != video_path:
        st.session_state.video_path = video_path
        # Reset everything for a new video
        st.session_state.video_summary = None
        st.session_state.messages = []
        
        # Display the video
        st.video(video_path)

        # Trigger summarization
        with st.spinner("Analyzing and summarizing the video..."):
            st.session_state.video_summary = summarize_video(video_path)
            
        # Display the generated summary
        st.subheader("Video Summary")
        st.markdown(st.session_state.video_summary)

        st.success("Video analysis complete! You can now ask questions.")

    # --- Chat Interface Logic ---
    st.subheader("Chat with the Assistant")

    # Initialize chat history if not present
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input("Ask a question about the video summary..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)

        # Get Groq response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                system_prompt = (
                    "You are a helpful and detailed assistant. You have been provided with a summary of a video. "
                    "Your task is to answer user questions based on the video summary and the ongoing chat history. "
                    "Do not make up information that is not in the summary. If the information isn't available, state that. "
                    f"Video Summary:\n{st.session_state.video_summary}"
                )
                
                response = get_groq_response(
                    system_prompt=system_prompt,
                    chat_history=st.session_state.messages,
                    user_question=prompt
                )
                
                st.markdown(response)
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})

else:
    # Initial state when no video is uploaded
    if "video_path" in st.session_state:
        del st.session_state.video_path
        if "video_summary" in st.session_state:
            del st.session_state.video_summary
        if "messages" in st.session_state:
            del st.session_state.messages

    st.info("Please upload a video to begin.")