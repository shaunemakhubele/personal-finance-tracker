Personal Finance Tracker

A simple web application for keeping track of personal finances. Built with Python, Flask, and SQLite, it lets users record income and expenses, check their current balance, and set monthly budgets for different spending categories.

I built this project to practise backend development, working with databases, handling user input, and writing automated tests.

Features
Dashboard: See total income, total expenses, and your current balance.
Transactions: Add income and expense records and view existing transactions.
Delete transactions: Remove transactions you no longer need.
Input validation: Check transaction details such as descriptions, categories, amounts, dates, and types.
Monthly budgets: Set spending limits for different categories each month.
Budget tracking: See how your spending compares with your budget.
SQLite database: Keep transaction and budget data saved between sessions.
Automated tests: Use pytest to check that the main features work as expected.
Built With
Python
Flask
SQLite
HTML and CSS
Jinja templates
pytest
Git and GitHub
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


The SQLite database is created locally when the application runs, so the database file doesn't need to be committed to GitHub.

Getting Started
Requirements

You'll need Python 3.10 or newer and Git installed on your machine.

1. Clone the repository
git clone https://github.com/shaunemakhubele/personal-finance-tracker.git
cd personal-finance-tracker

2. Create a virtual environment

Using a virtual environment keeps the project's dependencies separate from other Python projects.

Windows PowerShell:

python -m venv .venv
.\.venv\Scripts\Activate.ps1


If PowerShell prevents activation, you can still run Python directly from the virtual environment.

3. Install the dependencies
python -m pip install -r requirements.txt

4. Run the application
python run.py


Once the server starts, open your browser and go to:

http://127.0.0.1:5000

Running the Tests

To run the test suite, use:

python -m pytest -q


The tests cover things like loading pages, adding and deleting transactions, calculating balances, handling invalid amounts, and saving budgets.

What I Learned

Working on this project gave me practical experience with:

Building a web application with Flask.
Organising application code into separate modules.
Using SQLite to store and retrieve data.
Handling form submissions and validating user input.
Implementing database operations for transactions and budgets.
Writing tests with pytest.
Using Git and GitHub to manage a project.
What's Next?

There are a few things I'd like to add as the project develops:

User accounts and secure login.
Charts to make spending patterns easier to understand.
CSV export for transactions.
More detailed financial reports.
Additional security improvements before deployment.
Project Status

The application is a work in progress. The main features, including transaction management, balance calculations, monthly budgets, and automated tests, are in place. There's still room to improve the functionality and overall user experience.

Author

Shaune Makhubele

GitHub: shaunemakhubele
