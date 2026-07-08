<div align="center">

# AI Codebase Assistant

**An AI-powered backend that scans local and GitHub repositories to collect file metadata — the foundation for smarter, AI-driven code analysis.**

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat-square&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat-square&logo=fastapi)
![Uvicorn](https://img.shields.io/badge/Uvicorn-ASGI-4B8BBE?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Status](https://img.shields.io/badge/Status-In%20Development-yellow?style=flat-square)

</div>

---

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [Current API](#current-api)
- [Upcoming Features](#upcoming-features)

---

## Features

| | |
|---|---|
| ✅ | Scan local repositories |
| ✅ | Clone and scan public GitHub repositories |
| ✅ | Ignore unnecessary directories (`.git`, `.venv`, `venv`, `node_modules`, `__pycache__`) |
| ✅ | Extract file metadata — name, relative path, extension, size |
| ✅ | REST API built with FastAPI |

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Language | Python |
| API Framework | FastAPI |
| Server | Uvicorn |
| Version Control | Git |

---

## Getting Started

### Prerequisites

- Python 3.9+
- Git installed and available on your PATH

### Installation

```bash
git clone https://github.com/sindhujasankaramoorthy/AI-Codebase-Assistant
cd ai-codebase-assistant
pip install -r requirements.txt
```

### Run the Server

```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

---

## Current API

### Scan a GitHub Repository

`GET /scan-github`

**Query Parameters**

| Parameter | Type   | Required | Description                        |
|-----------|--------|----------|-------------------------------------|
| url       | string | Yes      | The GitHub repository URL to scan   |

**Example Request**

```
http://127.0.0.1:8000/scan-github?url=https://github.com/octocat/Hello-World.git
```

**Example Response**

```json
{
  "repository": "https://github.com/octocat/Hello-World.git",
  "file_count": 3,
  "files": [
    {
      "name": "README.md",
      "path": "README.md",
      "extension": ".md",
      "size": 2048
    }
  ]
}
```

---

## Upcoming Features

- [ ] Read file contents
- [ ] Repository statistics
- [ ] AI-powered code analysis
- [ ] Code summarization
- [ ] Question answering over repositories
