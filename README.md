# 🤖 AI RAG Chatbot using Vector Database

## 📌 Overview
This project implements a **Retrieval-Augmented Generation (RAG)** based AI chatbot that answers questions from user-provided documents.

Users can upload a text file, and the system retrieves relevant information from the document and generates accurate answers using a language model.

---

## 🚀 Features
- 📂 Upload `.txt` documents
- 🔍 Semantic search using embeddings
- 🧠 Context-aware AI responses (RAG)
- 💬 Chat-style interaction with history
- ⚡ Fast vector similarity search using FAISS
- 🧩 Modular architecture for easy extension

---

## 🧠 What is RAG?

Retrieval-Augmented Generation (RAG) combines:

- **Retrieval** → Finding relevant data from a database  
- **Generation** → Producing answers using an LLM  

### 🔄 Flow in this project:
User Query → Embedding → Vector DB → Retrieval → Context → LLM → Answer

---

## 🏗️ System Architecture

### Step-by-step pipeline:

1. **Document Upload**
2. **Text Chunking**
3. **Embedding Generation**
4. **Vector Storage (FAISS)**
5. **Query Processing**
6. **Retrieval (RAG Core)**
7. **Context Building**
8. **Answer Generation**

---

## 🧠 About Endee Integration

This project follows the architecture of the **Endee Vector Database**.

- FAISS is used as a local vector store  
- Designed for seamless integration with Endee  

### In production, Endee would:
- Replace FAISS  
- Provide scalable vector search  
- Enable real-time semantic retrieval  

---

## ⚙️ Tech Stack

| Component | Technology |
|----------|----------|
| Language Model | HuggingFace (flan-t5-base) |
| Embeddings | sentence-transformers |
| Vector DB | FAISS |
| Framework | LangChain |
| UI | Streamlit |

---

## ⚙️ Installation

```bash
git clone https://github.com/IzherBajeed/rag-chatbot.git
cd rag-chatbot
pip install -r requirements.txt