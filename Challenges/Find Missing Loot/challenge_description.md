# Find Missing Loot

## Complete the `find_missing_items` function.

You are tracking loot in a game. You have:

- `owned_items`: a list of item names you already have
- `available_items`: a list of all items that exist in the game

Return a **new list** containing the items that are in `available_items` but not in `owned_items`.

Use Python **sets** to solve this, using a set difference.

The result should:

- Contain each missing item only once (no duplicates)
- Be **sorted alphabetically** so the order is predictable

> You can turn a list into a set with `set(my_list)`.
>
> You can find items that are in one set but not another with the **set difference** operator: `set_a - set_b`.
>
> You can sort a collection with `sorted(values)`. It returns a new list with the items in order.


# What you need to do
1. Convert the input lists to sets.
2. Use **set difference** to find items that are in ``available_items`` but not in ``owned_items``.
3. Convert the result back to a list.
4. Sort that list alphabetically.
5. Return the sorted list.