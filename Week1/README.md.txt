# 📚 Salma Azoz – Week 1 Overview


## 📂 Table of Contents

1. Automation Workflows (n8n)

   * Daily Task Emailer
   * Daily Task Emailer AI
   * Mini ML Project (Supabase + Google Sheets)

2. Machine Learning Projects

   * Spaceship Titanic Dataset
   * Heart Disease Prediction
   * Bank Loan Prediction

3. Database & CRUD Tasks

   * Supabase Tasks CRUD

4. Notes & References

---

## ⚙️ Automation Workflows (n8n)

### 1. Daily Task Emailer

**Purpose:** Automate sending daily task emails from a Google Sheet to a recipient using n8n.

**Features:**

* Fetch tasks from Google Sheets
* Format tasks into a readable list
* Send task list via Gmail automatically
* Scheduled daily at 8 AM

**Workflow Steps:**

1. Schedule Trigger – Runs daily at 8 AM
2. Fetch Tasks from Sheet – Reads all tasks from Google Sheets
3. Format Task List – Formats tasks for email
4. Set Recipient – Assigns the email recipient
5. Email Tasks to User – Sends the formatted task list via Gmail

**Notes:**

* Supports multiple recipients
* Task formatting is customizable in the code node
* Ensure Google Sheet column names match the workflow

---

### 2. Daily Task Emailer AI

**Purpose:** Sends summarized daily tasks using LLM (AI) for concise summaries.

**Features:**

* Fetch tasks from Google Sheets
* Format tasks into a structured list
* Summarize tasks using LLM
* Send personalized, concise email to the user

**Workflow Steps:**

1. Schedule Trigger – Daily at 8 AM
2. Fetch Tasks from Sheet – Read Google Sheet tasks
3. Format Task List – Prepare structured task list
4. Summarize Tasks – LLM summarizes key tasks
5. Set Recipient – Define recipient email
6. Email Tasks to User – Send summarized tasks

**Notes:**

* Summaries limited to 2–3 sentences
* Friendly, motivating tone
* Easy to integrate with multiple recipients

---

### 3. Mini ML Project – Supabase + Google Sheets

**Purpose:** Fetch ML model results from Supabase, summarize, and save to Google Sheets.

**Workflow Steps:**

1. Schedule Trigger – Runs daily at 8 AM
2. Fetch Model Results – Pulls ML model metrics from Supabase
3. Aggregate Metrics – Combines metrics for summary
4. Summarize Results – LLM summarizes accuracy, F1 score, ROC AUC
5. Prepare Row Data – Prepares row for Google Sheet
6. Save to Google Sheet – Appends summary to Google Sheet

**Notes:**

* Friendly summaries using LLM
* Easy to read in Google Sheets
* Summaries highlight most important metrics

---

## 🤖 Machine Learning Projects

### 1. Spaceship Titanic Dataset

**Purpose:** Predict passenger survival on Spaceship Titanic using ML.

**Key Steps:**

* Data cleaning & preprocessing
* Feature engineering
* Model training (XGBoost, Random Forest, Deep Learning)
* Evaluation (Accuracy, F1 Score, ROC AUC)

**Notes:**

* Handled missing values and outliers
* Ensemble models improved performance

---

### 2. Heart Disease Prediction

**Purpose:** Predict heart disease presence using patient data.

**Key Steps:**

* Load & explore dataset
* Preprocessing (scaling, encoding)
* Train/test split
* Train models: Decision Tree, Random Forest
* Evaluate using accuracy, F1 score, ROC AUC
* Visualize confusion matrices

**Notes:**

* Scaled numeric features
* Evaluated model performance thoroughly

---

### 3. Bank Loan Prediction

**Purpose:** Predict whether a customer accepts a personal loan.

**Key Steps:**

* Load dataset & explore
* Drop irrelevant columns (ID, ZIP)
* Standardize features
* Train Decision Tree and Random Forest with GridSearchCV
* Evaluate models (accuracy, F1 score, ROC AUC)
* Insert model results into Supabase

**Notes:**

* Included parameter tuning
* Stored results in Supabase for tracking

---

## 🗄️ Database & CRUD Tasks

### Supabase Tasks CRUD

**Purpose:** Practice inserting, fetching, updating, and deleting tasks using Supabase.

**Key Steps:**

1. Connect to Supabase project
2. Insert tasks: single & multiple
3. Fetch all tasks
4. Update task status
5. Delete tasks by ID

**Notes:**

* Simple CRUD example for task management
* Can integrate with n8n workflows or Python scripts

---

## 📝 Notes & References

* Google Sheets for task tracking
* Supabase for database backend
* n8n for workflow automation
* LLM for friendly, summarized task emails
* Machine learning references: Titanic dataset, Heart disease dataset, Bank loan dataset

**Author:** Salma Azoz
**Week:** Full summary of all projects, ML experiments, and automation workflows
**Status:** All workflows ready to run; ML models evaluated and results stored
