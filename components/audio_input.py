import streamlit as st
from gtts import gTTS
from pydub import AudioSegment

def audio_input():
    audio = st.sidebar.file_uploader("🎤 Upload Audio", type=["mp3", "wav"])
    if audio:
        st.audio(audio)
        st.info("Audio input support placeholder. You can integrate Whisper or similar.")
