import pytest

from src.account_validator import validate_account
from src.file_utils import load_json


INVALID_ACCOUNT_DATA = load_json("invalid_accounts.json")

@pytest.mark.parametrize(
    "test_case",
    INVALID_ACCOUNT_DATA["invalid_accounts"],
    ids=lambda test_case: test_case["test_id"]
)
def test_invalid_account(test_case):
    account = test_case["account"]
    expected_error = test_case["expected_error"]

    with pytest.raises(ValueError) as exception:
        validate_account(account)

    assert str(exception.value) == expected_error