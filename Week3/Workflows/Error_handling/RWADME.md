# n8n Error Monitoring & Notifications Workflow

This workflow is designed to **catch errors** from any n8n workflow, **log them to Supabase**, and **send email notifications** via Gmail. It ensures that you are immediately aware of any failures in your automation processes.

---

## Features

- **Catch Workflow Errors**: Triggered whenever an error occurs in any workflow.
- **Prepare Error Payload**: Extracts relevant information such as workflow name, error message, stack trace, and timestamp.
- **Log Error to Supabase**: Stores error details in a Supabase table (`error_logs`) for monitoring and auditing.
- **Send Error Notification Email**: Sends a notification email to the specified recipient with error details.

---

## Workflow Nodes

1. **Catch Workflow Errors**
   - Node type: `Error Trigger`
   - Listens for workflow errors.

2. **Prepare Error Payload**
   - Node type: `Function`
   - Prepares JSON payload containing:
     - `workflow_name`
     - `error_message`
     - `error_stack`
     - `error_time`

3. **Log Error to Supabase**
   - Node type: `HTTP Request`
   - Sends a POST request to Supabase REST API to log errors.
   - Requires `supabaseApi` credentials.

4. **Send Error Notification Email**
   - Node type: `Gmail`
   - Sends email notifications to the designated recipient.
   - Requires `gmailOAuth2` credentials.
   - Email subject and body include workflow name, error message, timestamp, and stack trace.

---

## Supabase Setup

1. Create a Supabase project.
2. Create an `error_logs` table with the following columns:

| Column         | Type      |
|----------------|-----------|
| workflow_name  | text      |
| error_message  | text      |
| error_stack    | text      |
| error_time     | timestamp |
| created_at     | timestamp (default now) |

3. Create API credentials in n8n (`supabaseApi`) for authentication.

---

## Gmail Setup

1. Set up a Gmail account.
2. Create OAuth2 credentials in n8n (`gmailOAuth2`) for sending emails.
3. Add the recipient email in the `Send Error Notification Email` node.

---

## How It Works

1. When any workflow in n8n fails, the **Catch Workflow Errors** node triggers.
2. **Prepare Error Payload** formats the error data.
3. **Send Error Notification Email** immediately notifies the user.
4. **Log Error to Supabase** stores the error for monitoring and analysis.

---

## Notes

- You can customize the **recipient email** in the Gmail node.
- Ensure the Supabase table `error_logs` exists and matches the payload structure.
- Useful for **production workflows** where monitoring and alerting are critical.

---

## References

- [n8n Docs](https://docs.n8n.io/)
- [Supabase Docs](https://supabase.com/docs)
- [Gmail API](https://developers.google.com/gmail/api)
