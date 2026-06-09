# ApiForge

> Open Source API Testing Platform for Generating, Executing, and Analyzing API Test Scenarios

![Python](https://img.shields.io/badge/python-3.10+-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-alpha-orange)

---

## Overview

ApiForge is an open-source API Testing Platform designed to simplify the creation and management of API test scenarios.

The project currently provides tools for generating:

* CURL commands
* Postman collections

from structured API configurations.

The long-term vision of ApiForge is to become a complete API testing ecosystem capable of:

* Scenario Generation
* Request Execution
* HTML & JSON Reporting
* Test Analytics
* Cartesian Product Testing
* Automated API Validation

---

## Features

### Current Features

* Generate CURL commands from API definitions
* Generate Postman collections automatically
* Support custom request headers
* Support query parameters
* Support request bodies
* JSON-based configuration
* Input validation
* Lightweight architecture
* Extensible codebase

### Planned Features

* CURL Runner Service
* HTML Report Generator
* JSON Report Generator
* API Test Analytics Engine
* Cartesian Product Test Generation
* Per-Endpoint Header Configuration
* Execution History
* Retry Mechanism
* Dashboard Metrics
* Test Result Aggregation

---

## Why ApiForge?

Modern API tools like Postman and ApiDog are excellent for designing, testing, and documenting APIs.

However, generating large numbers of API request variations often requires repetitive manual work.

ApiForge focuses on solving a different problem:

> Rapid API Scenario Generation and Automated API Testing

### Example

Suppose you have:

* 5 API endpoints
* 3 request bodies
* 4 query parameter sets

Traditional testing may require manually creating:

```text
5 × 3 × 4 = 60 Requests
```

ApiForge is designed to generate these scenarios automatically and export them into:

* CURL Commands
* Postman Collections

Future releases will also execute those requests automatically and generate detailed reports.

### Designed For

* QA Engineers
* Software Testers
* Test Automation Engineers
* Backend Developers
* DevOps Engineers
* API Developers

### Key Advantages

* Open Source
* Lightweight
* Fast
* Automation-Friendly
* QA-Oriented
* Extensible Architecture
* Future-Ready Roadmap

---

## Project Status

ApiForge is currently in the **Alpha Stage**.

### Implemented

* CURL Generator
* Postman Collection Generator
* Request Validation
* JSON Input Support

### In Progress

* Architecture Refactoring
* Service Layer Improvements

### Planned

* CURL Runner
* HTML Reports
* JSON Reports
* Analytics Engine
* Cartesian Product Testing
* Per-URL Header Support

---

## Architecture

### Current Architecture

```text
JSON Input
    │
    ▼
Validation Layer
    │
    ▼
Scenario Builder
    │
    ├── CURL Generator
    │
    └── Postman Generator
```

### Future Architecture

```text
Scenario Builder
    │
    ▼
Execution Engine
    │
    ▼
Report Generator
    │
    ├── HTML Reports
    ├── JSON Reports
    │
    ▼
Analytics Engine
```

---

## Project Structure

```text
ApiForge/
│
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   └── feature_request.md
│   │
│   └── workflows/
│       ├── python-tests.yml
│       └── release.yml
│
├── docs/
│   └── roadmap.md
│
├── examples/
│   └── sample_request.json
│
├── tests/
│   ├── __init__.py
│   ├── test_curl_builder.py
│   ├── test_postman_builder.py
│   └── test_models.py
│
├── app.py
├── models.py
├── curl_builder.py
├── postman_builder.py
├── utils.py
│
├── README.md
├── LICENSE
├── CHANGELOG.md
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── requirements.txt
├── setup.py
├── pyproject.toml
└── .gitignore
```

---

## Installation


### 1. Clone Repository

```bash
git clone https://github.com/your-username/apiforge.git
cd apiforge
```

### 2. Create Virtual Environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Start Development Server

```bash
python -m uvicorn app:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

### 5. Open API Documentation

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

---

## Example Input

```json
{
  "urls": [
    "https://api.example.com/users"
  ],
  "methods": [
    "GET"
  ],
  "headers": {
    "Authorization": "Bearer token"
  },
  "query_params": {
    "page": "1"
  }
}
```

---

## Running Tests

Run all tests:

```bash
pytest tests -v
```

Run a specific test:

```bash
pytest tests/test_curl_builder.py -v
```

---

## Tech Stack

ApiForge is built with:

* Python 3.10+
* Flask
* JSON
* REST API Principles
* Pytest
* GitHub Actions

Future integrations may include:

* Pandas
* Jinja2
* SQLite
* Plotly

---

## Roadmap

See the detailed roadmap:

```text
docs/roadmap.md
```

Upcoming milestones:

* CURL Runner Service
* HTML Report Generator
* JSON Report Generator
* Analytics Engine
* Cartesian Product Testing
* Header Management Per Endpoint

---

## Contributing

Contributions are welcome.

Please read:

* CONTRIBUTING.md
* CODE_OF_CONDUCT.md

before submitting Pull Requests.

---

## Changelog

Project history is maintained in:

```text
CHANGELOG.md
```

---

## License

This project is licensed under the MIT License.

See:

```text
LICENSE
```

for more details.

---

## Support

If you find a bug or want to request a feature, please create an issue through GitHub.

Bug reports and feature requests help improve ApiForge for everyone.

---

## Vision

ApiForge aims to become a complete API Testing Platform that helps teams:

* Generate test scenarios
* Execute API requests
* Analyze responses
* Produce reports
* Improve API quality

from a single lightweight and open-source platform.
