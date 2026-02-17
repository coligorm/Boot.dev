from main import *

run_cases = [
    (
        ["sword", "shield"],
        ["sword", "shield", "potion"],
        ["potion"],
    ),
    (
        ["potion", "elixir"],
        ["potion", "elixir"],
        [],
    ),
    (
        [],
        ["map", "torch"],
        ["map", "torch"],
    ),
]

submit_cases = run_cases + [
    (
        ["map", "torch", "rope"],
        [],
        [],
    ),
    (
        ["sword", "sword", "potion"],
        ["sword", "shield", "potion", "potion"],
        ["shield"],
    ),
    (
        ["a", "c", "b", "b"],
        ["b", "c", "d", "e"],
        ["d", "e"],
    ),
]


def test(owned_items, available_items, expected_output):
    print("---------------------------------")
    print(f"Owned items:     {owned_items}")
    print(f"Available items: {available_items}")
    print("")
    result = find_missing_items(owned_items, available_items)
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
