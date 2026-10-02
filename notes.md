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



### 7.5.1 Function Transformations

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


---

## Chapter 9. Learn Data Structures and Algorithms

### Bubble Sort

Bubble sort is famous for how easy it is to write and understand.
However, it's one of the slowest sorting algorithms, and as a result is almost never used in practice.

<details>
    <summary><em>Pseudocode</em></summary>
    <ol>
        <li>Set <code>swapping</code> to <code>True</code></li>
        <li>Set <code>end</code> to the length of the input list</li>
        <li>While <code>swapping</code> is <code>True</code>:</li>
        <ol>
            <li>Set <code>swapping</code> to <code>False</code></li>
            <li>For <code>i</code> from the 2nd element to <code>end</code>:</li>
            <ul>
                <li>If the <code>(i-1)</code>th element of the input list is greater than the <code>i</code>th element:</li>
                <ol>
                    <li>Swap the <code>(i-1)</code>th element and the <code>i</code>th element</li>
                    <li>Set <code>swapping</code> to <code>True</code></li>
                </ol>
            </ul>
            <li>Decrement <code>end</code> by one</li>
        <li>Return the sorted list</li>
    </ol>
</details>

```python
def bubble_sort(nums: list[int]) -> list[int]:
    swapping = True
    end = len(nums)

    while swapping:
        swapping = False
        for i in range(1, end):
            if nums[i-1] > nums[i]:
                nums[i-1], nums[i] = nums[i], nums[i-1]
                swapping = True
        end -= 1
    return nums
```

### Merge Sort

Merge sort is a recursive sorting algorithm and it's quite a bit faster than bubble sort. It's a divide and conquer algorithm
In merge sort we:

- Divide the array into two equal halves (divide)
- Recursively sort the two halves
- Merge the two halves to form a sorted array (conquer)

<details>
    <summary><em>Pseudocode</em></summary>
    <b><code>merge_sort()</code></b>
    <br>
    Input: <code>A</code>, an unsorted list of integers
    <ol>
        <li>If the length of <code>A</code> is less than <code>2</code>, it's already sorted so return it</li>
        <li>Split the input array into two halves down the middle</li>
        <li>Call <code>merge_sort()</code> twice, once on each half</li>
        <li>Return the result of calling <code>merge(sorted_left_side, sorted_right_side)</code> on the results of the <code>merge_sort()</code> calls</li>
    </ol>
    <b><code>merge()</code></b>
    <br>
    Inputs: <code>A</code> and <code>B</code>. Two sorted lists of integers
    <ol>
        <li>Create a new <code>final</code> list of integers.</li>
        <li>Set <code>i</code> and <code>j</code> equal to zero. They will be used to keep track of indexes in the input lists (<code>A</code> and <code>B</code>).</li>
        <li>Use a loop to compare the current elements of <code>A</code> and <code>B</code>:</li>
        <ul>
            <li>While <code>i < len(A)</code> and <code>j < len(B)</code>, compare <code>A[i]</code> and <code>B[j]</code>.</li>
            <li>Append the smaller or equal value to <code>final</code>.</li>
            <li>Increment the index for the list you just took from.</li>
            <li>Stop when either list is exhausted.</li>
        </ul>
        <li>After comparing all the items, there may be some items left over in either <code>A</code> or <code>B</code>. Add those extra items to the <code>final</code> list.</li>
        <li>Return the <code>final</code> list.</li>
</details>


```python
def merge_sort(nums: list[int]) -> list[int]:
    if len(nums) < 2:
        return nums
    sorted_left_side = merge_sort(nums[: len(nums) // 2])
    sorted_right_side = merge_sort(nums[len(nums) // 2 :])
    return merge(sorted_left_side, sorted_right_side)


def merge(first: list[int], second: list[int]) -> list[int]:
    final = []
    i = 0
    j = 0
    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            final.append(first[i])
            i += 1
        else:
            final.append(second[j])
            j += 1
    while i < len(first):
        final.append(first[i])
        i += 1
    while j < len(second):
        final.append(second[j])
        j += 1
    return final
```

#### Why Merge Sort

Pros:
- Fast: Merge sort is much faster than bubble sort. O(n*log(n)) instead of O(n^2).
- Stable: Merge sort is a stable sort which means that values with duplicate keys in the original list will be in the same order in the sorted list.

Cons:
- Memory usage: Most sorting algorithms can be performed using a single copy of the original array. Merge sort requires extra subarrays in memory.
- Recursive: Merge sort requires many recursive function calls, and in many languages (like Python), this can incur a performance penalty.

### Insertion Sort

