from main import *


run_cases = [
    (
        Pack([Dog("Rex"), Cat("Milo")]),
        ["Dog: Rex says woof", "Cat: Milo says meow"],
    ),
    (
        Pack([Parrot("Kiwi")]),
        ["Parrot: Kiwi says squawk"],
    ),
    (
        Pack([Dog("Rex")]) + Pack([Parrot("Kiwi")]),
        ["Dog: Rex says woof", "Parrot: Kiwi says squawk"],
    ),
]

submit_cases = run_cases + [
    (Dog("Rex") == Cat("Rex"), False),
    (Pack([]) + Pack([Cat("Luna")]), ["Cat: Luna says meow"]),
    (
        Pack([Dog("Rex"), Cat("Milo")]) + Pack([Parrot("Kiwi"), Dog("Nova")]),
        [
            "Dog: Rex says woof",
            "Cat: Milo says meow",
            "Parrot: Kiwi says squawk",
            "Dog: Nova says woof",
        ],
    ),
]


def format_pack(pack):
    if isinstance(pack, bool):
        return str(pack)
    if not pack.animals:
        return "  (empty)"
    lines = []
    for animal in pack.animals:
        lines.append(f"  - {animal.__class__.__name__}(name={animal.name})")
    return "\n".join(lines)


def test_pack(pack, expected_output):
    print("---------------------------------")
    print("Input pack:")
    print(format_pack(pack))
    print("")
    result = pack.sounds()
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    if result == expected_output:
        return True
    return False


def test_equality(result, expected_output):
    print("---------------------------------")
    print("Input:")
    print("  Dog(name=Rex) == Cat(name=Rex)")
    print("")
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
        if isinstance(test_case[0], bool):
            correct = test_equality(*test_case)
        else:
            correct = test_pack(*test_case)
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
