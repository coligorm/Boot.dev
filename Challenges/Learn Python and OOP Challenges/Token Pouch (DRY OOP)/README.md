# Token Pouch (DRY OOP)

## Complete the `TokenPouch` class in `main.py`.

You’re building a tiny in-game currency system. A `TokenPouch` holds an integer number of tokens, and supports depositing, withdrawing, and transferring tokens between pouches.

### Requirements

Implement:

- `__init__(starting_tokens)`
    - starting_tokens must be an int and >= 0
    - otherwise raise ValueError

- `tokens` (read-only property)
    - returns the current token count

- `deposit(amount)`
    - `amount` must be an `int` and > 0
    - add tokens to the pouch
    - return the new token count

- `withdraw(amount)`
    - `amount` must be an `int` and > 0
    - if there aren’t enough tokens, raise `ValueError`
    - subtract tokens from the pouch
    - return the new token count

- `transfer_to(other_pouch, amount)`
    - `other_pouch` must be a `TokenPouch`, otherwise raise `TypeError`
    - `amount` must be an `int` and > 0
    - if there aren’t enough tokens to transfer, raise `ValueError`
    - move tokens from `self` to `other_pouch`
    - return a tuple: `(self.tokens, other_pouch.tokens)`

## Clean code / DRY constraint

Don’t copy/paste the same validation logic in multiple methods.

Use private helper method(s) (like `__validate_amount`(...)) so that validation is written once and reused.