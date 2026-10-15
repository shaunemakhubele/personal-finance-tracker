Personal Finance Tracker

A personal finance web application built with Python, Flask, and SQLite. The application allows users to record income and expenses, view their financial balance, and manage monthly budgets by category.

This project was built to practise web development, database management, input validation, and automated testing.

Table of Contents
Features
Technologies Used
Project Structure
Installation and Setup
Running the Application
Running Tests
Future Improvements
Author
Features
Dashboard: Displays total income, total expenses, and current balance.
Transaction Management: Add and view income and expense transactions.
Transaction Deletion: Remove existing transactions.
Input Validation: Validates transaction descriptions, categories, amounts, dates, and types.
Monthly Budgets: Set spending limits for different categories.
Budget Tracking: Compare actual spending against monthly budgets.
Data Persistence: Store transactions and budgets in an SQLite database.
Automated Testing: Test application functionality using pytest.
Technologies Used
Technology	Purpose
Python	Application logic
Flask	Web framework
SQLite	Database
HTML and CSS	Frontend and styling
Jinja	HTML templating
pytest	Automated testing
Git and GitHub	Version control
Project Structure
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


The SQLite database is stored locally and generated when the application runs. The database file should not be committed to version control.

Installation and Setup
Prerequisites

Make sure the following are installed:

Python 3.10 or newer
Git
1. Clone the repository
git clone https://github.com/shaunemakhubele/personal-finance-tracker.git
cd personal-finance-tracker

2. Create a virtual environment

A virtual environment keeps the project's Python dependencies separate from other projects.

Windows (PowerShell):
