from main import *


run_cases = [
    ("start", "engine started"),
    ("stop", "engine stopped"),
    ("start", "engine started"),
]

submit_cases = run_cases + [
    ("", "unknown command"),
    ("START", "unknown command"),
    ("stop", "engine stopped"),
]


def start_engine():
    return "engine started"



def stop_engine():
    return "engine stopped"



def should_not_run():
    raise Exception("This function should not have been called")



def test(command, expected_output):
    print("---------------------------------")
    print(f"Input command: {command!r}")
    print("Start function result: 'engine started'")
    print("Stop function result:  'engine stopped'")
    print("")

    try:
        if expected_output == "unknown command":
            result = choose_command(command, should_not_run, should_not_run)
        else:
            result = choose_command(command, start_engine, stop_engine)
        print(f"Expected: {expected_output}")
        print(f"Actual:   {result}")
        if result == expected_output:
            return True
        return False
    except Exception as e:
        print(f"Expected: {expected_output}")
        print(f"Actual error: {e}")
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
