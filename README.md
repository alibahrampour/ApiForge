# ApiForge

Generate CURL commands and Postman collections from API testing scenarios.

ApiForge is a lightweight API scenario generator built with FastAPI. It helps QA Engineers, API Testers, Developers, and Automation Engineers generate multiple CURL commands and Postman collections from a single API definition.

---

## Features

### Current Features

* Generate CURL commands
* Generate Postman Collection (v2.1)
* Multiple API Routes
* Multiple Request Bodies
* Multiple Query Parameters
* Scenario Combination Generation
* Export CURL Script File
* Export Postman Collection JSON

---

## Use Cases

### API Testing

Generate dozens of API test scenarios automatically.

### Postman Collection Generation

Create importable Postman collections from API definitions.

### Automation Preparation

Prepare API test cases before implementing automated tests.

### QA Scenario Generation

Quickly create different request combinations for manual testing.

---

## Tech Stack

* Python 3.10+
* FastAPI
* Pydantic
* Uvicorn

---

## Project Structure

```text
apiforge/
│
├── src/
│   ├── app.py
│   ├── models.py
│   ├── curl_builder.py
│   ├── postman_builder.py
│   └── utils.py
│
├── output/
│
├── examples/
│   └── sample_request.json
│
├── tests/
│
├── docs/
│   └── roadmap.md
│
├── requirements.txt
├── README.md
├── LICENSE
├── setup.py
└── pyproject.toml
```

---

## Why ApiForge?

Modern API tools like Postman and ApiDog are excellent for designing, testing, and documenting APIs. However, generating large numbers of request variations often requires manual work.

ApiForge focuses on one specific problem:

> Rapid API Scenario Generation

Instead of manually creating dozens of requests, ApiForge automatically generates test scenarios from combinations of:

* Routes
* Request Bodies
* Query Parameters

### Example

Suppose you have:

* 5 API endpoints
* 3 request bodies
* 4 query parameter sets

Creating all possible test cases manually would require:

```text
5 × 3 × 4 = 60 Requests
```

ApiForge generates them automatically and exports:

* CURL Scripts
* Postman Collections

### Designed For

* QA Engineers
* Software Testers
* API Automation Engineers
* Backend Developers
* DevOps Engineers

### Current Goal

Generate API testing scenarios quickly and consistently.

### Future Vision

ApiForge is evolving into a complete API Testing Platform that will support:

* Scenario Generation
* CURL Execution
* Retry Mechanisms
* JSON Reports
* HTML Reports
* API Analytics
* Test Result Statistics
* Cartesian Product Testing

### Why Not Just Use Postman?

Postman is excellent for API execution and collaboration.

ApiForge complements Postman by automating the generation of large numbers of API test scenarios and exporting them directly as Postman collections.

### Why Not Just Use ApiDog?

ApiDog focuses on API design, debugging, documentation, and testing.

ApiForge focuses on bulk scenario generation and future automated execution/reporting workflows, making it useful for large-scale API testing and QA activities.

### Key Advantages

* Lightweight
* Fast
* Open Source
* Developer Friendly
* QA Focused
* Easy Postman Integration
* Designed for Future Automation


## Installation

Clone repository:

```bash
git clone https://github.com/YOUR_USERNAME/apiforge.git

cd apiforge
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

Linux / Mac

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run Application

Start FastAPI server:

```bash
uvicorn src.app:app --reload
```

Application URL:

```text
http://127.0.0.1:8000
```

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

---

## API Endpoint

### Generate Scenarios

```http
POST /generate
```

---

## Example Request

```json
{
  "routes": [
    {
      "url": "https://api.example.com/users",
      "method": "GET"
    }
  ],

  "headers": {
    "Authorization": "Bearer token"
  },

  "bodies": [
    {
      "name": "Ali"
    }
  ],

  "queries": [
    {
      "page": 1
    }
  ]
}
```

---

## Example Response

```json
{
  "generated_requests": 1,
  "curl_file": "output/curls.sh",
  "postman_file": "output/postman_collection.json"
}
```

---

## Generated CURL Example

```bash
curl --location --request GET \
'https://api.example.com/users?page=1' \
--header 'Authorization: Bearer token'
```

---

## Generated Files

### CURL Script

```text
output/curls.sh
```

### Postman Collection

```text
output/postman_collection.json
```

---

## How Scenario Generation Works

ApiForge generates combinations based on:

```text
Routes × Bodies × Queries
```

Example:

```text
3 Routes
2 Bodies
4 Queries
```

Generated Requests:

```text
3 × 2 × 4 = 24
```

---

## Roadmap

### v0.2.0

* Route Specific Headers
* Custom Output Names
* Environment Configuration

### v0.3.0

* CURL Runner
* Retry Mechanism
* Execution Logs

### v0.4.0

* JSON Reports

### v0.5.0

* HTML Reports

### v0.6.0

* Statistics Engine

### v0.7.0

* Cartesian Product Testing

### v1.0.0

Complete API Testing Platform

* Scenario Generation
* CURL Execution
* Report Generation
* API Analytics
* Test Automation

---

## Contributing

Contributions, issues, and feature requests are welcome.

Feel free to open an issue or submit a pull request.

---

## License

MIT License

---

## Author

Ali Bahrampour

GitHub: https://github.com/alibahrampour
