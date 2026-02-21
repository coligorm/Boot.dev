# Group Books by Author

## Complete the ``group_books_by_author`` function.

You are given a list of book dictionaries. Each book has a ``"title"`` and an ``"author"`` key.

Your job is to build and return a dictionary that groups book titles by their author.

- The keys of the result should be author names (strings).
- The values should be lists of titles (strings) written by that author.
- The titles in each list should appear in the same order as in the input list.
- If the input list is empty, return an empty dictionary.

### Function Details
> ``result = group_books_by_author(books)``

- books is a list of dictionaries like:
    - ``{"title": "The Hobbit", "author": "J.R.R. Tolkien"}``
- You should create a new dictionary and fill it using a loop.

Think in steps:

1. Start with an empty dictionary ``author_to_titles``.
2. Loop through each ``book`` in the ``books`` list.
3. For each ``book``:
    - Get the author name.
    - Get the title.
    - If the author is not already a key in the dictionary, add it with an empty list.
    - Append the title to that author's list.
4. Return the ``author_to_titles`` dictionary.