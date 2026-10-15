## Personal Finance Tracker

A personal finance web application built with Python, Flask, and SQLite. It allows users to keep track of their income and expenses, check their current balance, and set monthly budgets for different spending categories.

I built this project to practise backend web development, working with databases, validating user input, and writing automated tests.

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

*Note: The SQLite database is created locally when the application runs. The database file should not be committed to the repository.*

## Getting Started
### Prerequisites

Make sure you have Python 3.10 or newer and Git installed.
```
1. Clone the repository
git clone https://github.com/shaunemakhubele/personal-finance-tracker.git
cd personal-finance-tracker
```
### 2. Create a virtual environment

**Windows PowerShell:**
```
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Linux or macOS:

python3 -m venv .venv
source .venv/bin/activate


A virtual environment keeps the project's dependencies separate from other Python projects.

### 3. Install dependencies
python -m pip install -r requirements.txt

### 4. Start the application

Run the following command from the project directory:

python run.py


Once the application is running, open your browser and visit:

http://127.0.0.1:5000

## Running Tests

Run the test suite from the project root using:

python -m pytest -q


The tests check that pages load correctly, transactions can be added and deleted, balances are calculated correctly, invalid amounts are rejected, and budgets can be saved.

## Learning Outcomes

-Building this project gave me practical experience with:

-Developing a web application using Flask.
-Organising Python code into modules and routes.
-Using SQLite to store and retrieve financial data.
-Handling form submissions and validating user input.
-Implementing database operations for transactions and budgets.
-Writing automated tests with pytest.
-Using Git and GitHub to manage source code.

## Future Improvements

Some features I would like to add in the future include:

-User registration and login.
-Charts to show income and spending trends.
-Exporting transactions to CSV.
-More detailed financial reports.
-Additional security improvements before deployment.
-Project Status

The project is still under development. The main features, including transaction management, balance calculations, monthly budgets, and automated tests, are implemented. I plan to continue improving the application and adding features over time.

## Author

Shaune Makhubele

GitHub: https://github.com/shaunemakhubele

A personal project built to develop my skills in Python, Flask, database management, and software testing.
