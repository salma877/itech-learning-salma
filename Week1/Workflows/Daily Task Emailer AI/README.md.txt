=========================================================
                 DAILY TASK EMAILER AI – N8N WORKFLOW
=========================================================

DESCRIPTION:
Automates fetching tasks from a Google Sheet, generating a short AI-based summary, and sending the summarized tasks via Gmail.

FEATURES:
- Fetch tasks from Google Sheets
- Format tasks into a clean, readable list
- Summarize tasks using AI (LangChain / OpenRouter LLM)
- Send summarized task list via Gmail automatically
- Scheduled to run daily at 8 AM

SETUP:
1. Import the workflow JSON into your n8n instance
2. Configure Google Sheets OAuth2 credentials to access your task sheet
3. Configure Gmail OAuth2 credentials to send emails
4. Configure OpenRouter API credentials for AI summarization
5. Update the Sheet ID and Recipient Email as needed
6. Activate the workflow

WORKFLOW STEPS:
1. Schedule Trigger      - runs daily at 8 AM
2. Fetch Tasks from Sheet - reads all tasks from Google Sheets
3. Format Task List       - formats tasks for AI processing
4. Summarize Tasks        - generates a short, motivating summary of tasks
5. Set Recipient          - assigns the email recipient
6. Email Tasks to User    - sends the AI-generated summary via Gmail

NOTES:
- Supports one or multiple recipients
- Task formatting and summary prompts can be customized in the Code and Summarize nodes
- Ensure the Google Sheet column names match the workflow
- LLM model can be changed or fine-tuned for different summarization styles


Schedule Trigger (Runs daily at 8 AM)
        |
        v
Fetch Tasks from Sheet (Google Sheets)
        |
        v
Format Task List (Code Node)
        |
        v
Summarize Tasks (AI / LangChain + LLM)
        |
        v
Set Recipient (Assign Email)
        |
        v
Email Tasks to User (Gmail)