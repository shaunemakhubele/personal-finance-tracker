
import sqlite3
from datetime import date
from flask import current_app


def get_connection():
    connection = sqlite3.connect(current_app.config["DATABASE"])
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    return connection


def init_db(app):
    with app.app_context():
        connection = get_connection()
        try:
            connection.executescript("""
                CREATE TABLE IF NOT EXISTS transactions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    transaction_type TEXT NOT NULL
                        CHECK (transaction_type IN ('income', 'expense')),
                    description TEXT NOT NULL,
                    category TEXT NOT NULL,
                    amount REAL NOT NULL CHECK (amount > 0),
                    transaction_date TEXT NOT NULL
                );

                CREATE TABLE IF NOT EXISTS budgets (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    category TEXT NOT NULL,
                    monthly_limit REAL NOT NULL CHECK (monthly_limit > 0),
                    month TEXT NOT NULL,
                    UNIQUE(category, month)
                );
            """)
            connection.commit()
        finally:
            connection.close()


def get_transactions():
    connection = get_connection()
    try:
        return connection.execute("""
            SELECT * FROM transactions
            ORDER BY transaction_date DESC, id DESC
        """).fetchall()
    finally:
        connection.close()


def get_summary():
    connection = get_connection()
    try:
        row = connection.execute("""
            SELECT
                COALESCE(SUM(CASE
                    WHEN transaction_type = 'income' THEN amount
                    ELSE 0 END), 0) AS total_income,
                COALESCE(SUM(CASE
                    WHEN transaction_type = 'expense' THEN amount
                    ELSE 0 END), 0) AS total_expenses
            FROM transactions
        """).fetchone()

        income = row["total_income"]
        expenses = row["total_expenses"]

        return {
            "total_income": income,
            "total_expenses": expenses,
            "balance": income - expenses,
        }
    finally:
        connection.close()


def add_transaction(
    transaction_type, description, category, amount, transaction_date
):
    connection = get_connection()
    try:
        connection.execute("""
            INSERT INTO transactions (
                transaction_type, description, category,
                amount, transaction_date
            ) VALUES (?, ?, ?, ?, ?)
        """, (
            transaction_type, description, category,
            amount, transaction_date,
        ))
        connection.commit()
    finally:
        connection.close()


def delete_transaction(transaction_id):
    connection = get_connection()
    try:
        cursor = connection.execute(
            "DELETE FROM transactions WHERE id = ?",
            (transaction_id,),
        )
        connection.commit()
        return cursor.rowcount > 0
    finally:
        connection.close()


def get_budgets(month=None):
    month = month or date.today().strftime("%Y-%m")
    connection = get_connection()
    try:
        return connection.execute("""
            SELECT
                b.id,
                b.category,
                b.monthly_limit,
                b.month,
                COALESCE((
                    SELECT SUM(t.amount)
                    FROM transactions t
                    WHERE t.transaction_type = 'expense'
                      AND LOWER(t.category) = LOWER(b.category)
                      AND SUBSTR(t.transaction_date, 1, 7) = b.month
                ), 0) AS spent
            FROM budgets b
            WHERE b.month = ?
            ORDER BY b.category
        """, (month,)).fetchall()
    finally:
        connection.close()


def save_budget(category, monthly_limit, month):
    connection = get_connection()
    try:
        connection.execute("""
            INSERT INTO budgets (category, monthly_limit, month)
            VALUES (?, ?, ?)
            ON CONFLICT(category, month)
            DO UPDATE SET monthly_limit = excluded.monthly_limit
        """, (category, monthly_limit, month))
        connection.commit()
    finally:
        connection.close()
