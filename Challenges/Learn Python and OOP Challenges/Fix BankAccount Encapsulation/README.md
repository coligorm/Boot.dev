# Fix BankAccount Encapsulation

The `BankAccount` class is meant to model a bank account with **encapsulated (private) state**.

Right now, it has a few bugs related to:

- **Class vs. instance variables** (account numbers and per-account settings)
-**Getters that leak private state** (mutable lists being returned directly)

## What to fix

Update `BankAccount` so that it behaves like this:

1. **Account numbers must be unique across all accounts**

    - `BankAccount.next_account_number` is a **class variable**.
    - When you create multiple accounts, their account numbers should increment globally (e.g. `1000`, `1001`, `1002`, ...).

2. **Daily withdrawal limit must be per-account (instance state)**

    - `BankAccount.default_daily_withdraw_limit` is the default for new accounts.
    - Calling `set_daily_withdraw_limit(...)` should only change that one account, not the default for every future account.

3. **`get_transactions()` must not allow outside code to mutate the internal list**

    - It should return a new list (a copy) rather than the actual internal transactions list.