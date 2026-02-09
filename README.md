# 📚 DocuMind API — PDF RAG Backend (FastAPI + AI)

## 🚀 Project Overview
DocuMind API adalah backend service berbasis **FastAPI + AI (RAG - Retrieval Augmented Generation)** yang memungkinkan user:

- Upload dokumen PDF
- Menyimpan knowledge dokumen ke vector database
- Melakukan query berbasis isi dokumen
- Mendapat jawaban berdasarkan context PDF yang tersimpan

Project ini dirancang sebagai portfolio backend + AI system dengan fokus pada:
- Clean architecture
- Scalable storage design
- Local AI inference (optional cloud model)

---

## 🧠 Core Concept — RAG (Retrieval Augmented Generation)

Alur RAG:

1. Document diubah menjadi text
2. Text dipecah menjadi chunk kecil
3. Chunk diubah menjadi embedding vector
4. Vector disimpan di vector database
5. Saat user bertanya → sistem mencari chunk paling relevan
6. Chunk digunakan sebagai context untuk generate jawaban

---

## 🛠 Tech Stack

### 🔹 Backend
- FastAPI
- Uvicorn
- Pydantic v2
- Python 3.10+

### 🔹 AI / Machine Learning
- Sentence Transformers (Embedding Model)
- Transformers
- PyTorch
- Scikit-learn

### 🔹 Vector Database
- ChromaDB (Local Persistent Vector Store)

### 🔹 Document Processing
- PyPDF (PDF Text Extraction)

### 🔹 Supporting Tools
- Python Dotenv (Environment Config)
- HTTPX (Async HTTP Client)

---

## 📂 Project Structure

