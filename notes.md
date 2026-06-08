# Notes for Boot.dev course

## Chapter 7. Learn Functional Programming in Python

### First Class Functions

#### Lambda

Anonymous functions have no name, and in Python, they're called [lambda functions](https://docs.python.org/3/reference/expressions.html#lambda) after lambda calculus. Here's a lambda function that takes a single argument x and returns the result of x + 1:
```
lambda x: x + 1
```
This is usefull for simple functions like the above, instead of writing this:
```
def add_one(x):
    return x + 1
```

Using the lambda function in the code below:
```
add_one = lambda x: x + 1
print(add_one(2))
# 3
```

They simply return the result of an expression, they're often used for small, simple evaluations

##### Lambda If/Else

```
lambda x: True if x % 2 == 0 else False
```

##### Lambda Assignment Example

In the following assignment, I was asked to take a list of tuples, where each tuple contains a file type (e.g. "code", "document", "image", etc.) and a list of associated file extensions (e.g. [".py", ".js"] or [".docx", ".doc"]), and return a lambda function that accepts a string (a file extension) and returns its file type from the dictionary.

```
def file_type_getter(file_extension_tuples):
    file_extensions_dict = {}
    for tup in file_extension_tuples:
        for ext in tup[1]:
            file_extensions_dict[ext] = tup[0]
    return lambda ext: file_extensions_dict.get(ext, "Unknown")
```

#### First Class and Higher Order Functions

A programming language "supports first-class functions" when functions are treated like any other variable. That means functions can be passed as arguments to other functions, can be returned by other functions, and can be assigned to variables.

- **First-class function**: A function that is treated like any other value
- **Higher-order function**: A function that accepts another function as an argument or returns a function

##### First Class Example

```
def square(x):
    return x * x

# Assign function to a variable
f = square

print(f(5))
# 25
```

##### Higher-Order Example

```
def square(x):
    return x * x

def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

squares = my_map(square, [1, 2, 3, 4, 5])
print(squares)
# [1, 4, 9, 16, 25]
```

> "Map," "filter," and "reduce" are three commonly used higher-order functions in functional programming.

#### Map

The `map` function takes a function and an iterable (in this case a list) as inputs. It returns an iterator that applies the function to every item, yielding the results.

```
def square(x):
    return x * x

nums = [1, 2, 3, 4, 5]
squared_nums = map(square, nums)

print(list(squared_nums))
# [1, 4, 9, 16, 25]
```

> Note: `map()` returns a "map object," so the `list()` type constructor is needed to convert it back into a standard list.

##### Map Assignment Example

Complete the `change_bullet_style` function. It takes a document (a string) as input, and returns a single string as output. The returned string should have any lines that start with a - character replaced with a * character.

```
def change_bullet_style(document):
    return "\n".join(map(convert_line, document.split("\n")))


# Don't edit below this line


def convert_line(line):
    old_bullet = "-"
    new_bullet = "*"
    if len(line) > 0 and line[0] == old_bullet:
        return new_bullet + line[1:]
    return line
```

#### Filter

The `filter` function takes a function and an iterable (in this case a list) and returns an iterator that only contains elements from the original iterable where the result of the function on that item returned `True`.

```
def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(is_even, numbers))
print(evens)
# [2, 4, 6]
```

##### Filter Assignment Example

Complete the `remove_invalid_lines function`. It accepts a document string as input. It should:

- Use the built-in filter function with a lambda to make a filtered copy of the input document.
- Remove any lines that start with a - character.
- Keep all other lines and preserve any trailing newlines (\n).
- Return the result, all on one expression.

```
def remove_invalid_lines(document):
    return "\n".join(filter(lambda line: not line.startswith("-"), document.split("\n")))
```

#### Reduce

The `functools.reduce()` function takes a function and a list of values, and applies the function to each value in the list, accumulating a single result as it goes.

```
# import functools from the standard library
import functools

def add(sum_so_far, x):
    print(f"sum_so_far: {sum_so_far}, x: {x}")
    return sum_so_far + x

numbers = [1, 2, 3, 4]
sum = functools.reduce(add, numbers)
# sum_so_far: 1, x: 2
# sum_so_far: 3, x: 3
# sum_so_far: 6, x: 4
# 10 doesn't print, it's just the final result
print(sum)
# 10
```

> Notice that we are passing the function add without the ().
> It means that reduce will take care of the execution and pass the parameters for you.

##### Reduce Assignment Example

Complete the `join` and the `join_first_sentences` functions. The `join` function is a helper function we'll use in `join_first_sentences`.
The `join` function returns the result of concatenating the "doc" and "sentence" strings together, with a period and a space in between.
The `join_first_sentences` function accepts two arguments:

- A list of sentence strings
- An integer `n`

Only use the first `n` sentences from the list. If `n` is zero, just return an empty string.
Use `functools.reduce()` with your join function to combine the sliced sentences into a single string.
Add a final period without a trailing space and return this string.

```
import functools


def join(doc_so_far, sentence):
    return doc_so_far + ". " + sentence


def join_first_sentences(sentences, n):
    if n == 0:
        return ""
    return functools.reduce(join, sentences[:n]) + "."

```

#### Zip

The zip function takes two iterables (in this case lists), and returns a new iterable where each element is a tuple containing one element from each of the original iterables.

```
a = [1, 2, 3]
b = [4, 5, 6]

c = list(zip(a, b))
print(c)
# [(1, 4), (2, 5), (3, 6)]
```



### Function Transformations

"Function transformation" is just a concise way to describe a specific type of higher-order function. It's when a function takes a function (or functions) as input and returns a new function. Let's look at an example:

```
from collections.abc import Callable

def multiply(x: int, y: int) -> int:
    return x * y

def add(x: int, y: int) -> int:
    return x + y

# self_math is a higher-order function
# input: a function that takes two arguments and returns a value
# output: a new function that takes one argument and returns a value
def self_math(math_func: Callable[[int, int], int]) -> Callable[[int], int]:
    def inner_func(x: int) -> int:
        return math_func(x, x)
    return inner_func

square_func: Callable[[int], int] = self_math(multiply)
double_func: Callable[[int], int] = self_math(add)

print(square_func(5))
# prints 25

print(double_func(5))
# prints 10
```

The `self_math` function takes a function that operates on two *different* parameters (e.g. `multiply` or `add`) and returns a new function that operates on one parameter *twice* (e.g. `square` or `double`).