# Validate Discounted Price

## Complete the ``apply_discount`` function.

This function helps a small in-game shop safely apply percentage discounts to item prices.

``apply_discount(price, discount)`` should:

1. Treat both price and discount as integers.
2. Use exceptions to handle bad input.
3. Ret3.urn the final price after the discount.

### Rules
1. Try to convert both ``price`` and ``discount`` to integers.

    - If either value cannot be converted (for example, a list or a string like ``"ten"``), raise:
    > ``ValueError("price and discount must be numbers")``

2. If the (converted) price is less than 0, raise:

    > ``ValueError("price must be non-negative")``

3. If the (converted) discount is less than 0 or greater than 100, raise:

    > ``ValueError("discount must be between 0 and 100")``

4. Otherwise, compute the final price as an integer after applying the percentage discount.
    - Use integer math (no decimals). For example, a 25% discount on 80 should give 60.