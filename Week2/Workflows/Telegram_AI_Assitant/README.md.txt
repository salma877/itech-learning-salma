# 🤖 Telegram AI Assistant with Memory (Supabase)

This project is an **AI-powered Telegram assistant** built with **n8n**, **OpenRouter AI**, and **Supabase**.  
The bot can **chat naturally with users**, **remember important facts**, and **use past conversations** to provide more personalized responses.

---

## 📌 Workflow Overview

1. **Receive User Message (Telegram Trigger)**
   - Listens for incoming Telegram messages from users.
   - Captures message text, sender ID, and chat ID.

2. **Fetch User Memories (Supabase)**
   - Queries the `ConversationMemory` table in Supabase.
   - Retrieves previously saved facts for the specific user (`sender`).

3. **Format Memories (Aggregate Node)**
   - Aggregates stored facts + timestamps into a structured list.
   - Passes this context to the AI agent.

4. **AI Memory Agent (LangChain Agent)**
   - Powered by **OpenRouter model**: `glm-4.5-air:free`.
   - Instructions:
     - Talk naturally as a **friendly AI assistant**.
     - Detect if the user shares **important facts** (e.g., name, preferences, plans).
     - Save those facts silently using the **Save Memory** tool.
     - Use previously stored facts when replying (avoid asking again).

5. **SaveMemory (Supabase)**
   - Stores important facts detected by the AI in the `ConversationMemory` table.
   - Fields saved:
     - `message` (the fact summary)
     - `sender` (Telegram user ID)
     - `recipient` (Telegram chat ID)

6. **Send Reply to Telegram**
   - Sends the AI’s response back to the user on Telegram.
   - Replies are **context-aware** using memory.

---

## 📊 Data Flow

**Telegram → n8n → Supabase (memory) → AI Agent → Telegram**

---

## 🛠️ Tech Stack

- **n8n** – Workflow automation
- **Telegram Bot API** – Messaging platform
- **OpenRouter AI (`glm-4.5-air:free`)** – Conversational intelligence
- **Supabase** – Persistent memory storage (`ConversationMemory` table)

---

## ✅ Benefits

- **Contextual AI Conversations** – Remembers past user details
- **Memory Persistence** – Stored in Supabase for long-term use
- **Personalized Responses** – Uses facts from history to reply
- **Scalable** – Can be extended with more tools or integrations

---




## 📂 Database Schema

Table: **ConversationMemory**

| Column     | Type     | Description                        |
|------------|----------|------------------------------------|
| id         | UUID/INT | Primary key                        |
| message    | TEXT     | Fact or memory stored              |
| sender     | TEXT     | Telegram user ID                   |
| recipient  | TEXT     | Telegram chat ID                   |
| created_at | TIMESTAMP| Auto-generated timestamp           |

---

🚀 With this setup, your **Telegram bot becomes a smart AI assistant** that not only chats but also **remembers users like a real friend**.
