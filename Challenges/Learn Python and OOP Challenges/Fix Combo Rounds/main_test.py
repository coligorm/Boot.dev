from main import *

run_cases = [
    ([12, 5, 18, 9], [12, 18]),
    ([3, 4, 5], []),
    ([10, 10, 2, 15], [10, 10, 15]),
]

submit_cases = run_cases + [
    ([], []),
    ([1, 10, 11, 9, 25], [10, 11, 25]),
    ([14, 8, 13, 7, 12], [14, 13, 12]),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Input scores: {input1}")
    result = get_combo_rounds(input1)
    print(f"Expected:     {expected_output}")
    print(f"Actual:       {result}")
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
