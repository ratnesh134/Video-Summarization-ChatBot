import streamlit as st
from src.agents.chat_agent import get_groq_response

def display_chat_history():
    """Displays all messages from st.session_state."""
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

def chat_input_logic():
    """Handles user chat input and generates a response."""
    if prompt := st.chat_input("Ask a question about the video summary..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        with st.chat_message("user"):
            st.markdown(prompt)

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
        
        st.session_state.messages.append({"role": "assistant", "content": response})