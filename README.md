# Outreachy 30: Addressing the new Lusophone technological wishlist proposals

This repository contains the completed tasks for [T386128](https://phabricator.wikimedia.org/T386128), as part of the Outreachy Round 30 internship. The two tasks are located in separate subdirectories:

- **Task 1**: `Task_1/Task 1 - Intern.html`A script that displays the creation dates of various Lusophone-related Wikipedia articles in a formatted manner.
- **Task 2**: `Task_2/status_code_getter.py` and `Task 2 - Intern.csv`
  A Python script that checks the HTTP status of URLs listed in the CSV file and logs detailed errors in `error_details.txt`.

## Run Guide

Follow these steps to set up and run the project:

### 1. Clone the repository

```bash
git clone https://github.com/22f1001635/wishlist-proposal
cd wishlist-proposal
```

### 2. Create and activate a virtual environment

**On Windows:**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**On macOS/Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Task 2

Make sure you are in the root directory and execute:

```bash
python ./Task_2/status_code_getter.py
```

The script will process the CSV file and generate an `error_details.txt` log in the `Task_2` folder for any URLs that failed.

### 5. View Task 1

Open the HTML file directly in your browser:

```
Task_1/Task 1 - Intern.html
```

---

### Author

Saksham Sirohi
Contributions for Outreachy 30 under Wikimedia.
