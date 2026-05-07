# Fix Priority Member Labels

The `get_priority_member_labels` pipeline is supposed to:

- keep only **active** members
- keep only members whose `spend` is **greater than or equal** to `minimum_spend`
- return a new list of labels in this format:
```
"NAME (tier)"
```

The current code has multiple bugs in the filtering and transformation steps.

## Example

```
members = [
    {"name": "Ava", "active": True, "spend": 120, "tier": "gold"},
    {"name": "Ben", "active": False, "spend": 200, "tier": "platinum"},
    {"name": "Cora", "active": True, "spend": 90, "tier": "silver"},
]

print(get_priority_member_labels(members, 100))
# Expected:
# ["AVA (gold)"]
```

## Your task

Fix these functions so they behave correctly:

- `filter_active_members`
- `filter_min_spend`
- `build_member_labels`
- `get_priority_member_labels`

## Requirements

- Use higher-order functions with `filter()` and `map()`.
- Use small `lambda` functions inside `filter()` and `map()`.
- Return regular Python lists, not `filter` or `map` objects.
- If the input list is empty, return an empty list.
- If no members match, return an empty list.

## Expected behavior

- `active` must be `True`
- `spend` must be `>= minimum_spend`
- labels must use the member name in uppercase
- labels must preserve the original order of matching records
