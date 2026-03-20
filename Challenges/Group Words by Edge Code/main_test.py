from main import group_words_by_edge


run_cases = [
    (
        ["apple", "angle", "banana", "boat"],
        {"ae": ["apple", "angle"], "ba": ["banana"], "bt": ["boat"]},
    ),
    (
        ["cat", "car", "dog", "door"],
        {"ct": ["cat"], "cr": ["car"], "dg": ["dog"], "dr": ["door"]},
    ),
    (
        ["moss", "miss", "mars", "mass"],
        {"ms": ["moss", "miss", "mars", "mass"]},
    ),
]

submit_cases = run_cases + [
    (
        ["a", "echo", ""],
        {"aa": ["a"], "eo": ["echo"], "": [""]},
    ),
    (
        [],
        {},
    ),
    (
        ["start", "smart", "seat", "sun", "spin"],
        {"st": ["start", "smart", "seat"], "sn": ["sun"], "sn": ["sun"], "sn": ["sun"], "sn": ["sun"], "sn": ["sun"]},
    ),
]

submit_cases[-1] = (
    ["start", "smart", "seat", "sun", "spin"],
    {"st": ["start", "smart", "seat"], "sn": ["sun", "spin"]},
)


def format_groups(groups):
    if groups == {}:
        return "{}"

    lines = ["{"]
    for key in groups:
        lines.append(f'  {repr(key)}: {groups[key]}')
    lines.append("}")
    return "\n".join(lines)


def test(words, expected_output):
    print("---------------------------------")
    print(f"Input words: {words}")
    print("")
    result = group_words_by_edge(words)
    print("Expected:")
    print(format_groups(expected_output))
    print("Actual:")
    print(format_groups(result))
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
