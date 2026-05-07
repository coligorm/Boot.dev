# Label Exam Scores

## Complete the `label_scores` function.

You are building a small tool for a teacher to quickly see how students did on a test.

The function should:

- Take a list of integer scores and a single `passing_score` (also an integer).
- Return a new list of strings with one label for each score:
- `"excellent"` if the score is greater than or equal to `passing_score + 20`
- `"pass"` if the score is greater than or equal to `passing_score`, but less than `passing_score + 20`
- `"fail"` if the score is less than `passing_score`

Use a `for` loop to go through the list of scores and `if` / `elif` / `else` to choose the right label.

Do **not** modify the original list. Build and return a new list.