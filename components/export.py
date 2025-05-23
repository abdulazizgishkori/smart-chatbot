import streamlit as st
from reportlab.pdfgen import canvas
import io

def export_data(messages):
    if st.sidebar.button("Export as TXT"):
        txt = "\n".join([f"{s}: {m}" for s, m in messages])
        st.download_button("Download TXT", txt, "chat.txt")

    if st.sidebar.button("Export as Markdown"):
        md = "\n\n".join([f"**{s}**: {m}" for s, m in messages])
        st.download_button("Download MD", md, "chat.md")

    if st.sidebar.button("Export as PDF"):
        buffer = io.BytesIO()
        c = canvas.Canvas(buffer)
        y = 800
        for sender, msg in messages:
            c.drawString(50, y, f"{sender}: {msg}")
            y -= 20
        c.save()
        st.download_button("Download PDF", buffer.getvalue(), "chat.pdf")
