# Fix Shape Polymorphism and Addition

You are building a small geometry library for a level editor.

The code is **supposed to use polymorphism** so that every kind of shape knows how to calculate its own area. You should be able to:

1. Create `Rectangle` and `Square` objects
2. Call `.area()` on any shape, without caring which kind it is
3. Use `+` between shapes to build a `CompositeShape`
4. Call `.area()` on a `CompositeShape` to get the total area of all its shapes

Right now, the implementation is wrong in several places:

- Some shapes are **not returning the correct area**.
- Adding shapes with `+` returns a plain number instead of a new shape.
- Combined shapes do not correctly sum the areas of all their parts.

Your job is to **fix the polymorphic behavior** so that every call to `.area()` uses the **correct implementation for that specific shape**, and `+` always returns a `CompositeShape`.

## Expected Behavior

### Individual shapes

```
from main import Rectangle, Square

r = Rectangle(2, 3)
print(r`.area())`
# Expected: 6

s = Square(4)
print(s`.area())`
# Expected: 16
```

- `Rectangle(width, height)` area: `width * height`
- `Square(side)` area: `side * side`

`Square` is a kind of `Rectangle`, so it should reuse the rectangle behavior through inheritance.

### Adding shapes with `+`

Using `+` between shapes should create a `CompositeShape` that represents all of them together.

```
from main import Rectangle, Square

r = Rectangle(2, 3)     # area 6
s = Square(4)           # area 16
combined = r `+` s        # should be a `CompositeShape`

print(type(combined).__name__)
# Expected: "`CompositeShape`"

print(combined`.area())`
# Expected: 22  (6 `+` 16)
```

You should also be able to chain additions:

```
from main import Rectangle, Square

r = Rectangle(2, 3)     # 6
s = Square(4)           # 16
small = Rectangle(1, 1) # 1

big = r `+` s `+` small
print(big`.area())`
# Expected: 23  (6 `+` 16 `+` 1)
```

The `+` operator should:

- Work between any two `Shape` objects
- Return a `CompositeShape` that contains **all** the shapes
- If either side is already a `CompositeShape`, it should include all of its shapes (not nest them weirdly)

### CompositeShape

`CompositeShape` represents a collection of shapes.

```
from main import Rectangle, Square, `CompositeShape`

r1 = Rectangle(3, 3)   # 9
r2 = Rectangle(2, 5)   # 10
s = Square(2)          # 4

combo = `CompositeShape`([r1, r2, s])
print(combo`.area())`
# Expected: 23  (9 `+` 10 `+` 4)

more = combo `+` Square(1)  # `+`1 area
print(more`.area())`
# Expected: 24
```

`CompositeShape``.area()` must:

- Call `.area()` on each contained shape (polymorphism)
- Return the **sum** of all their areas

## What You Need to Do

Open `main.py` and fix the existing classes:

- Make sure Rectangle`.area()` returns the correct area
- Make sure Square correctly uses rectangle behavior through inheritance
- Fix Shape.__add__ so that using `+` between shapes returns a `CompositeShape`, not a number
- Make `CompositeShape``.area()` correctly sum the areas of all its shapes using their own `.area()` methods

You **do not** need to add new classes or new public methods. Just fix the broken logic so the tests pass.

> __add__ is a special method that lets you overload the `+` operator in Python. When you write a `+` b, Python actually calls a.__add__(b) under the hood.