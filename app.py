import streamlit as st

from components.chat_ui import chat_ui
from components.export import export_data
from components.audio_input import audio_input
from components.file_uploader import handle_file_upload  # FIXED: Removed `.py` from import

from services.ollama_integration import get_response
from services.multilingual import translate_input, translate_output

# Page config
st.set_page_config(page_title="AI Chatbot", layout="wide")

# Load custom CSS
with open('./assets/styles.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("🤖 AI Chatbot")

# Language selection
lang = st.selectbox("Select Language", ["en", "es", "fr", "hi", "zh"])

# Audio + text input
audio_input()
user_input = st.chat_input("Type your message or record audio...")

if user_input:
    translated_input = translate_input(user_input, lang)
    response = get_response(translated_input)
    final_response = translate_output(response, lang)

    st.session_state.messages.append(("user", user_input))
    st.session_state.messages.append(("bot", final_response))

# Chat UI display
chat_ui(st.session_state.messages)

# File upload + Q&A
handle_file_upload()

# Export chat
export_data(st.session_state.messages)

# Theme toggle
st.sidebar.toggle("Dark Mode 🌙")
