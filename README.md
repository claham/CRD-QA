# CRD QA - Rebalancing APP Tests

This is a testing framework meant to test the account securities rebalancing application.

## Architecture

The project follows a simple data-driven testing approach. 
Account-specific data and expected results are kept in external JSON files, while the Python implementation and tests remain generic.

* `data/` - account input data, expected results and invalid test data
* `src/` - rebalancing logic, account validation and file utilities
* `tests/` - pytest automated test suite

## Test Approach

The automated tests validate:

* The trade action for each security
* the calculated number of shares
* invalid account data and input validation

Tests are parameterized using the external JSON data

## Assumptions

* Fractional shares are supported.
* The account is assumed to be 100% invested.
* Transaction fees, taxes and market price changes during rebalancing are out of scope.
* Testing is focused on the backend rebalancing logic.
## Notes

* Target variance is not saved in the test data because it can be calculated:

  `target variance = current_percent - target_percent`

* `Decimal` is used for calculations to avoid floating-point precision issues.

* The requirements do not define fractional-share precision or a rounding policy. The automated tests therefore use a small comparison tolerance. The acceptable precision/tolerance should be defined by the product owner for a production system.
* The automation will be executed in CI/CD.

## Tests Execution

Install dependencies:

`pip install -r requirements.txt`

Run all tests:

`pytest -v`
