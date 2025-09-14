# WhatsApp/Telegram AI Assistant (IWAA)

This project implements a lightweight AI assistant for Telegram (and WhatsApp via Telegram integration) using **FastAPI**, **Supabase**, **OpenRouter LLM**, and **ngrok**. It logs user messages, retrieves conversation context, caches AI responses, and replies intelligently.

---

## Features

- Receives user messages via Telegram webhook.
- Stores conversation history in **Supabase** (`conversationmemory` table).
- Retrieves last 5 messages for context.
- Checks **cache** (`reply_logs`) before calling the LLM to save costs and reduce latency.
- Calls **OpenRouter LLM** to generate AI responses.
- Sends replies back to Telegram.
- Uses **ngrok** to expose FastAPI webhook for testing.

---

## Requirements

```bash
pip install fastapi uvicorn requests supabase python-telegram-bot python-dotenv pyngrok nest_asyncio
