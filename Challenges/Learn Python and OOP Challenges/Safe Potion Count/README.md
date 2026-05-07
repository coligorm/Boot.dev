# Safe Potion Count

## Complete the `read_potion_count` function.

It should take a string and:
- return the number as an `int` if the string contains a valid whole number
- raise `ValueError("not a number")` if the string cannot be converted to an integer
- raise V`alueError("count cannot be negative")` if the number is less than `0`

Use a `try/except` block for the string-to-integer conversion, and raise your own `ValueError` when needed.

### Examples
```
print(read_potion_count("7"))
# 7
```
```
read_potion_count("oops")
# raises ValueError("not a number")
```
```
read_potion_count("-3")
# raises ValueError("count cannot be negative")
```