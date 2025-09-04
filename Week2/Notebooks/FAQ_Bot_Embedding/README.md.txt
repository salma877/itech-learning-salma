# 🤖 iTech FAQ Bot – Supabase + Embeddings + n8n

This project implements a **FAQ chatbot** for iTech Solutions using:
- **Supabase** for database + RPC functions
- **Sentence Transformers** for embeddings
- **Keyword search** (for n8n compatibility)
- **Python** testing and integration demos

It provides both **semantic search (vector embeddings)** and **keyword-based search**, with easy integration into **n8n workflows**.

---

## 🚀 Features
- Load a FAQ dataset and store it in Supabase.
- Generate vector embeddings for semantic similarity search.
- Support keyword-based fallback queries.
- Compare performance of embeddings vs keywords.
- Simulate **n8n webhook integration**.
- Direct Supabase API testing included.

---
Example Outputs

Embedding-based search
🤔 Question: What services does iTech offer?
📊 EMBEDDING-BASED RESULTS:
   1. [97.5%] We deliver innovative technology and AI-driven solutions, including cloud migration...

Keyword-based search
🔍 KEYWORD-BASED RESULTS (N8N Compatible):
   1. [Score: 0.88] We deliver innovative technology and AI-driven solutions, including cloud migration...

