# Rebalancing Account ABC

Account ABC has $100,000 in total assets and is 100% vested.

The target allocation for each security is 20%, so each security should have a target value of $20,000.

**Calculation:**

`trade value = target value - current value`

`shares = |trade value| / unit price`

## Results

| Security | Target % | Current % | Target Variance | Unit Price | Output - Number of Shares to Buy/Sell |
| -------- | -------: | --------: | --------------: | ---------: | ------------------------------------- |
| IBM      |       20 |        10 |             -10 |       $150 | **BUY 66.666667**                     |
| MSFT     |       20 |        20 |               0 |        $90 | **0**                                 |
| ORCL     |       20 |        30 |              10 |       $220 | **SELL 45.454545**                    |
| AAPL     |       20 |        20 |               0 |       $450 | **0**                                 |
| HD       |       20 |        20 |               0 |        $70 | **0**                                 |

## What do we have to do to get to zero target variance?

* Buy **66.666667 shares of IBM**
* Sell **45.454545 shares of ORCL**
* No trade is required for MSFT, AAPL or HD.
