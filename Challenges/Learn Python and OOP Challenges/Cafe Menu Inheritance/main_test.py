from main import *

run_cases = [
    ("menu", ("Toast", 4), "Toast: $4"),
    ("drink", ("Coffee", 5, "small"), "Coffee (small drink): $5"),
    ("dessert", ("Pie", 6, 2), "Pie (2 slices): $6"),
]

submit_cases = run_cases + [
    ("drink", ("Tea", 3, "large"), "Tea (large drink): $3"),
    ("dessert", ("Brownie", 7, 1), "Brownie (1 slices): $7"),
    ("menu", ("Soup", 9), "Soup: $9"),
]


def test(item_type, values, expected_output):
    print("---------------------------------")
    if item_type == "menu":
        name, price = values
        print("Input:")
        print(f"  Type: MenuItem")
        print(f"  Name: {name}")
        print(f"  Price: {price}")
        result = MenuItem(name, price).description()
    elif item_type == "drink":
        name, price, size = values
        print("Input:")
        print(f"  Type: Drink")
        print(f"  Name: {name}")
        print(f"  Price: {price}")
        print(f"  Size: {size}")
        result = Drink(name, price, size).description()
    else:
        name, price, slices = values
        print("Input:")
        print(f"  Type: Dessert")
        print(f"  Name: {name}")
        print(f"  Price: {price}")
        print(f"  Slices: {slices}")
        result = Dessert(name, price, slices).description()
    print("")
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    if result == expected_output:
        return True
    return False



def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
            print("Pass")
        else:
            failed += 1
            print("Fail")
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")



test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
