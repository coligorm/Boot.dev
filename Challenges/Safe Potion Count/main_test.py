from main import *

run_cases = [
    ("3", 3, None),
    ("12", 12, None),
]

submit_cases = run_cases + [
    ("abc", None, "not a number"),
    ("-1", None, "count cannot be negative"),
    ("25", 25, None),
]


def test(input1, expected_output, expected_error):
    print("---------------------------------")
    print(f"Input: {input1}")
    try:
        result = read_potion_count(input1)
        print(f"Expected return: {expected_output}")
        print(f"Actual return:   {result}")
        if expected_error is not None:
            print(f"Expected error:  {expected_error}")
            return False
        return result == expected_output
    except Exception as error:
        print(f"Expected error: {expected_error}")
        print(f"Actual error:   {error}")
        if expected_error is None:
            return False
        return type(error) is ValueError and str(error) == expected_error



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


text_cases = submit_cases
if "__RUN__" in globals():
    text_cases = run_cases

test_cases = text_cases
main()
