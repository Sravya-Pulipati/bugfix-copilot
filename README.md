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
