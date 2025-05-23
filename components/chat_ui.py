import streamlit as st

def chat_ui(messages):
    for sender, msg in messages:
        if sender == "user":
            st.chat_message("User").markdown(f"🧑‍💻: {msg}")
        else:
            st.chat_message("Assistant").markdown(f"🤖: {msg}")
