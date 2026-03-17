# Clean and Join Tags

You work on a small blog platform that uses tags to organize posts. The raw tags can be messy: they might have extra spaces, different casing, and duplicates.

Complete the ``clean_tags(tags)`` function so it returns a new list of tags that are:

- trimmed (no leading/trailing spaces)
- lowercased
- unique, preserving the first time each tag appears

The provided code will then print the tags joined with the given separator and the total count.

Details:

- Use a loop and a list to build the result while preserving order
- Do not sort the tags
- Do not use sets (we need to preserve the first occurrence order)

Expected behavior for the provided input:

- Input list: contains values like `" Python ", "strings", "Python", " Loops ", "lists", "loops", "Lists "`
- Output printed exactly as two lines:
```
Tags: python, strings, loops, lists
Total: 4
```