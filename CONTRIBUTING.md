# Contributing to ApiForge

First of all, thank you for considering contributing to ApiForge.

ApiForge is an open-source API Testing Platform focused on generating, executing, and analyzing API test scenarios. Contributions from the community help make the project better for everyone.

---

## Ways to Contribute

You can contribute in several ways:

* Reporting bugs
* Suggesting new features
* Improving documentation
* Writing tests
* Refactoring code
* Implementing roadmap features
* Improving performance

---

## Development Setup

### Clone the Repository

```bash
git clone https://github.com/your-username/apiforge.git
cd apiforge
```

### Create Virtual Environment

```bash
python -m venv venv
```

Linux/Mac:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

```bash
python app.py
```

---

## Running Tests

```bash
pytest tests -v
```

---

## Pull Request Process

1. Fork the repository.
2. Create a feature branch.

```bash
git checkout -b feature/my-feature
```

3. Implement your changes.
4. Add or update tests.
5. Ensure all tests pass.
6. Commit your changes.

```bash
git commit -m "Add new feature"
```

7. Push your branch.

```bash
git push origin feature/my-feature
```

8. Open a Pull Request.

---

## Coding Standards

* Follow PEP 8 guidelines.
* Write clear and maintainable code.
* Use meaningful variable and function names.
* Add docstrings where appropriate.
* Include tests for new functionality.

---

## Commit Message Guidelines

Good examples:

```text
feat: add postman collection export
fix: handle empty request body
docs: update roadmap
test: add curl builder tests
```

---

## Roadmap Contributions

Current roadmap items include:

* CURL Runner
* HTML Report Generator
* JSON Report Generator
* Result Analytics Engine
* Cartesian Product Testing
* Per-Endpoint Header Configuration

Contributions in these areas are especially welcome.

---

Thank you for helping improve ApiForge.
