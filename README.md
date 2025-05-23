# 🤖 Smart Chatbot using Streamlit + Local AI

A powerful, privacy-friendly AI chatbot built with [Streamlit](https://streamlit.io) and local LLMs using [Ollama](https://ollama.com). It supports markdown formatting, emoji reactions, multilingual conversation, PDF Q&A, and much more — all running locally on your machine!

---

## 🚀 Features

- 💬 Chat with a local LLM (via Ollama)
- 📝 Supports Markdown formatting & emoji reactions
- 🌐 Multilingual conversations
- 🔒 Optional authentication (Streamlit Auth or Firebase)
- 🎤 Audio chat support (TTS + STT)
- 📄 PDF, TXT & Markdown Q&A
- 📊 CSV upload and chat
- 🖼️ Image drag-and-drop + captioning
- 🧠 Smart memory (session-aware chat)
- 🌙 Light/Dark mode toggle
- ⬇️ Export chat as `.txt`, `.md`, `.pdf`

---

## 📁 Folder Structure


---

## 🧠 Powered by Local LLM

Uses [Ollama](https://ollama.com) to run local language models like:

- `llama3`
- `mistral`
- `gemma`
- or any custom GGUF/GGML model

You have full control. No external APIs required.

---

## ⚙️ Installation

### 1. Clone the Repo

```bash
git clone https://github.com/abdulazizgishkori/smart-chatbot.git
cd smart-chatbot
# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install Python dependencies
pip install -r requirements.txt
ollama run llama3streamlit run app.py



