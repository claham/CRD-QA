import pytest
from decimal import Decimal
from src.file_utils import load_json
from src.rebalancer import rebalance_account


def get_account_by_id(data, account_id):
    """
    Find an account in a JSON dataset by account ID.
    """
    for account in data["accounts"]:
        if account["account_id"] == account_id:
            return account

    raise ValueError(f"Account '{account_id}' not found")


ACCOUNT_DATA = load_json("accounts.json")
EXPECTED_DATA = load_json("expected_results.json")

SHARE_COMPARISON_TOLERANCE = Decimal("0.000001")

@pytest.mark.parametrize(
    "account",
    ACCOUNT_DATA["accounts"],
    ids=lambda account: account["account_id"]
)
def test_rebalancing(account):
    """
    Verify that the calculated trades match the expected trades for each account.
    """

    account_id = account["account_id"]

    expected_account = get_account_by_id(EXPECTED_DATA,account_id)

    actual_trades = rebalance_account(account)
    expected_trades = expected_account["expected_trades"]

    assert len(actual_trades) == len(expected_trades)

    actual_by_symbol = {
        trade["symbol"]: trade
        for trade in actual_trades
    }

    for expected_trade in expected_trades:

        symbol = expected_trade["symbol"]
        assert symbol in actual_by_symbol

        actual_trade = actual_by_symbol[symbol]
        assert actual_trade["action"] == expected_trade["action"], (
            f"{symbol}: expected action {expected_trade['action']}, "
            f"but got {actual_trade['action']}"
        )

        expected_shares = Decimal(str(expected_trade["shares"]))
        actual_shares = actual_trade["shares"]
        assert abs(actual_shares - expected_shares) <= SHARE_COMPARISON_TOLERANCE, (
            f"{symbol}: expected {expected_shares} shares, "
            f"but got {actual_shares}"
        )
