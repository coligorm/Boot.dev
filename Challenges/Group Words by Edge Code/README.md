# Group Words by Edge Code

## Complete the ``group_words_by_edge`` function.

It should take a list of strings and return a dictionary:

- each **key** is made from the word's first character plus its last character
- each **value** is a list of all words that match that key
- keep the words in the same order they appeared in the input list

Use string slicing to get the first and last parts of each word.

For example:

```
words = ["apple", "angle", "banana", "boat"]
print(group_words_by_edge(words))
# {
#   "ae": ["apple", "angle"],
#   "ba": ["banana"],
#   "bt": ["boat"]
# }
```

## Requirements

- Return a dictionary
- Use the edge code ``word[:1] + word[-1:]``
- If multiple words have the same edge code, put them in the same list
- If the input list is empty, return an empty dictionary
- An empty string should use ``""`` as its key