# Mini_Project – ML Model Results Summarizer 🚀

Hey there! This n8n workflow helps you **automatically fetch, summarize, and save your machine learning model results**—all without lifting a finger. Perfect for keeping your Google Sheet up-to-date with concise insights from your experiments! ✨

---

## What It Does

- **Fetch** your ML model results from Supabase.
- **Aggregate** key metrics like Accuracy, F1 Score, and ROC AUC into a single summary.
- **Summarize** results with a friendly LLM assistant, keeping it short and clear (1–2 sentences).
- **Save** the summary with a timestamp in Google Sheets.
- Runs **automatically every day at 8 AM**, so you always have fresh updates.

---

## How to Set It Up

1. Import the workflow JSON into your n8n instance.
2. Connect your **Supabase account** to access the `model_results` table.
3. Connect your **Google Sheets account** to save the summaries.
4. Connect your **LLM/OpenRouter account** to generate summaries.
5. Activate the workflow and let it work its magic! 🎩✨

---

## Workflow Steps 

1. **Schedule Trigger** – Our workflow wakes up daily at 8 AM. ⏰
2. **Fetch Model Results** – Pulls all your ML experiment results. 📊
3. **Aggregate Metrics** – Combines everything into a neat summary. 📝
4. **Summarize Results** – LLM crafts a friendly, concise summary highlighting the most important metrics. 💡
5. **Prepare Row Data** – Adds a timestamp to your summary. ⏱️
6. **Save to Google Sheet** – Appends the summary to your sheet, ready to share! 📑

---

## Notes

- Handles multiple models gracefully.
- You can tweak the LLM’s messages to change the tone or level of detail.
- Each summary comes with a timestamp, so you always know when it was generated.
- Fully automatic—no manual updates needed! 🎉

---

## Visual Workflow (Friendly ASCII-style)

=========================================================
               MINI_PROJECT – N8N WORKFLOW 🚀
=========================================================

Schedule Trigger (Wake up at 8 AM)
        |
        v
Fetch Model Results (Supabase: model_results)
        |
        v
Aggregate Metrics (Combine all metrics into summary)
        |
        v
Summarize Results (LLM: Friendly & concise summary)
        |
        v
Prepare Row Data (Add timestamp)
        |
        v
Save to Google Sheet (Append summary to Sheet1)
=========================================================
