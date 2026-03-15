# YouTube RAG Assistant

A simple **Retrieval-Augmented Generation (RAG)** application that allows users to ask questions about a **YouTube video** and receive answers grounded in the video's transcript.

The system extracts the transcript, converts it into embeddings, retrieves the most relevant sections using vector search, and generates an answer using a Large Language Model.

The interface is built using **Streamlit** for quick interaction.

---

## Demo

Run the application locally and open:

http://localhost:8501


Workflow:

1. Paste a YouTube video URL  
2. Enter a question about the video  
3. The system retrieves relevant transcript sections and generates an answer  

---

## Architecture

The system follows a basic **Retrieval-Augmented Generation pipeline**.

YouTube URL
│
▼
Transcript Extraction
│
▼
Text Chunking
│
▼
Embeddings (Sentence Transformers)
│
▼
Vector Store (FAISS)
│
▼
Retriever
│
▼
Prompt Template
│
▼
LLM (HuggingFace)
│
▼
Answer


---

## Tech Stack

- **LangChain** – RAG pipeline orchestration  
- **HuggingFace Models** – LLM and embeddings  
- **FAISS** – vector similarity search  
- **Streamlit** – user interface  
- **youtube-transcript-api** – transcript extraction  

---

## Project Structure

YoutubeChat
│
├── app.py # Streamlit UI
├── rag_pipeline.py # RAG pipeline
├── youtube_utils.py # YouTube transcript extraction
├── config.py # Configuration parameters
├── requirements.txt
└── README.md



---

## Running the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YoutubeChat


2. Create virtual environment
