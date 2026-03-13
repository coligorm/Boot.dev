# Calculate Item Revenue

## Complete the `get_revenue_per_item` function.

You are helping a fantasy shop keep track of how much money each item earns.

You are given:

- `orders`: a **list** of dictionaries. Each order dictionary has an `"items"` key.
- `"items`" is a list of dictionaries. Each item dictionary has:
    - `"name`": the item name (a string)
    - `"quantity`": how many were sold in that order (an integer)
- `prices`: a **dictionary** that maps item names (strings) to their price (integers).

Your job is to calculate how much **gold each item earned in total** across all orders.

## Function behavior

Write the function:

```
def get_revenue_per_item(orders, prices):
    # your code
```

It should:

1. Go through every order in `orders`.
2. For each order, go through every item in that order's `"items"` list.
3. For each item:
    - Look up the price in the `prices` dictionary using the item `"name"`.
    - Multiply the price by the `"quantity"` to get the revenue for that item in this order.
    - Add that revenue to a running total for that item name in a result dictionary.
4. Return the result dictionary.

### Important details

- If an item name from an order is **not** in the `prices` dictionary, **ignore that item** completely. Do not add it to the result.
- If there are **no orders**, return an empty dictionary: {}.
- The keys of the result dictionary should be item names (strings).
- The values of the result dictionary should be the total revenue (integers) for that item.