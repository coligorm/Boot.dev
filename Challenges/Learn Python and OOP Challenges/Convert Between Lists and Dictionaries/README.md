# Convert Between Lists and Dictionaries

## Complete two functions in `main.py`:

- `list_to_dict(pairs)`
- `dict_to_list(mapping)`

You are working with a simple game inventory system.

## 1. `list_to_dict(pairs)`

`pairs` will be a list of 2-item lists, where:

- ndex `0` is the key (a string)
- ndex `1` is the value (a number)

Convert this list into a dictionary and return it.

For example:

```
items = [["potion", 3], ["elixir", 1]]
print(list_to_dict(items))
# {"potion": 3, "elixir": 1}
```

If the same key appears more than once, the last value should be kept (this is what normally happens when you assign to the same dictionary key multiple times).

## 2. `dict_to_list(mapping)`

`mapping` will be a dictionary.

Convert this dictionary into a list of 2-item lists in the format:

```
[key, value]
```

Return the resulting list.

The order of items in the list should follow the dictionary's insertion order (the order the keys appear in the dictionary).

For example:
```
inventory = {"potion": 3, "elixir": 1}
print(dict_to_list(inventory))
# [["potion", 3], ["elixir", 1]]
```

### Summary

- Use a loop to build a dictionary from a list of `[key, value]` pairs.
- Use a loop to build a list of `[key, value]` pairs from a dictionary.
- Do not print anything in these functions, just `return` the result.


