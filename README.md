# iTech Learning - Salma 🚀

Welcome to my learning journey as an **AI Engineer Trainee at iTech Solutions**.  
This repository documents my weekly progress during the internship, covering **machine learning, data pipelines, Supabase integration, and AI agent development with workflow automation**.  

> ⚡ Status: Internship ongoing — updates will continue week by week.

---

## 📂 Folder Structure

Week1/  
├── Notebooks/  
│   ├── Heart/  
│   ├── Loan_Supabase/  
│   ├── Supabase_Trial/  
│   └── Titanic/  
└── Workflows/  
    ├── Daily Task Emailer AI/  
    └── Daily Task Emailer/  

Week2/  
├── Notebooks/  
│   ├── FAQ_Bot_Embedding/  
│   └── Simulate_WhatsApp_Messages/  
└── Workflows/  
    ├── FAQ_Bot/  
    ├── Order & FAQ Automation_FlowerStore/  
    └── Telegram_AI_Assitant/  

Week3/  
├── Notebooks/  
│   ├── Telgram_ai_bot_python/  
│   │   ├── telegram_ai_assistant_with_supabase.ipynb  
│   │   └── telegram_ai_sop.md  
│   └── Telgram_ai_bot_python+chache/  
│       └── telegram_ai_assistant_with_supabase+chache.ipynb  
└── Workflows/  
    ├── Error_handling/  
    │   └── Error Monitoring & Notifications.json  
    └── Sales_data_engine/  
        └── Sales Data Engine — CSV to Supabase.json  

Week4/  
├── Notebooks/  
│   ├── Dual-Agent Intent Validation v2.json  
│   ├── Dual-Agent Intent Validation.json  
│   ├── Sales Data Engine V2.json  
│   └── Webhook - Evolution Sim (1).json  
└── day28_pilot_pack/  
    ├── .env  
    ├── LoadTest_Report.pdf  
    ├── load_test.py  
    ├── requirements.txt  
    ├── results/  
    │   └── results.csv  
    └── runbook.pdf  

Week5/  
└── Workflows/  
    ├── Full pipeline (1).json  
    ├── Social Media Lead Capture — Scoring & Auto-Tag.json  
    ├── Social Media Lead Capture.json  
    ├── WhatsApp Lead Capture & AI Response Flow (1).json  
    ├── WhatsApp Lead Capture Flow — IWAA.json  
    └── WhatsApp Lead Capture — Intent Routing.json  

---

## 📘 Internship Progress

### 🔹 Week 1 (Days 1–7) — Foundations
- **Day 1 – Environment Setup & GitHub** → Installed Python, Jupyter/Colab, Git, and n8n. Practiced GitHub workflows.  
- **Day 2 – Data Cleaning & Preprocessing** → Worked with Titanic & Heart datasets. Feature engineering, normalization.  
- **Day 3 – Model Training & Evaluation** → Trained Logistic Regression, Random Forest, and XGBoost. Random Forest performed best.  
- **Day 4 – Workflow Automation (n8n)** → Google Sheets automation + AI summarization APIs.  
- **Day 5 – Supabase Integration** → CRUD operations, Row-Level Security (RLS).  
- **Day 6 – AI Agents & Prompt Engineering** → Built a simple RAG demo with external knowledge.  
- **Day 7 – Mini Project** → Bank Loan pipeline → preprocessing → Random Forest → Supabase metrics → daily n8n automation.  

✅ **Outcome**: Built strong foundations in ML, Supabase backend, and workflow automation.  

---

### 🔹 Week 2 (Days 8–14) — Applied Projects
- **Day 8 – GitHub Collaboration** → Created repo `itech-learning-salma`, structured Week1, practiced branching.  
- **Day 9 – WhatsApp Simulation** → Simulated messaging via Evolution API, logged chats in Supabase.  
- **Day 10 – Flower Bloom Order & FAQ Workflow** → Automated orders via Google Forms, integrated FAQ AI, stored orders in Supabase.  
- **Day 11 – Telegram AI Assistant with Memory** → Built Telegram bot with persistent memory using Supabase.  
- **Day 12–13 – FAQ Bot with Supabase** → Hybrid FAQ bot (Python embeddings + n8n keyword search). Logged conversations + daily summaries to Google Sheets.  
- **Day 14 – Demo & Report** → Recorded Loom demo, prepared report analyzing business extensions.  

✅ **Outcome**: Applied Week1 foundations into real-world scenarios — chatbots, order management, multi-channel assistants.  

---

