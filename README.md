# 🐞 BugFix Copilot

An AI-assisted debugging tool that analyzes application logs, extracts errors, and suggests root causes and fixes.

---

## 🚀 Features

* Parse raw logs and extract meaningful error messages
* Identify common exceptions (NullPointer, IndexOutOfBounds, etc.)
* Provide structured debugging insights:

  * Root Cause
  * Affected Module
  * Fix Suggestion
* REST API built with Django REST Framework

---

## 🧠 Architecture

Client → Django API → Log Parser → AI Analyzer (mock/LLM-ready) → Response

---

## ⚙️ Tech Stack

* Python
* Django
* Django REST Framework
* SQLite (default DB)

---

## ▶️ How to Run

```bash
git clone https://github.com/<your-username>/bugfix-copilot.git
cd bugfix-copilot

python -m venv venv
source venv/Scripts/activate   # Windows (Git Bash)

pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
```

---

## 🐍 Virtual Environment Setup (Windows)

This project uses a Python virtual environment (`venv`) to manage dependencies. Follow these steps to set it up correctly.

---

### 🔹 1. Create Virtual Environment

```bash
python -m venv venv
```

---

### 🔹 2. Activate Virtual Environment

#### ▶️ For PowerShell:

```bash
venv\Scripts\Activate.ps1
```

#### ▶️ For Git Bash:

```bash
source venv/Scripts/activate
```

---

### 🔹 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 🔹 4. Run the Server

```bash
python manage.py runserver
```

---

## ⚠️ Common Issues & Fixes

### ❌ Issue: `No module named django`

👉 Fix:

* Ensure virtual environment is activated
* Reinstall dependencies:

```bash
pip install django djangorestframework
```

---

### ❌ Issue: `Permission denied: venv\Scripts\python.exe`

👉 Fix:

* Your virtual environment is corrupted
* Delete and recreate:

```bash
deactivate
rm -rf venv   # or manually delete folder
python -m venv venv
```

---

### ❌ Issue: Activation script blocked (PowerShell)

👉 Fix:

```bash
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

---

## 💡 Best Practices

* Always activate `venv` before running the project
* Do NOT create a virtual environment inside another active `venv`
* Do NOT commit `venv/` to GitHub (already ignored in `.gitignore`)

---


## 🔌 API Usage

### Endpoint:

POST `/analyze/`

### Request:

```json
{
  "log": "IndexOutOfBoundsException in OrderService"
}
```

### Response:

```json
{
  "parsed_error": "IndexOutOfBoundsException in OrderService",
  "ai_analysis": {
    "root_cause": "Accessing index beyond array/list size",
    "module": "OrderService",
    "fix": "Check list size before accessing elements"
  }
}
```

---

## 🚧 Future Improvements

* Integrate real LLM APIs
* Add similarity search for past bugs
* Introduce async processing (Kafka/RabbitMQ)
* Add frontend dashboard

---

## 💡 Motivation

Reduce debugging time by automating log analysis and suggesting actionable fixes.

---
