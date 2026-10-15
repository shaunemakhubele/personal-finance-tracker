# Personal Finance Tracker

A web-based personal finance application built with **Python, Flask, and SQLite**. The application helps users record income and expenses, monitor their financial balance, manage transactions, and set monthly spending budgets.

This project was developed to practise backend web development, database management, form validation, and automated testing.

## Features

- **Dashboard:** View total income, total expenses, and current balance.
- **Transaction management:** Add and view income and expense transactions.
- **Delete transactions:** Remove transactions when needed.
- **Input validation:** Validate transaction descriptions, categories, amounts, dates, and transaction types.
- **Monthly budgets:** Create spending budgets for different categories and months.
- **Budget tracking:** Compare expenses against monthly budget limits.
- **Persistent storage:** Store transactions and budgets in an SQLite database.
- **Automated testing:** Use pytest to verify application behaviour.

## Technology Stack

- **Language:** Python
- **Web framework:** Flask
- **Database:** SQLite
- **Frontend:** HTML, CSS, Jinja templates
- **Testing:** pytest
- **Version control:** Git and GitHub

## Project Structure

```text
personal-finance-tracker/
├── app/
│   ├── __init__.py
│   ├── db.py
│   ├── routes.py
│   ├── static/
│   │   └── style.css
│   └── templates/
│       ├── base.html
│       ├── dashboard.html
│       ├── transactions.html
│       └── budgets.html
├── tests/
│   └── test_app.py
├── src/
│   └── main.py
├── instance/
│   └── finance.db
├── run.py
├── requirements.txt
├── .gitignore
└── README.md
```

*Note: The database file is generated locally when the application runs. It should not be committed to the repository.*

## Getting Started

### Prerequisites

Install Python 3.10 or newer and Git.

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-GITHUB-USERNAME/personal-finance-tracker.git
cd personal-finance-tracker
```

Replace `YOUR-GITHUB-USERNAME` with your GitHub username.

### 2. Create a virtual environment

**Windows PowerShell:**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell activation is blocked, you can run the environment's Python executable directly instead.

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Start the application

```bash
python run.py
```

Open your browser and visit:

http://127.0.0.1:5000

## Running Tests

Run the automated test suite from the project root:

```bash
python -m pytest -q
```

The tests cover key application behaviour, including page loading, adding transactions, calculating balances, rejecting invalid amounts, deleting transactions, and saving budgets.

## Learning Outcomes

This project demonstrates practical experience with:

- Building a web application using Flask.
- Organising code into modules and routes.
- Designing and querying a relational SQLite database.
- Handling form submissions and validating user input.
- Performing database create, read, and delete operations, as well as budget updates.
- Writing automated tests with pytest.
- Managing source code with Git and GitHub.

## Future Improvements

Potential future enhancements include:

- User registration and secure authentication.
- Charts showing income and spending trends.
- Exporting transactions to CSV.
- More detailed financial reports.
- Improved security protections for deployment.

## Project Status

**Development version.** Core transaction management, financial summaries, monthly budgets, and automated tests have been implemented. Further improvements may be made as the project develops.

## Author

**Shaune Makhubele**

GitHub: https://github.com/YOUR-GITHUB-USERNAME

---

Built as a software development portfolio project to demonstrate Python, Flask, database, and testing skills.