from main import *

run_cases = [
    # age, has_id, is_vip, has_coupon, expected
    (25, True, True, False, "VIP-21"),
    (17, True, False, False, "STANDARD-TEEN"),
    (19, True, False, True, "DISCOUNT"),
]

submit_cases = run_cases + [
    (-1, True, False, False, "invalid age"),
    (15, True, True, True, "not allowed"),
    (30, True, False, False, "STANDARD-ADULT"),
]


def test(age, has_id, is_vip, has_coupon, expected_output):
    print("---------------------------------")
    print("Input:")
    print(f"  age:        {age}")
    print(f"  has_id:     {has_id}")
    print(f"  is_vip:     {is_vip}")
    print(f"  has_coupon: {has_coupon}")
    print("")
    result = get_ticket_type(age, has_id, is_vip, has_coupon)
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
