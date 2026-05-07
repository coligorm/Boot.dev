from main import *

run_cases = [
    (["10", "20", "30"], (60, 0), False),
    (["5", "x", "15"], (20, 1), False),
    (["-3", "0", "7", "oops"], (4, 1), False),
]

submit_cases = run_cases + [
    (["a", "b", "3"], (3, 2), False),
    (["abc", "???"], None, True),
]


def test(values, expected_result, expect_error):
    print("---------------------------------")
    print(f"Input values: {values}")
    if not expect_error:
        print(f"Expecting: {expected_result}")
    else:
        print('Expecting: ValueError("no valid numbers")')

    try:
        result = sum_valid_numbers(values)
        print(f"Actual:   {result}")

        if expect_error:
            print("Fail (expected an exception but none was raised)")
            return False

        if result == expected_result:
            print("Pass")
            return True
        else:
            print("Fail")
            return False

    except ValueError as e:
        print(f"Raised:   ValueError('{e}')")
        if expect_error and str(e) == "no valid numbers":
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
