import streamlit as st
from groq import Groq

# NOTE: Client is configured in app.py
def get_groq_response(system_prompt: str, chat_history: list, user_question: str) -> str:
    """Gets a response from Llama 3.3 70B via Groq API."""
    try:
        groq_client = st.session_state.groq_client # Assuming you store client in session state
        messages = [{"role": "system", "content": system_prompt}]
        for message in chat_history:
            messages.append({"role": message["role"], "content": message["content"]})
        messages.append({"role": "user", "content": user_question})

        response = groq_client.chat.completions.create(
            messages=messages,
            model="llama-3.3-70b-versatile",
            temperature=0.7,
            max_tokens=4096,
        )
        return response.choices[0].message.content
    except Exception as e:
        st.error(f"Error calling Groq API: {e}")
        return "Sorry, I am unable to connect to the Groq API at the moment. Please try again later."