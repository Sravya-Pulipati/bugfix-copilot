# 🐞 BugFix Copilot

🔥 **AI-powered log analysis system with similarity detection & severity classification**

BugFix Copilot is a production-style debugging assistant that analyzes application logs, extracts errors, detects similar past issues, classifies severity, and suggests fixes.

---

## 🚀 Features

### 🧩 Core Features

* Parse raw logs and extract meaningful error messages
* Identify common exceptions (IndexError, NullPointer, etc.)
* Provide structured debugging insights:

  * Root Cause
  * Affected Module
  * Fix Suggestion

---

### 🧠 Advanced Features

#### 🔍 Similarity-Based Bug Detection

* Compares new errors with historical logs
* Reuses previous solutions if similar issue found
* Reduces redundant analysis

---

#### 🚨 Severity Classification

Categorizes errors based on impact:

| Severity  | Description                                  |
| --------- | -------------------------------------------- |
| 🔴 HIGH   | Critical failures (system crash, DB down)    |
| 🟡 MEDIUM | Runtime exceptions (IndexError, NullPointer) |
| 🟢 LOW    | Minor issues / warnings                      |

---

#### 📊 Real-Time Log Monitoring

* Errors are written to `app.log`
* System reads and analyzes logs dynamically
* Mimics real-world monitoring tools

---

#### 🎨 UI Dashboard

* Simple frontend to:

  * Generate errors
  * Analyze logs
* Displays results instantly
* Severity-based color coding:

  * 🔴 Red → HIGH
  * 🟠 Orange → MEDIUM
  * 🟢 Green → LOW

---

## 🧠 Architecture

```text
Client (UI/Postman)
        ↓
Django API
        ↓
Log Generator → app.log
        ↓
Log Reader
        ↓
Parser → Extract Error
        ↓
Similarity Engine → Check past logs
        ↓
Severity Classifier
        ↓
AI Analyzer (LLM / Mock)
        ↓
Response (JSON/UI)
```

---

## ⚙️ Tech Stack

* Python
* Django
* Django REST Framework
* SQLite (default DB)
* OpenAI API (optional / fallback supported)

---

## ▶️ How to Run

```bash
git clone https://github.com/<your-username>/bugfix-copilot.git
cd bugfix-copilot

python -m venv venv
```

### Activate venv:

**PowerShell**

```bash
venv\Scripts\Activate.ps1
```

**Git Bash**

```bash
source venv/Scripts/activate
```

---

### Install dependencies

```bash
pip install -r requirements.txt
```

---

### Run migrations

```bash
python manage.py migrate
```

---

### Start server

```bash
python manage.py runserver
```

---

## 🌐 Access Application

```text
http://127.0.0.1:8000/
```

---

## 🔌 API Endpoints

### 1️⃣ Generate Error

```
GET /generate-error/
```

👉 Simulates runtime error and logs it to `app.log`

---

### 2️⃣ Auto Analyze Logs

```
GET /auto-analyze/
```

👉 Reads logs → parses → analyzes → returns insights

---

### 3️⃣ Analyze Custom Log

```
POST /analyze/
```

#### Request:

```json
{
  "log": "IndexError: list index out of range"
}
```

#### Response:

```json
{
  "parsed_error": "IndexError: list index out of range",
  "severity": "MEDIUM",
  "ai_analysis": {
    "analysis": "Root cause: accessing invalid index..."
  }
}
```

---

## 🔄 Working Flow

```text
Generate Error → Stored in app.log →
Read Logs → Parse Error →
Check Similarity →
Classify Severity →
AI Analysis →
Return Response → Display in UI
```

---

## 🗄️ Database Model

**BugLog**

* raw_log
* parsed_error
* ai_analysis
* severity

---

## ⚠️ Common Issues & Fixes

### ❌ No module named django

```bash
pip install django djangorestframework
```

---

### ❌ venv permission issue

```bash
deactivate
rm -rf venv
python -m venv venv
```

---

### ❌ OpenAI quota error

* System automatically falls back to mock response
* No impact on functionality

---

## 💡 Best Practices

* Always activate virtual environment
* Do NOT commit `venv/` to GitHub
* Use `.gitignore` properly

---

## 🚧 Future Improvements

* Vector embeddings for smarter similarity
* Dashboard with charts & analytics
* Async processing (Kafka / Celery)
* Real-time log streaming

---

## 🎯 Resume Value

This project demonstrates:

* Backend system design
* Real-time log processing
* API development
* Performance optimization (reuse via similarity)
* Production-like architecture

---

## 💡 Motivation

To reduce debugging time by automating log analysis and prioritizing critical issues using intelligent systems.

---

## 👩‍💻 Author

**Sravya Pulipati**

---
