from decimal import Decimal

def validate_account(account):

    total_assets = Decimal(str(account["total_assets"]))

    if total_assets <= 0:
        raise ValueError("Total assets must be greater than zero")

    securities = account["securities"]

    if not securities:
        raise ValueError("Account must contain at least one security")

    total_target_percent = Decimal("0")
    total_current_percent = Decimal("0")

    for security in securities:
        target_percent = Decimal(str(security["target_percent"]))
        current_percent = Decimal(str(security["current_percent"]))
        unit_price = Decimal(str(security["unit_price"]))

        if unit_price <= 0:
            raise ValueError(
                f"{security['symbol']}: unit price must be greater than zero"
            )

        if not Decimal("0") <= target_percent <= Decimal("100"):
            raise ValueError(
                f"{security['symbol']}: target percentage must be between 0 and 100"
            )

        if not Decimal("0") <= current_percent <= Decimal("100"):
            raise ValueError(
                f"{security['symbol']}: current percentage must be between 0 and 100"
            )

        total_target_percent += target_percent
        total_current_percent += current_percent

    if total_target_percent != Decimal("100"):
        raise ValueError("Target percentages must total 100")

    if total_current_percent != Decimal("100"):
        raise ValueError("Current percentages must total 100")