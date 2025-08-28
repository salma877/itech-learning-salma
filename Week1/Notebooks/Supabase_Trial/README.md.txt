Supabase Task Manager

This Python script demonstrates how to interact with a Supabase database using the Supabase Python client. It includes operations to insert, fetch, update, and delete tasks in a Tasks table.

Features:

Insert a single task

Insert multiple tasks at once

Fetch all tasks from the table

Update a task’s status by ID

Delete a task by ID

View the table contents after operations

Requirements:

Python 3.7 or higher

supabase Python package

Install Supabase client:

pip install supabase

Configuration:

Replace the following values with your Supabase project details:

url = "https://YOUR_PROJECT_URL.supabase.co"
key = "YOUR_ANON_PUBLIC_KEY"

Usage:

Connect to your Supabase project using create_client.

Use insert() to add tasks to the Tasks table.

Use select() to fetch tasks.

Use update() to modify task status by ID.

Use delete() to remove a task by ID.

Example operations included in the script:

Insert a single task: "Train AI model"

Insert multiple tasks: "Check emails", "Prepare report", "Team meeting"

Update task ID 2 to "done"

Delete task ID 3

Output

The script prints:

Inserted tasks

All tasks before and after updates

Confirmation of updates and deletions