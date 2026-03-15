# Cafe Menu Inheritance

## Complete the classes in `main.py`.

This is a small Python OOP practice challenge using classes and inheritance.

### Your task

Create these classes:

- `MenuItem`(name, price)`
- `Drink(name, price, size)`
- `Dessert(name, price, slices)`

### Required behavior

#### `MenuItem`

- Store `name` and `price`
- Add a `description()` method
- `description()` should return:

```
"Tea: $3"
```

#### `Drink`

- Inherit from `MenuItem`
- Also store `size`
- Override `description()` so it returns:

```
"Tea (large drink): $3"
```

#### `Dessert`

- Inherit from `MenuItem`
- Also store `slices`
- Override `description()` so it returns:

```
"Pie (2 slices): $6"
```

### Example

```
item = `MenuItem`("Toast", 4)
print(item.`description()`)
# Toast: $4

drink = Drink("Coffee", 5, "small")
print(drink.`description()`)
# Coffee (small drink): $5

dessert = Dessert("Cake", 8, 3)
print(dessert.`description()`)
# Cake (3 slices): $8
```

### Notes

- Use inheritance for `Drink` and `Dessert`
- Keep the output text exactly the same as shown
- Do not use encapsulation or private attributes for this challenge