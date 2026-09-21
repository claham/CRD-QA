from decimal import Decimal
from src.account_validator import validate_account

def calculate_trade(total_assets, security):
    """
    Calculate the trade required to move a security
    from its current allocation to its target allocation.
    """

    total_assets = Decimal(str(total_assets))
    target_percent = Decimal(str(security["target_percent"]))
    current_percent = Decimal(str(security["current_percent"]))
    unit_price = Decimal(str(security["unit_price"]))

    target_value = total_assets * target_percent / Decimal("100")
    current_value = total_assets * current_percent / Decimal("100")

    trade_value = target_value - current_value

    if trade_value > 0:
        action = "BUY"
    elif trade_value < 0:
        action = "SELL"
    else:
        action = "NONE"

    shares = abs(trade_value / unit_price)

    return {
        "symbol": security["symbol"],
        "action": action,
        "shares": shares
    }


def rebalance_account(account):
    """
    Calculate the required trades for all securities in an account
    """
    validate_account(account)

    trades = []

    for security in account["securities"]:
        trade = calculate_trade(account["total_assets"],security)
        trades.append(trade)

    return trades