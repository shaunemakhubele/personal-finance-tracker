
import math
from datetime import date
from flask import (
    Blueprint, render_template, request,
    redirect, url_for, flash,
)
from app.db import (
    get_transactions, get_summary, add_transaction,
    delete_transaction, get_budgets, save_budget,
)

main = Blueprint("main", __name__)


def valid_month(value):
    try:
        parsed = date.fromisoformat(value + "-01")
        return parsed.strftime("%Y-%m") == value
    except (ValueError, TypeError):
        return False


@main.route("/")
def dashboard():
    return render_template(
        "dashboard.html",
        summary=get_summary(),
        transactions=get_transactions()[:5],
    )


@main.route("/transactions")
def transactions():
    return render_template(
        "transactions.html",
        transactions=get_transactions(),
        today=date.today().isoformat(),
    )


@main.route("/transactions/add", methods=["POST"])
def add_transaction_route():
    transaction_type = request.form.get("transaction_type", "")
    description = request.form.get("description", "").strip()
    category = request.form.get("category", "").strip()
    amount_text = request.form.get("amount", "").strip()
    transaction_date = request.form.get("transaction_date", "")

    if transaction_type not in ("income", "expense"):
        flash("Choose income or expense.", "error")
        return redirect(url_for("main.transactions"))

    if not description or len(description) > 100:
        flash("Description is required (maximum 100 characters).", "error")
        return redirect(url_for("main.transactions"))

    if not category or len(category) > 50:
        flash("Category is required (maximum 50 characters).", "error")
        return redirect(url_for("main.transactions"))

    try:
        amount = float(amount_text)
        if not math.isfinite(amount) or amount <= 0:
            raise ValueError
    except (ValueError, TypeError):
        flash("Enter an amount greater than zero.", "error")
        return redirect(url_for("main.transactions"))

    try:
        parsed_date = date.fromisoformat(transaction_date)
        if parsed_date.isoformat() != transaction_date:
            raise ValueError
    except (ValueError, TypeError):
        flash("Enter a valid transaction date.", "error")
        return redirect(url_for("main.transactions"))

    add_transaction(
        transaction_type, description, category,
        amount, transaction_date,
    )
    flash("Transaction added successfully!", "success")
    return redirect(url_for("main.transactions"))


@main.route("/transactions/<int:transaction_id>/delete", methods=["POST"])
def delete_transaction_route(transaction_id):
    if delete_transaction(transaction_id):
        flash("Transaction deleted.", "success")
    else:
        flash("Transaction not found.", "error")
    return redirect(url_for("main.transactions"))


@main.route("/budgets", methods=["GET", "POST"])
def budgets():
    current_month = date.today().strftime("%Y-%m")

    if request.method == "POST":
        category = request.form.get("category", "").strip()
        limit_text = request.form.get("monthly_limit", "")
        month = request.form.get("month", current_month)

        if not category or len(category) > 50:
            flash("Enter a category (maximum 50 characters).", "error")
            return redirect(url_for("main.budgets"))

        if not valid_month(month):
            flash("Choose a valid budget month.", "error")
            return redirect(url_for("main.budgets"))

        try:
            monthly_limit = float(limit_text)
            if not math.isfinite(monthly_limit) or monthly_limit <= 0:
                raise ValueError
        except (ValueError, TypeError):
            flash("Budget must be greater than zero.", "error")
            return redirect(url_for("main.budgets"))

        save_budget(category, monthly_limit, month)
        flash("Budget saved successfully!", "success")
        return redirect(url_for("main.budgets") + "?month=" + month)

    month = request.args.get("month", current_month)
    if not valid_month(month):
        month = current_month

    return render_template(
        "budgets.html",
        budgets=get_budgets(month),
        month=month,
    )
