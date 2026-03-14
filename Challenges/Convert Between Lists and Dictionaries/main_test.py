from main import list_to_dict, dict_to_list

run_cases = [
    (
        [["potion", 3], ["elixir", 1]],
        {"potion": 3, "elixir": 1},
        [["potion", 3], ["elixir", 1]],
    ),
    (
        [["gold", 100], ["silver", 50], ["bronze", 10]],
        {"gold": 100, "silver": 50, "bronze": 10},
        [["gold", 100], ["silver", 50], ["bronze", 10]],
    ),
]

submit_cases = run_cases + [
    (
        [],
        {},
        [],
    ),
    (
        [["arrow", 10], ["arrow", 25]],
        {"arrow": 25},
        [["arrow", 25]],
    ),
    (
        [["key", 1], ["map", 1], ["torch", 2]],
        {"key": 1, "map": 1, "torch": 2},
        [["key", 1], ["map", 1], ["torch", 2]],
    ),
]


def test_list_and_dict(pairs_input, expected_dict, expected_list):
    print("---------------------------------")
    print("Input list of pairs:")
    print(f"  {pairs_input}")
    print("")

    result_dict = list_to_dict(pairs_input)
    print("From list_to_dict:")
    print(f"Expected dict: {expected_dict}")
    print(f"Actual dict:   {result_dict}")

    if result_dict != expected_dict:
        print("Result: Fail")
        return False

    print("")
    print("Input dictionary for dict_to_list:")
    print(f"  {expected_dict}")
    result_list = dict_to_list(expected_dict)
    print("From dict_to_list:")
    print(f"Expected list: {expected_list}")
    print(f"Actual list:   {result_list}")

    if result_list != expected_list:
        print("Result: Fail")
        return False

    print("Result: Pass")
    return True


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)

    for test_case in test_cases:
        correct = test_list_and_dict(*test_case)
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
