# 📘 SOP – Deploying Telegram AI Assistant with Supabase & FastAPI

### 🎯 Objective
Set up a Telegram AI assistant that:
- Receives user messages via Telegram webhook
- Logs messages in Supabase (`conversationmemory` table)
- Sends AI-generated replies via OpenRouter LLM
- Exposes FastAPI server with Ngrok

---

## 1️⃣ Prerequisites
- Python 3.10+
- Google Colab / Local environment
- Installed packages:
  ```bash
  pip install fastapi uvicorn requests supabase python-telegram-bot python-dotenv pyngrok nest_asyncio
  ```
- Telegram Bot Token (from [BotFather](https://t.me/BotFather))
- Supabase project (with table `conversationmemory`)
- OpenRouter API Key ([https://openrouter.ai](https://openrouter.ai))
- (Optional) Ngrok auth token

---

## 2️⃣ Environment Setup

1. **Create secrets file** `/content/secrets.env`:
   ```python
   from getpass import getpass

   TELEGRAM_TOKEN = getpass("TELEGRAM_TOKEN: ")
   SUPABASE_URL = getpass("SUPABASE_URL (https://...): ")
   SUPABASE_KEY = getpass("SUPABASE_KEY: ")
   OPENROUTER_KEY = getpass("OPENROUTER_KEY: ")
   NGROK_AUTH = getpass("NGROK_AUTH_TOKEN (optional, press enter to skip): ")

   with open('/content/secrets.env','w') as f:
       f.write(f"TELEGRAM_TOKEN={TELEGRAM_TOKEN}\n")
       f.write(f"SUPABASE_URL={SUPABASE_URL}\n")
       f.write(f"SUPABASE_KEY={SUPABASE_KEY}\n")
       f.write(f"OPENROUTER_KEY={OPENROUTER_KEY}\n")
       if NGROK_AUTH:
           f.write(f"NGROK_AUTH={NGROK_AUTH}\n")
   ```

✅ Output: `✅ Saved secrets to /content/secrets.env`

---

## 3️⃣ FastAPI Application

- **Core logic** in `/content/main.py`:
  - Load secrets from `.env`
  - Handle `/webhook` route (Telegram → FastAPI)
  - Save messages to Supabase
  - Fetch conversation history
  - Send prompt to OpenRouter LLM
  - Save AI response in Supabase
  - Reply back to Telegram

---

## 4️⃣ Run FastAPI with Ngrok

```python
from pyngrok import ngrok
import os, time
from dotenv import load_dotenv

load_dotenv('/content/secrets.env')
NGROK_AUTH = os.getenv('NGROK_AUTH')

if NGROK_AUTH:
    ngrok.set_auth_token(NGROK_AUTH)

public_url = ngrok.connect(8000)
print("🌍 Public URL:", public_url)

get_ipython().system_raw("uvicorn main:app --host 0.0.0.0 --port 8000 > /content/uvicorn.log 2>&1 &")
time.sleep(2)
!tail -n 10 /content/uvicorn.log
```

✅ Output: `🌍 Public URL: https://xxxx.ngrok-free.app`

---

## 5️⃣ Configure Telegram Webhook

```python
import requests, os
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
NGROK_URL = "<your-public-ngrok-url>"

url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/setWebhook"
resp = requests.get(url, params={"url": f"{NGROK_URL}/webhook"})
print(resp.json())
```

✅ Output: `{ "ok": true, "result": true, "description": "Webhook was set" }`

---

## 6️⃣ Testing

1. Send a message to your bot in Telegram.
2. Check logs:
   ```bash
   !tail -n 50 /content/uvicorn.log
   ```
3. Verify in Supabase `conversationmemory` table.

---

## 7️⃣ Shutdown

```bash
!pkill -f ngrok
!pkill -f uvicorn
```

---

## 8️⃣ Troubleshooting

- ❌ **Insert error in Supabase** → Check table name & columns.
- ❌ **LLM timeout** → Switch to another OpenRouter free model.
- ❌ **No reply in Telegram** → Confirm webhook URL matches Ngrok URL.
