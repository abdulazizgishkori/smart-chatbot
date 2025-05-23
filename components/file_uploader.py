import streamlit as st
import fitz  # PyMuPDF

def handle_file_upload():
    file = st.sidebar.file_uploader("📄 Upload PDF/Doc", type=["pdf"])
    if file:
        text = ""
        with fitz.open(stream=file.read(), filetype="pdf") as doc:
            for page in doc:
                text += page.get_text()
        st.session_state.messages.append(("bot", f"Document uploaded. Content preview:\n{text[:300]}..."))