### 🔹 Week 3 (Days 15–21) — Advanced Workflows & Error Handling
- **Day 15 – GitHub Collaboration & Pull Requests** → Forked an open-source n8n/Supabase repo, created a feature branch, opened a Pull Request, and documented PR steps.  
- **Day 16 – Supabase Schema Design (Leads & Conversations)** → Designed schema for `leads` and `conversations` tables with RLS enabled. Deliverable: SQL schema + screenshots.  
- **Day 17 – WhatsApp AI Assistant (Lite Version)** → Built sandbox WhatsApp AI Assistant using Evolution API simulation. Logged messages & AI responses into Supabase.  
- **Day 18 – Sales Data Engine (Prototype)** → Created workflow to process uploaded PDF/Excel files, extract structured sales data, and store in Supabase.  
- **Day 19 – Performance & Cost Optimization** → Researched token usage reduction strategies. Implemented batching/caching in WhatsApp Assistant Lite.  
- **Day 20 – Monitoring & Error Handling** → Added error handling in n8n, logged errors into `error_logs` table, and sent error notifications to Google Sheets/email.  
- **Day 21 – Weekly Demo & Report** → Recorded Loom demo (5–7 mins) showing WhatsApp Lite Assistant, Sales Data Engine, error handling & optimization. Wrote 2–3 page report *“From Sandbox to Production – How iTech AI Workflows Can Scale.”*  

✅ **Outcome**: Delivered sandbox AI assistant, sales data engine prototype, schema design, optimization, and robust error handling — all tied together with GitHub collaboration and documentation.  

---

### 🔹 Week 4 (Days 22–28) — Scaling & Load Testing
- **Day 22 – Supabase Schema Enhancements** → Extended schema with indexes & refined RLS for better query performance and data security.  
- **Day 23 – Webhook Ingestion Workflow** → Built n8n webhook ingestion with retry + deduplication logic, ensuring reliable event capture.  
- **Day 24 – Dual-Agent Intent Validation** → Designed a validator workflow with branching for FAQ, Booking, Lead capture, and fallback categories.  
- **Day 25 – Optimization with Caching** → Implemented caching layer (Redis) to reduce latency and optimize token usage in AI workflows.  
- **Day 26 – Sales Data Engine (V2)** → Enhanced ingestion pipeline to parse CSV/Excel/PDF files, validate schema, log errors, and store clean data in Supabase.  
- **Day 27 – Monitoring Dashboard** → Created Looker Studio dashboard showing message volumes, intents, errors, and before/after caching metrics.  
- **Day 28 – Load Test & Pilot Pack** → Performed load testing (50–100 concurrent chat sessions). Packaged Pilot Readiness Kit: repo structure, `.env` sample, runbook, load test report, and Loom demo.  

✅ **Outcome**: Delivered production-ready workflows with schema optimization, reliable ingestion, caching, monitoring dashboards, and stress-tested load performance — packaged into a full Pilot Readiness Kit.  

---

### 🔹 Week 5 (Days 29–35) — Lead Capture & Qualification Workflows  
- **Day 29 – WhatsApp Lead Capture Flow** → Built a workflow to capture WhatsApp leads via n8n webhook, auto-acknowledge messages, and log them into Supabase.  
- **Day 30 – Lead Qualification Scoring** → Designed a scoring model (0–10) based on urgency, budget mention, and service interest. Implemented scoring inside workflow.  
- **Day 31 – Multi-Channel Lead Collector (WhatsApp + Social)** → Unified schema in Supabase for WhatsApp, Instagram, and Facebook. Auto-tagged leads by source.  
- **Day 32 – Social Media Lead Capture (Instagram/Facebook)** → Simulated lead forms/DM capture, stored in Supabase with source tags. Workflow JSON + schema screenshot delivered.  
- **Day 33 – Lead Routing & Intent Detection** → Added routing layer to classify leads into categories (Support, Sales, General) and notify relevant teams.  
- **Day 34 – High-Priority Lead Alerts** → Configured email alerts with HTML template for high-score leads (e.g., budget mentioned + urgent). Sent to sales/support team automatically.  
- **Day 35 – Weekly Dashboard & Report** → Extended Looker Studio dashboard to include lead volumes, qualification scores, source breakdown, and high-priority alerts. Prepared weekly summary report.  

✅ **Outcome**: Delivered a complete lead management pipeline — capturing, scoring, routing, and alerting across multiple channels, integrated into dashboards and reports.  

---

📌 *This repo will be updated weekly to reflect my ongoing work at iTech Solutions.*  
