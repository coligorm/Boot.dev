from main import *

run_cases = [
    ([55, 80, 40], 60, ["fail", "excellent", "fail"]),
    ([95, 80, 50], 75, ["excellent", "pass", "fail"]),
    ([60, 85, 100], 60, ["pass", "excellent", "excellent"]),
]

submit_cases = run_cases + [
    ([], 70, []),
    ([70, 89, 90], 70, ["pass", "pass", "excellent"]),
    ([30, 59, 60, 79, 80], 60, ["fail", "fail", "pass", "pass", "excellent"]),
]


def test(scores, passing_score, expected_output):
    print("---------------------------------")
    print(f"Input scores: {scores}")
    print(f"Passing score: {passing_score}")
    result = label_scores(scores, passing_score)
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
