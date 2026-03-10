# Sum Valid Numbers Safely

## Complete the `sum_valid_numbers` function.

You are given a list of values that should be whole numbers written as strings, but some entries might be invalid.

The function must:

1. Try to convert each value to an integer using int(...).
2. Use a try / except block to catch conversion errors.
3. Keep a running total of all values that convert successfully.
4. Count how many values are invalid (they raise an error when you try to convert them).
5. If at least one value is valid, return a tuple (total, invalid_count):
    - total: the sum of all valid numbers
    - invalid_count: how many values were invalid
6. If no values are valid, raise a ValueError with the message:
```
"no valid numbers"
```

You should explicitly raise this error using the raise keyword.
> try / except lets you run code that might fail, and handle the error instead of crashing the program. The raise keyword lets you create an error on purpose.