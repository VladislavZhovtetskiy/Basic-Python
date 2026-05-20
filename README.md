# Core Python: Practical Tasks & Projects

This repository tracks my journey in learning Python fundamentals. It serves as a structured collection of programs, exercises, and algorithmic challenges, ranging from basic syntax to object-oriented logic and exceptions.

---

Each subdirectory focuses on a specific Python concept or a standalone practical problem. Click on the project name to view its detailed documentation and source code:

| Project Directory                          | Core Topic / Concepts Applied                   |    Status     | Description                                              |
| :----------------------------------------- | :---------------------------------------------- | :-----------: | :------------------------------------------------------- |
| [combinatorics_task](./combinatorics_task) | Math algorithms, Input Validation, Loops        |    `Done`     | Calculates possible combinations for selecting students. |
| [water_balance](./water_balance)   | Encapsulation, Scopes, Arguments, Return values | `Done` | Calculate necessery volume for 1 human.              |
| [geometry_problem](./geometry_problem)   | `math` module, Type casting, Exception handling |   `Done`   | Computes geometric parameters (e.g., volume and area).        |
| [nutrients](./nutrients)   | Type casting, Exception handling, Dictionary |   `Done`   | Daily kilocalorie requirement calculated using the Mifflin-St Jeor formula.        |
| [random_password](./random_password)   | Dictionary, Lists, For loop, Random |   `Done`   | Easy password generator for terminal.        |
| [students_avarage](./students_avarage)   | Try\except, File Hadling, Dictionary, List, Const |   `Done`   | Script that calculate avarage score from file.        |


---

## Global Installation & Setup

All projects in this repository are managed under a single unified virtual environment. Follow these steps to set up and run any script locally:

### 1. Clone the Repository

```bash
git clone github.com
cd A-combinatorics-problem
```

### 2. Set Up the Virtual Environment

Create and activate the environment based on your Operating System:

- **Windows (PowerShell):**
  ```powershell
  python -m venv .venv
  .venv\Scripts\Activate.ps1
  ```
- **Linux / macOS:**
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```

### 3. Install Shared Dependencies

Install any required external packages (if specified in the project folders):

```bash
pip install -r requirements.txt
```

### 4. How to Execution Any Task

You can execute any script directly from the root directory by specifying its path:

```bash
python combinatorics_task/task_class.py
```

---

## Learning Roadmap & Goals

- [x] Implement robust user input validation loops.
- [x] Isolate system files (`.venv`, `pyvenv.cfg`) using clean global `.gitignore`.
- [ ] Master Python exceptions (`try/except/finally`) for mathematical edge cases.
- [ ] Explore data visualization using external libraries (e.g., matplotlib).
