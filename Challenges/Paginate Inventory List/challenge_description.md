# Paginate Inventory List

## Complete the `paginate_items` function.

You are building an inventory screen for a game. The inventory is a list of item names, and you can only show a fixed number of items per page.

`paginate_items(items, page_size)` should:

- Take a list of strings `items` (the inventory)
- Take an integer `page_size` (how many items fit on one page)
- Return a **list of pages**, where each page is a **list of items**
- Keep the original order of the items
- Put up to `page_size` items on each page

You can assume `page_size` is always a positive integer (`>= 1`).

Use a loop and **list slicing** to build the pages.

> **List slicing** lets you take a part of a list.
> 
> For example, with `numbers = [10, 20, 30, 40, 50]`:
> 
> - `numbers[0:2]` is `[10, 20]` (from index 0 up to, but not including, index 2)
> - `numbers[2:5]` is `[30, 40, 50]`