# Fix Combo Rounds

## The `get_combo_rounds` function is supposed to return a new list containing every round score that is 10 or higher.

Right now, it stops too early and misses later scores.

### Expected behavior

- Look through the whole round_scores list
- Keep every score that is 10 or more
- Return them in the same order
- If there are no combo rounds, return an empty list