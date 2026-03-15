# YouTube RAG Assistant

A simple **Retrieval-Augmented Generation (RAG)** application that allows users to ask questions about a **YouTube video** and receive answers grounded in the video's transcript.

The system extracts the transcript, converts it into embeddings, retrieves the most relevant sections using vector search, and generates an answer using a Large Language Model.

The interface is built using **Streamlit** for quick interaction.

---

## Demo

Run the application locally and open:

```
http://localhost:8501
```

Workflow:

1. Paste a YouTube video URL  
2. Enter a question about the video  
3. The system retrieves relevant transcript sections and generates an answer  

---

## Architecture

The system follows a basic **Retrieval-Augmented Generation pipeline**.

```
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
```

---

## Tech Stack

- **LangChain** – RAG pipeline orchestration  
- **HuggingFace Models** – LLM and embeddings  
- **FAISS** – vector similarity search  
- **Streamlit** – user interface  
- **youtube-transcript-api** – transcript extraction  

---

## Project Structure

```
YoutubeChat
│
├── app.py            # Streamlit UI
├── rag_pipeline.py   # RAG pipeline
├── youtube_utils.py  # YouTube transcript extraction
├── config.py         # Configuration parameters
├── requirements.txt
└── README.md
```

---

## Running the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/ShankarOmmi/RAG.git
cd YoutubeChat
```

---

### 2. Create virtual environment

```bash
python -m venv .venv
```

Activate environment

**Windows**

```bash
.venv\Scripts\activate
```

**Mac/Linux**

```bash
source .venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Add HuggingFace API Key

Create a `.env` file:

```
HUGGINGFACEHUB_API_TOKEN=your_token_here
```

Make sure `.env` is included in `.gitignore`.

---

### 5. Run the application

```bash
streamlit run app.py
```

---

## Possible Improvements

This project implements a **basic RAG system** and can be extended using more advanced techniques.

### Evaluation
- Ragas
- LangSmith

### Indexing
- Better document ingestion
- Semantic text splitting
- Scalable vector databases (Pinecone, Weaviate)

### Retrieval

**Pre-Retrieval**
- Query rewriting
- Multi-query generation
- Domain-aware routing

**During Retrieval**
- MMR (Maximum Marginal Relevance)
- Hybrid retrieval
- Reranking

**Post-Retrieval**
- Contextual compression

### Augmentation
- Improved prompt templating
- Context window optimization
- Answer grounding

### Generation
- Answers with citations
- Guardrails to reduce hallucination

### System Design
- Multimodal support
- Agent-based workflows
- Conversation memory

---

## Learning Goals

This project demonstrates the fundamentals of building **LLM applications using Retrieval-Augmented Generation**, including:

- document chunking  
- embeddings  
- vector search  
- retrieval pipelines  
- prompt engineering  
- LLM integration  

---

## License

This project is intended for **educational and learning purposes**.
