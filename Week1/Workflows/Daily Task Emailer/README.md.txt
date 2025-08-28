==================================================
               DAILY TASK EMAILER – N8N WORKFLOW
==================================================

DESCRIPTION:
Automates sending daily task emails from a Google Sheet to a recipient using n8n.

FEATURES:
- Fetch tasks from Google Sheets
- Format tasks into a clean, readable list
- Send the task list via Gmail automatically
- Scheduled to run daily at 8 AM

SETUP:
1. Import the workflow JSON into your n8n instance
2. Configure Google Sheets OAuth2 credentials to access your task sheet
3. Configure Gmail OAuth2 credentials to send emails
4. Update the Sheet ID and Recipient Email as needed
5. Activate the workflow

WORKFLOW STEPS:
1. Schedule Trigger      - runs daily at 8 AM
2. Fetch Tasks from Sheet - reads all tasks from Google Sheets
3. Format Task List       - formats tasks for email
4. Set Recipient          - assigns the email recipient
5. Email Tasks to User    - sends the formatted task list via Gmail

NOTES:
- Supports one or multiple recipients
- Task formatting can be customized in the Code Node
- Ensure the Google Sheet column names match the workflow


┌────────────────────┐
│  Schedule Trigger  │
│  (Daily at 8 AM)  │
└─────────┬──────────┘
          │
          ▼
┌─────────────────────────────┐
│ Fetch Tasks from GoogleSheet│
│      (Read all tasks)       │
└─────────┬───────────────────┘
          │
          ▼
┌─────────────────────────────┐
│     Format Task List        │
│  (Convert tasks to text)   │
└─────────┬───────────────────┘
          │
          ▼
┌─────────────────────────────┐
│       Set Recipient         │
│  (Assign email address)     │
└─────────┬───────────────────┘
          │
          ▼
┌─────────────────────────────┐
│   Email Tasks to User       │
│ (Send email via Gmail)      │
└─────────────────────────────┘

