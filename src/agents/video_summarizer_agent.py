import streamlit as st
import google.generativeai as genai
import time

# NOTE: API key is configured in app.py
def summarize_video(video_path: str) -> str:
    """Summarizes a video using the Gemini 1.5 Flash model."""
    st.info("Starting video summarization. This may take a few minutes...")
    try:
        video_file = genai.upload_file(path=video_path)
        
        status_placeholder = st.empty()
        while video_file.state.name == "PROCESSING":
            status_placeholder.info("Waiting for video processing...")
            time.sleep(10)
            video_file = genai.get_file(video_file.name)
        
        status_placeholder.empty()

        if video_file.state.name == "FAILED":
            return f"Error: Video processing failed. State: {video_file.state.name}"

        model = genai.GenerativeModel(model_name="gemini-1.5-flash")
        
        prompt = """
            You are a highly detailed visual understanding and forensic analysis agent. Your task is to provide a minute-by-minute, comprehensive log of all events and objects present in the video.

            Follow these instructions precisely:
            1.  **Detailed Object and Person Tracking**: For every distinct object and person that appears in the video, note its entry timestamp, exit timestamp, and a brief description of its appearance.
                * **Format**: 'Object ID: [ID], Appearance: [Description], Enters: [timestamp], Exits: [timestamp].'
                
            2.  **Event Analysis**: Log every significant event or interaction that occurs, no matter how small. For each event, provide a timestamp and a detailed description.
                * **Format**: 'At [timestamp], [Detailed event description].'
                
            3.  **Action and Violation Identification**: Identify all actions, movements, and interactions, noting any potential guideline violations, safety concerns, or unusual behavior.
                * **Format**: 'At [timestamp], [Action or behavior]. Potential issue: [Violation or concern type].'
                
            4.  **Scene and Environment Description**: Provide a thorough description of the video's setting and changes in the environment over time. This includes weather, time of day, lighting, and any notable features of the location.
                
            5.  **Final Comprehensive Summary**: Conclude with a detailed, narrative summary of the entire video, combining all the logged information into a cohesive and chronological report.

            Your final output should be structured as a comprehensive report, not just a simple list. Break it down into clear sections for **Object Tracking**, **Event Log**, **Scene Description**, and **Final Summary**.
        """

        response = model.generate_content([video_file, prompt])
        return response.text

    except Exception as e:
        st.error(f"An error occurred during video summarization: {str(e)}")
        return f"An error occurred: {str(e)}"