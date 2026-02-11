from main import *

run_cases = [
    (["potion", "sword", "shield", "bow", "arrow"], 2, [["potion", "sword"], ["shield", "bow"], ["arrow"]]),
    (["apple", "bread", "cheese"], 5, [["apple", "bread", "cheese"]]),
    ([], 3, []),
]

submit_cases = run_cases + [
    (["herb", "elixir", "scroll", "gem"], 1, [["herb"], ["elixir"], ["scroll"], ["gem"]]),
    (["iron", "wood", "stone", "cloth", "leather", "glass", "crystal"], 3, [["iron", "wood", "stone"], ["cloth", "leather", "glass"], ["crystal"]]),
    (["key"], 1, [["key"]]),
]


def test(items, page_size, expected_output):
    print("---------------------------------")
    print(f"Input items: {items}")
    print(f"Page size:   {page_size}")
    print("")
    result = paginate_items(items, page_size)
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
