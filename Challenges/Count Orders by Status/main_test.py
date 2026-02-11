from main import *

run_cases = [
    (
        [
            {"id": 1, "status": "shipped"},
            {"id": 2, "status": "processing"},
            {"id": 3, "status": "shipped"},
        ],
        {"shipped": 2, "processing": 1},
    ),
    (
        [
            {"id": 10, "status": "pending"},
            {"id": 11, "status": "pending"},
            {"id": 12, "status": "canceled"},
        ],
        {"pending": 2, "canceled": 1},
    ),
]

submit_cases = run_cases + [
    (
        [],
        {},
    ),
    (
        [
            {"id": 100, "status": "processing"},
            {"id": 101, "status": "processing"},
            {"id": 102, "status": "processing"},
        ],
        {"processing": 3},
    ),
    (
        [
            {"id": 5, "status": "shipped"},
            {"id": 6, "status": "delivered"},
            {"id": 7, "status": "returned"},
            {"id": 8, "status": "delivered"},
            {"id": 9, "status": "shipped"},
        ],
        {"shipped": 2, "delivered": 2, "returned": 1},
    ),
]


def test(input_orders, expected_output):
    print("---------------------------------")
    print("Input orders:")
    for order in input_orders:
        print(f"  id={order['id']}, status={order['status']}")
    if not input_orders:
        print("  (no orders)")
    print("")
    result = count_orders_by_status(input_orders)
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
