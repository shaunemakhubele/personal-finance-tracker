
import pytest
from app import create_app
from app.db import get_summary, get_transactions


@pytest.fixture
def app(tmp_path):
    test_app = create_app({
        "TESTING": True,
        "SECRET_KEY": "test-secret-key",
        "DATABASE": str(tmp_path / "test_finance.db"),
    })
    yield test_app


@pytest.fixture
def client(app):
    return app.test_client()


def test_dashboard_loads(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Financial Dashboard" in response.data


def test_transactions_page_loads(client):
    response = client.get("/transactions")
    assert response.status_code == 200
    assert b"Add Transaction" in response.data


def test_add_income_updates_summary(app, client):
    response = client.post("/transactions/add", data={
        "transaction_type": "income",
        "description": "Salary",
        "category": "Work",
        "amount": "15000",
        "transaction_date": "2026-10-01",
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b"Transaction added successfully" in response.data

    with app.app_context():
        summary = get_summary()
        assert summary["total_income"] == pytest.approx(15000)
        assert summary["total_expenses"] == pytest.approx(0)
        assert summary["balance"] == pytest.approx(15000)


def test_expense_updates_balance(app, client):
    client.post("/transactions/add", data={
        "transaction_type": "income",
        "description": "Salary",
        "category": "Work",
        "amount": "15000",
        "transaction_date": "2026-10-01",
    })

    client.post("/transactions/add", data={
        "transaction_type": "expense",
        "description": "Groceries",
        "category": "Food",
        "amount": "850",
        "transaction_date": "2026-10-02",
    })

    with app.app_context():
        summary = get_summary()
        assert summary["total_expenses"] == pytest.approx(850)
        assert summary["balance"] == pytest.approx(14150)


def test_invalid_amount_is_rejected(client):
    response = client.post("/transactions/add", data={
        "transaction_type": "expense",
        "description": "Invalid expense",
        "category": "Food",
        "amount": "-100",
        "transaction_date": "2026-10-01",
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b"Enter an amount greater than zero" in response.data


def test_delete_transaction(app, client):
    client.post("/transactions/add", data={
        "transaction_type": "expense",
        "description": "Test purchase",
        "category": "Shopping",
        "amount": "100",
        "transaction_date": "2026-10-03",
    })

    with app.app_context():
        transactions = get_transactions()
        transaction_id = transactions[0]["id"]

    response = client.post(
        f"/transactions/{transaction_id}/delete",
        follow_redirects=True,
    )

    assert response.status_code == 200

    with app.app_context():
        assert get_transactions() == []


def test_budget_can_be_saved(client):
    response = client.post("/budgets", data={
        "category": "Food",
        "monthly_limit": "2000",
        "month": "2026-10",
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b"Budget saved successfully" in response.data
