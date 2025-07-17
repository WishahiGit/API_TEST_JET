# 📚 Library Management API – Automation Testing


## Overview
This project provides automated API testing for a RESTful Library Management system using Python, Pytest, and the Requests library.
It covers CRUD operations (Create, Read, Update, Delete) as well as book lending and returning features.
Test scenarios are data-driven, loaded from an Excel sheet containing both positive and negative cases.


## 📁 Structure
- tests/test_api_books.py – Automated API tests for books and users (create, book list,users, update, delete, borrow, return)

- apis/BooksAPI.py – Abstraction layer for all book/user-related API interactions

- apis/BaseRequest.py – Generic request handler for all HTTP methods (GET, POST, PUT, DELETE)

- utils/load_data.py – Excel-based test data loader with action-based filtering

- utils/response_validators.py – Common field validations for all API responses (id, message, etc.)

- utils/Allure_Attachments.py – Optional Allure integration for attaching logs/screenshots

- test_data/test_cases_BOOKS.xlsx – All test scenarios including expected results (positive & negative)

- tests/BaseTest.py – Base test class for setup/teardown and shared logic

- tests/conftest.py – Shared fixtures (if needed) and configuration for pytest

- pytest.ini – Pytest runtime configuration (markers, options)

- requirements.txt – Python dependencies list


## 🔧 Technologies/Features

- Built API automation using the AOM (API Object Model) architecture
- Unified, data-driven test execution (positive & negative flows)
- Allure integration for detailed reporting
- Python 3.x
- Pytest
- Requests

---

## 🐞 Bugs / Known Issues

❌ No critical or blocking bugs were discovered during the test execution.  
⚠️ The current API is hosted in a demo environment with **minimal input validation**.  
🧪 As a result, many negative test cases — which should fail in a real-world system — return `200 OK` or succeed unexpectedly.  
ℹ️ This includes scenarios like updating a book with empty fields (see Postman screenshot). Despite empty title and author, the system accepted the request and returned a valid response.

---

## ⚠️ About Negative Testing Limitations

While this project includes a wide range of negative test cases (e.g., missing fields, empty strings, invalid types), the backend does not enforce validation rules.
For that reason, test cases that are expected to fail may pass based on the current API behavior. The automation reflects this by still running these tests but logging them as “negative” with expected=False in the Excel.


## 📑 Test Coverage Summary

The file `test_data/test_cases_BOOKS.xlsx` contains all test scenarios divided by action type (create, update, delete, borrow, return, get).

✅ A total of **20 test scenarios** were executed:
- **13 Positive** – Expected to succeed → ✅ All passed
- **7 Negative** – Expected to fail (e.g., empty title, invalid ID, negative values) → ✅ All behaved as expected (`expected=False`, result matched)

⚠️ Note: In most cases, the demo backend **responds correctly** to negative input when marked appropriately in the Excel.  
          However, **Update scenarios with empty fields were not labeled as `expected=False`**, even though the backend still accepted them. This edge case was documented but not flagged as a failure.

## ❗ Importance of Negative Test Scenarios

Negative test scenarios are essential to ensure the robustness and reliability of any production-grade system.  
They validate that the system **correctly rejects invalid input** and **enforces business rules**.

Although this demo API allows operations with missing or malformed data (due to relaxed validation), all negative scenarios were executed and verified to:

- Ensure coverage of edge cases and improper usage
- Confirm that the automation infrastructure supports both success and failure paths
- Demonstrate that the system **should** reject such inputs in a real-world environment

**Negative scenarios included:**
- Empty or missing required fields (title, author)
- Invalid book IDs (non-existent or malformed)
- Attempting to borrow or return books with incorrect data
- Sending logically invalid values (e.g., negative booleans, empty strings)

These tests are crucial to prevent:
- Silent failures or data corruption
- Unexpected application behavior
- Security or integrity issues in production systems

## 📦 Prerequisites

Before starting, make sure the following are installed on your machine:

- [Git](https://git-scm.com/downloads)
- [Python 3.8+](https://www.python.org/downloads/)
- pip (comes with Python)
- Allure CLI (see installation below)

Additionally, make sure to clone and run the demo **Library Management API server** locally:
- bash
- git clone https://github.com/LBS720/library-management-api.git
- cd library-management-api/python
- python app.py

ℹ️ The server should be running at http://localhost:5000
All test cases are based on this local environment.




## 🛠️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/WishahiGit/Api-Python-Pytest.git
cd Api-Python-Pytest



### 2️⃣ Set up Virtual Environment 

```bash
python -m venv .venv
.venv\Scripts\activate     # On Windows
# OR
source .venv/bin/activate  # On Mac/Linux
```

### 3️⃣ Install Dependencies
 Install all required Python packages:
```bash
pip install -r requirements.txt
```

---

## 🚀 How to Run Tests

### Option 1: From Terminal inside the Project
Run all tests and generate Allure results with a single command:
```bash
pytest --alluredir=allure-results
```

### Option 2: From External Command Line (CMD / PowerShell)

```bash
cd path\to\project\directory
.venv\Scripts\activate
pytest --alluredir=allure-results
```

---

## 🧪 Run Specific Tests


API only:

```bash
pytest -m api --alluredir=allure-results
```

---

## 📊 Generate Allure Report

```bash
allure serve allure-results
```

---


## Author

Created by Saber Wishahi

