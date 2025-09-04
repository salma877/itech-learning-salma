# 🌸 Flower Bloom – Order & FAQ Automation

This workflow automates **order intake, FAQ answering, and data storage** for Flower Bloom using **n8n**, **Google Sheets**, **AI (OpenRouter)**, and **Supabase**.

---

## 📌 Workflow Overview

1. **New Form Response (Trigger)**
   - Triggered whenever a new response is submitted in the Flower Bloom Google Form.
   - Reads customer details from the Google Sheet:  
     [Form Responses Sheet](https://docs.google.com/spreadsheets/d/18sXGKeBPd3jjSOYh5c4zshlvB4megwnLVl1iJ87fcAw).

   **Captured fields:**
   - Full Name  
   - Phone Number  
   - Email  
   - Flower Type  
   - Preferred Delivery Date  
   - Delivery Address  
   - Any Customer Question

---

2. **Answer Customer Question (AI Agent)**
   - Uses a **LangChain Agent** with:
     - **AI Model**: `glm-4.5-air:free` (via OpenRouter)  
     - **FAQ Sheet**: [FAQ Database](https://docs.google.com/spreadsheets/d/1Bi-FYMX34Nmt66E0ohti07nDhdG6VLrbgZg9gWzKWRk)  

   **Logic:**
   - Finds the FAQ question closest in meaning to the customer’s query.
   - If a match is found → responds with the FAQ answer.
   - If no match → responds with:  
     `Thank you 🌸 Our team will follow up.`

---

3. **Save Order + Q&A to Supabase**
   - Stores both the **customer order** and the **AI response** in the `flower_orders` table.  

   **Saved fields:**
   - `timestamp`
   - `full_name`
   - `phone_number`
   - `email`
   - `flower_type`
   - `delivery_date`
   - `delivery_address`
   - `customer_question`
   - `ai_answer`

---

## 📊 Data Flow

**Google Form → Google Sheets → n8n Workflow → AI FAQ Bot → Supabase Database**

---

## 🛠️ Tech Stack

- **n8n** – Workflow automation
- **Google Sheets** – Form responses + FAQ knowledge base
- **OpenRouter AI (glm-4.5-air:free)** – Customer Q&A
- **Supabase** – Order & Q&A storage

---

## ✅ Benefits

- Fully **automated order logging** – no manual work
- **Instant FAQ answers** for customers
- **Centralized database** for easy tracking
- **Fallback handling** when no FAQ match is found

---

