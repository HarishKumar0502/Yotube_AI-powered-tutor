```markdown
#  YouTube AI-Powered Tutor

An AI-powered application that allows users to learn from YouTube videos by automatically extracting transcripts and answering questions about the video content using Retrieval-Augmented Generation (RAG) and Large Language Models (LLMs).

## ✨ Features

- 📺 Extract transcripts from YouTube videos
- 🤖 Ask questions about the video
- 🧠 AI-generated answers based on transcript content
- ⚡ Fast retrieval using vector embeddings
- 💬 Interactive Streamlit web interface
- 🔒 Secure API key management using `.env`

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **LangChain**
- **Groq API**
- **FAISS**
- **HuggingFace Embeddings**
- **YouTube Transcript API**
- **python-dotenv**

## 📁 Project Structure

```

youtube_transcripter/
│
├── app.py                 # Main Streamlit application
├── transcript.txt         # Extracted transcript (generated)
├── requirements.txt       # Python dependencies
├── .env                   # API keys (not committed)
├── .gitignore
└── README.md

````

## 🚀 Installation

### 1. Clone the repository

```bash
git clone git@github-personal:HarishKumar0502/Yotube_AI-powered-tutor.git
cd Yotube_AI-powered-tutor
````

### 2. Create a virtual environment

Windows:

```bash
python -m venv venv310
venv310\Scripts\activate
```

Linux / macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 🔑 Environment Variables

Create a `.env` file in the project root.

Example:

```env
GROQ_API_KEY=your_groq_api_key
```

> Never commit your `.env` file to GitHub.

## ▶️ Run the Application

```bash
streamlit run app.py
```

## 📖 How It Works

1. Enter a YouTube video URL.
2. The application extracts the video's transcript.
3. The transcript is converted into vector embeddings.
4. Relevant transcript chunks are retrieved for each user question.
5. The Groq LLM generates an accurate answer based on the retrieved context.

## 📌 Future Improvements

* Multi-language transcript support
* Chat history
* PDF notes generation
* Voice-based questions
* Transcript summarization
* Support for longer videos
* Multiple LLM provider options

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push to your branch.
5. Open a Pull Request.

## 📄 License

This project is licensed under the MIT License.

---

### 👨‍💻 Author

**Harish Kumar**

GitHub: https://github.com/HarishKumar0502

```
```
