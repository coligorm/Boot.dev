# Fix Bit Flags Utilities

You’re working with **8-bit flags** (numbers from `0` to `255`). Each bit represents whether a feature is on (`1`) or off (`0`).

Fix the functions in `main.py`:

## 1. to_8bit_binary(n)
Return an 8-character string of `0`s and `1`s representing the **lowest 8 bits** of `n`.

Examples:
```
to_8bit_binary(5)    # "00000101"
to_8bit_binary(255)  # "11111111"
```

## 2. has_all_flags(value, flags)

Return `True` if **all** bits that are set in `flags` are also set in `value`.

Example:
```
value = 0b00101101
flags = 0b00100100
has_all_flags(value, flags)  # True
```

## 3. add_flags(value, flags)

Return a new number that is `value` but with all bits from `flags` turned on.

Example:
```
add_flags(0b00010000, 0b00000101)  # 0b00010101
```