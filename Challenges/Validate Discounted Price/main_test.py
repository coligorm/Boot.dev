from main import apply_discount

run_cases = [
    (100, 10, 90, None),
    (50, 0, 50, None),
    (80, 25, 60, None),
]

submit_cases = run_cases + [
    ("100 coins", 10, None, "price and discount must be numbers"),
    (100, 150, None, "discount must be between 0 and 100"),
    (-10, 10, None, "price must be non-negative"),
]


def test(price, discount, expected_result, expected_error):
    print("---------------------------------")
    print(f"Input price:    {price}")
    print(f"Input discount: {discount}")
    print("")

    try:
        result = apply_discount(price, discount)
        if expected_error is not None:
            print(f"Expected error: {expected_error}")
            print(f"Actual result:  {result}")
            print("Fail")
            return False
        print(f"Expected: {expected_result}")
        print(f"Actual:   {result}")
        if result == expected_result:
            print("Pass")
            return True
        print("Fail")
        return False
    except Exception as e:
        if expected_error is None:
            print(f"Expected: {expected_result}")
            print(f"Actual error: {repr(e)}")
            print("Fail")
            return False
        error_message = str(e)
        print(f"Expected error: {expected_error}")
        print(f"Actual error:   {error_message}")
        if isinstance(e, ValueError) and error_message == expected_error:
            print("Pass")
            return True
        print("Fail")
        return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)

    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1

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
