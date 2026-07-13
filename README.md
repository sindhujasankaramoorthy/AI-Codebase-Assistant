<div align="center">

# 🧠 AI Codebase Assistant

**An AI-powered backend that scans local and GitHub repositories, extracts code and repository metadata, and prepares repositories for intelligent AI-powered code analysis.**

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat-square&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat-square&logo=fastapi)
![Uvicorn](https://img.shields.io/badge/Uvicorn-ASGI-4B8BBE?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Status](https://img.shields.io/badge/Status-In%20Development-yellow?style=flat-square)

</div>

---

## 📑 Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Getting Started](#-getting-started)
- [Current API](#-current-api)
- [Current Capabilities](#-current-capabilities)
- [Upcoming Features](#-upcoming-features)

---

## ✨ Features

| | |
|---|---|
| ✅ | Scan local repositories |
| ✅ | Clone and scan public GitHub repositories |
| ✅ | Ignore unnecessary directories (`.git`, `.venv`, `venv`, `node_modules`, `__pycache__`) |
| ✅ | Extract file metadata (name, path, extension, size) |
| ✅ | Read supported source code and text file contents |
| ✅ | Repository analytics (total files, total size, extension statistics) |
| ✅ | Detect largest and smallest files |
| ✅ | Calculate average file size |
| ✅ | Identify the most common file extension |
| ✅ | Generate repository summary (README, LICENSE, .gitignore, primary language) |
| ✅ | REST API built with FastAPI |

---

## 🛠 Tech Stack

| Layer | Technology |
|-------|------------|
| Language | Python |
| Backend | FastAPI |
| ASGI Server | Uvicorn |
| Version Control | Git |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- Git installed and available on your PATH

### Installation

```bash
git clone https://github.com/sindhujasankaramoorthy/AI-Codebase-Assistant
cd AI-Codebase-Assistant/backend
pip install -r requirements.txt
```

### Run the Server

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

---

## 📡 Current API

### Scan a GitHub Repository

**`GET`** `/scan-github`

#### Query Parameter

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `url` | string | Yes | Public GitHub repository URL |

#### Example Request

```
http://127.0.0.1:8000/scan-github?url=https://github.com/octocat/Hello-World.git
```

#### Example Response

```json
{
  "repository_url": "https://github.com/octocat/Hello-World.git",
  "total_files": 1,
  "total_size": 14,
  "extension_count": {
    "": 1
  },
  "largest_file": {
    "name": "README",
    "path": "README",
    "size": 14
  },
  "smallest_file": {
    "name": "README",
    "path": "README",
    "size": 14
  },
  "average_file_size": 14,
  "most_common_extension": {
    "extension": "",
    "count": 1
  },
  "summary": {
    "has_readme": true,
    "has_license": false,
    "has_gitignore": false,
    "main_language": "Unknown"
  },
  "files": [
    {
      "name": "README",
      "path": "README",
      "extension": "",
      "size": 14,
      "content": null
    }
  ]
}
```

---

## ⚙️ Current Capabilities

The backend can currently:

- Clone public GitHub repositories
- Scan repository files recursively
- Ignore unnecessary directories
- Read supported source code files
- Extract metadata from every file
- Generate repository statistics
- Produce a high-level repository summary

> This forms the foundation for **Retrieval-Augmented Generation (RAG)** and AI-powered code understanding.

---

## 🔮 Upcoming Features

- [ ] Code chunking
- [ ] Embedding generation
- [ ] Vector database integration (FAISS)
- [ ] Semantic code search
- [ ] AI-powered repository chat
- [ ] Code summarization
- [ ] Repository question answering
- [ ] Frontend interface
- [ ] Deployment
