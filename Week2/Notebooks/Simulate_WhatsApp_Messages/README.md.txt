# 📩 Supabase WhatsApp Chat Logger (Simulation)

This project demonstrates how to log and retrieve WhatsApp-style conversations using **Supabase** as the backend and Python `requests` for API interaction.  

It simulates sending and receiving messages, storing them in a Supabase `messages` table, and retrieving the full chat history.

---

## 🚀 Features
- Store chat messages (sent or received) in Supabase.
- Retrieve all messages for a specific phone number in chronological order.
- Simple Python script using `requests`.
- Environment variables used for security (`SUPABASE_URL` and `SUPABASE_KEY`).

---
[SENT] Hello, this is Salma 👋
[RECEIVED] Hey Salma, got your message ✅
[SENT] Great! Let’s meet tomorrow.

--- Chat with +201234567890 ---
2025-09-04T13:30:01Z | SENT: Hello, this is Salma 👋
2025-09-04T13:30:05Z | RECEIVED: Hey Salma, got your message ✅
2025-09-04T13:30:10Z | SENT: Great! Let’s meet tomorrow.
