# Manual Tests

These manual tests are intended as a quick sanity check when a new version of the rebalancer is released.

They focus on verifying that the core rebalancing functionality is working as expected. More detailed calculation, validation, negative, and regression scenarios are covered by the automated pytest suite.

---

## ST01 – Buy Required

**Scenario:** Verify that a BUY trade is generated when the current allocation is lower than the target allocation.

**Test Steps:**

1. Load an account with a security where the target allocation is 20% and the current allocation is 10%.
2. Run the rebalancer.
3. Review the generated trade.

**Expected Result:**
A BUY action is generated with a positive number of shares.

---

## ST02 – Sell Required

**Scenario:** Verify that a SELL trade is generated when the current allocation is higher than the target allocation.

**Test Steps:**

1. Load an account with a security where the target allocation is 20% and the current allocation is 30%.
2. Run the rebalancer.
3. Review the generated trade.

**Expected Result:**
A SELL action is generated with a positive number of shares.

---

## ST03 – No Trade Required

**Scenario:** Verify that no trade is generated when the current allocation matches the target allocation.

**Test Steps:**

1. Load an account with a security where the target allocation is 20% and the current allocation is 20%.
2. Run the rebalancer.
3. Review the generated trade.

**Expected Result:**
The action is `NONE` and the number of shares is 0.

---

## ST04 – Invalid Input

**Scenario:** Verify that the rebalancer rejects basic invalid input.

**Test Steps:**

1. Load an account containing a security with a unit price of 0.
2. Run the rebalancer.
3. Review the result.

**Expected Result:**
The rebalancing operation is rejected and an appropriate validation error is returned.
