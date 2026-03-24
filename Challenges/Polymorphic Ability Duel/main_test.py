from main import *


def build_ability(kind, name, value):
    if kind == "fire":
        return FireAbility(name, value)
    if kind == "ice":
        return IceAbility(name, value)
    return WindAbility(name, value)


def describe_ability(kind, name, value):
    if kind == "fire":
        return f"FireAbility(name={name}, flames={value})"
    if kind == "ice":
        return f"IceAbility(name={name}, shards={value})"
    return f"WindAbility(name={name}, gusts={value})"


run_cases = [
    (
        ("fire", "Meteor", 4),
        ("wind", "Breeze Kick", 2),
        [("ice", "Frost Lance", 3), ("fire", "Meteor", 4), ("wind", "Breeze Kick", 2)],
        23,
        True,
        "Meteor",
    ),
    (
        ("ice", "Glacier Spear", 5),
        ("fire", "Spark", 2),
        [("fire", "Spark", 2), ("wind", "Storm Step", 8), ("ice", "Glacier Spear", 5)],
        23,
        True,
        "Glacier Spear",
    ),
]

submit_cases = run_cases + [
    (
        ("wind", "Feather Dash", 1),
        ("fire", "Inferno", 3),
        [("wind", "Feather Dash", 1), ("fire", "Inferno", 3), ("ice", "Hail Burst", 4)],
        18,
        False,
        "Inferno",
    ),
    (
        ("ice", "Snow Pin", 2),
        ("wind", "Jet Stream", 7),
        [],
        18,
        False,
        None,
    ),
    (
        ("fire", "Blaze", 3),
        ("ice", "Shard Rain", 4),
        [("fire", "Blaze", 3), ("ice", "Shard Rain", 4), ("wind", "Rush", 7)],
        24,
        False,
        "Blaze",
    ),
]


def test(ability_one_data, ability_two_data, roster_data, expected_sum, expected_comparison, expected_strongest):
    ability_one = build_ability(*ability_one_data)
    ability_two = build_ability(*ability_two_data)

    roster = []
    for item in roster_data:
        roster.append(build_ability(*item))

    print("---------------------------------")
    print(f"Ability one: {describe_ability(*ability_one_data)}")
    print(f"Ability two: {describe_ability(*ability_two_data)}")
    print("Roster:")
    if len(roster_data) == 0:
        print("  []")
    else:
        for item in roster_data:
            print(f"  - {describe_ability(*item)}")
    print("")

    result_sum = ability_one + ability_two
    result_comparison = ability_one > ability_two
    result_strongest = get_strongest_ability(roster)

    print(f"Expected ability_one + ability_two: {expected_sum}")
    print(f"Actual ability_one + ability_two:   {result_sum}")
    print(f"Expected ability_one > ability_two: {expected_comparison}")
    print(f"Actual ability_one > ability_two:   {result_comparison}")
    print(f"Expected strongest name:            {expected_strongest}")
    print(f"Actual strongest name:              {result_strongest}")

    if result_sum != expected_sum:
        return False
    if result_comparison != expected_comparison:
        return False
    if result_strongest != expected_strongest:
        return False
    return True



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