Insertion sort builds a sorted list one item at a time. It's much less efficient on large lists than merge sort because it's <code>O(n^2)</code>, but it's actually faster (not in Big O terms, but due to smaller constants) than merge sort on small lists.

<details>
    <summary><em>Pseudocode</em></summary>
    <ol>
        <li>For each index in the input list, starting with the second element:</li>
        <ol>
            <li>Set a <code>j</code> variable to the current index</li>
            <li>While <code>j</code> is greater than <code>0</code> and the element at index <code>j-1</code> is greater than the element at index <code>j</code>:</li>
            <ol>
                <li>Swap the elements at indices <code>j</code> and <code>j-1</code></li>
                <li>Decrement <code>j</code> by <code>1</code></li>
            </ol>
        </ol>
        <li>Return the list</li>
    </ol>
</details>

```python
def insertion_sort(nums: list[int]) -> list[int]:
    for i in range(1, len(nums)):
        j = i
        while j > 0 and nums[j-1] > nums[j]:
            nums[j], nums[j-1] = nums[j-1], nums[j]
            j -= 1
    return nums

```

#### Why Insetion Sort

- Fast: for very small data sets (even faster than merge sort and quick sort, which we'll cover later)
- Adaptive: Faster for partially sorted data sets
- Stable: Does not change the relative order of elements with equal keys
- In-Place: Only requires a constant amount of memory
- Online: Can sort a list as it receives it

### Quick Sort

Quick sort is an efficient sorting algorithm that's widely used in production sorting implementations. Like merge sort, quick sort is a recursive divide and conquer algorithm.

Divide:
- Select a pivot element that will preferably end up close to the center of the sorted pack
- Move everything onto the "greater than" or "less than" side of the pivot
- The pivot is now in its final position
- Recursively repeat the operation on both sides of the pivot

Conquer:
- The array is sorted after all elements have been through the pivot operation

<details>
    <summary><em>Pseudocode</em></summary>
    <ol>
        <li>Complete quick_sort(nums, low, high):</li>
        <ol>
            <li>If low is less than high:</li>
            <ol>
                <li>Partition the input list using the partition function and store the returned "middle" index</li>
                <li>Recursively call quick_sort on the elements left of the pivot (low to middle - 1)</li>
                <li>Recursively call quick_sort on the elements right of the pivot (middle + 1 to high)</li>
            </ol>
        </ol>
        <li>partition(nums, low, high):</li>
        <ol>
            <li>Set pivot to the element at index high</li>
            <li>Set i to the index before low</li>
            <li>For each index (j) in range(low, high):</li>
            <ol>
                <li>If the element at index j is less than the pivot:</li>
                <ol>
                    <li>Increment i by 1</li>
                    <li>Swap the element at index i with the element at index j</li>
                </ol>
            </ol>
            <li>Swap the element at index i + 1 with the element at index high (the pivot's position)</li>
            <li>Return i + 1 (the pivot's new index)</li>
            </ol>
        </ol>
    </ol>
</details>

```python
def quick_sort(nums: list[int], low: int, high: int) -> None:
    if low < high:
        middle = partition(nums, low, high)
        quick_sort(nums, low, middle - 1)
        quick_sort(nums, middle + 1, high)

def partition(nums: list[int], low: int, high: int) -> int:
    pivot = nums[high]
    i = low - 1
    for j in range(low, high):
        if nums[j] < pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i+1], nums[high] = nums[high], nums[i+1]
    
    return i + 1
```

#### Fixing Quick Sort

While the version of quicksort that we implemented is almost always able to perform at speeds of O(n*log(n)), its Big O is still technically O(n^2) due to the worst-case scenario. We can fix this by altering the algorithm slightly.

Two of the approaches are:
- Shuffle input randomly before sorting. This can trivially be done in O(n) time.
- Actively find the median of a sample of data from the partition, this can be done in O(1) time.

#### Why Use Quick Sort?

Pros:
- Very fast: At least it is in the average case
- In-Place: Saves on memory, doesn't need to do a lot of copying and allocating

Cons:
- Typically unstable: changes the relative order of elements with equal keys
- Recursive: can incur a performance penalty in some implementations
- Pivot sensitivity: if the pivot is poorly chosen, it can lead to poor performance

### Selection Sort

It's similar to bubble sort in that it works by repeatedly swapping items in a list. However, it's slightly more efficient than bubble sort because it only makes one swap per iteration.

<details>
    <summary><em>Pseudocode</em></summary>
    <ol>
        <li>For each index:</li>
        <ol>
            <li>Set <code>smallest_idx</code> to the current index (of the outer loop)</li>
            <li>For each index from <code>i + 1</code> to the end of the list:</li>
            <ol>
                <li>If the number at the inner loop index is smaller than the number at <code>smallest_idx</code>, set <code>smallest_idx</code> to the inner loop index</li>
            </ol>
            <li>Swap the number at the outer loop index with the number at <code>smallest_idx</code></li>
        </ol>
        <li>Return the sorted list</li>
    </ol>
</details>

```python
def selection_sort(nums: list[int]) -> list[int]:
    for i in range(len(nums)):
        smallest_idx = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[smallest_idx]:
                smallest_idx = j
        nums[i], nums[smallest_idx] = nums[smallest_idx], nums[i]
    return nums
```

## Delete Binary Tree Node Assignment

I enjoyed this exercise on creating a delete function for a Binary Tree and didnt know where I wanted to document it yet:

> Delete
> We also need a way to remove users from our BST if a user decides to delete their account.
> 
> Assignment
> Implement the recursive delete method. It takes a value as an input and deletes the node with that value if it exists. Each call returns the new root of > the tree (or subtree) after the deletion.
> 
> Notice that in the test suite the delete method is called like this:
> 
> ```bst = bst.delete(character)```
> 
> Check if the current node is empty (has no value). If it is, return None. This represents an empty tree or a leaf node where deletion has already occurred.
> If the value to delete is less than the current node's value:
> If there's a left child, recursively delete the value from the left subtree and update the left child reference with the result.
> Return the current node.
> If the value to delete is greater than the current node's value:
> If there's a right child, recursively delete the value from the right subtree and update the right child reference with the result.
> Return the current node.
> If the value to delete equals the current node's value, we've found the node to delete:
> If there is no right child, return the left child. This bypasses the current node, effectively deleting it.
> If there is no left child, return the right child, accomplishing the same thing.
> If there are both left and right children:
> Start at the right child.
> Walk left until you find the smallest node in that right subtree. This is the next-largest value after the current node's value.
> Copy the next largest value into the current node's value.
> Delete the successor value from the right subtree by calling delete on it, and save the returned node as the new right child.
> Return the current node.

My solution:

```
from typing import Any


class BSTNode:
    def delete(self, val: Any) -> "BSTNode | None":
        if not self.val:
            return None

        if val < self.val:
            if self.left:
                res = self.left.delete(val)
                self.left = res
            return self

        if val > self.val:
            if self.right:
                res = self.right.delete(val)
                self.right = res
            return self

        if val == self.val:
            if not self.right:
                return self.left
            if not self.left:
                return self.right
            if self.right and self.left:
                next_largest = self.right.get_min()
                self.val = next_largest
                new_right_child = self.right.delete(self.val)
                self.right = new_right_child
            return self
                
    # don't touch below this line

    def __init__(self, val: Any = None) -> None:
        self.left: BSTNode | None = None
        self.right: BSTNode | None = None
        self.val = val

    def insert(self, val: Any) -> None:
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)

    def get_min(self) -> Any:
        current = self
        while current.left is not None:
            current = current.left
        return current.val

    def get_max(self) -> Any:
        current = self
        while current.right is not None:
            current = current.right
        return current.val

```

The solution:

```
from typing import Any


class BSTNode:
    def delete(self, val: Any) -> "BSTNode | None":
        if self.val is None:
            return None
        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)
            return self
        if val > self.val:
            if self.right:
                self.right = self.right.delete(val)
            return self
        if self.right is None:
            return self.left
        if self.left is None:
            return self.right
        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.val = min_larger_node.val
        self.right = self.right.delete(min_larger_node.val)
        return self

    # don't touch below this line

    def __init__(self, val: Any = None) -> None:
        self.left: BSTNode | None = None
        self.right: BSTNode | None = None
        self.val = val

    def insert(self, val: Any) -> None:
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)

    def get_min(self) -> Any:
        current = self
        while current.left is not None:
            current = current.left
        return current.val

    def get_max(self) -> Any:
        current = self
        while current.right is not None:
            current = current.right
        return current.val
```


## Red-Black Tree

A red-black tree is a kind of binary search tree that solves the "balancing" problem. It contains a bit of extra logic to ensure that as nodes are inserted and deleted, the tree remains relatively balanced.

**How it works**
Each node in an RB Tree stores an extra bit, called the "color": either red or black. The "color" ensures that the tree remains approximately balanced during insertions and deletions. When the tree is modified, the new tree is rearranged and repainted to restore the coloring properties that constrain how unbalanced the tree can become in the worst case.

**List of Very Simple Rules**
Each node is either red or black.
The root is black.
All Nil leaf nodes are black.
If a node is red, then both its children are black.
All paths from a single node go through the same number of black nodes to reach any of its descendant Nil (black) nodes.