# iTech WhatsApp Lite Assistant

## Overview
This project implements a WhatsApp Lite AI Assistant using FastAPI, Supabase, Telegram Bot API, and OpenRouter LLM. It demonstrates a sandbox-to-production workflow for AI-powered messaging and data logging.

The assistant can:  
- Receive messages from Telegram users  
- Store messages in Supabase (`conversationmemory` table)  
- Retrieve conversation context (last 5 messages)  
- Generate intelligent replies using OpenRouter LLM  
- Send replies back to the user via Telegram  

## Features
- **Conversation Memory:** Stores all user interactions in Supabase for context and future analysis.  
- **Context-Aware Responses:** Uses the last 5 messages to generate relevant AI replies.  
- **AI Integration:** Uses OpenRouter LLM to provide intelligent answers.  
- **Telegram Webhook:** FastAPI app receives messages via webhook.  
- **Public Access:** Uses Ngrok to expose a local FastAPI server to the web.
  
 ## Workflow

User sends a message to the Telegram bot.

FastAPI webhook receives the message.

Message is saved in Supabase conversationmemory.

The last 5 messages are retrieved for context.

A prompt is built and sent to OpenRouter LLM.

AI reply is stored in Supabase and sent to the user via Telegram.

## Setup

### 1. Install Dependencies
```bash
!pip install fastapi uvicorn requests supabase python-telegram-bot python-dotenv pyngrok nest_asyncio
!pip install supabase

