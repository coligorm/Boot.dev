from main import *

run_cases = [
    (
        [
            {"name": "Ava", "active": True, "spend": 120, "tier": "gold"},
            {"name": "Ben", "active": False, "spend": 300, "tier": "platinum"},
            {"name": "Cora", "active": True, "spend": 100, "tier": "silver"},
        ],
        100,
        ["AVA (gold)", "CORA (silver)"],
    ),
    (
        [
            {"name": "Milo", "active": True, "spend": 80, "tier": "bronze"},
            {"name": "Nia", "active": True, "spend": 140, "tier": "gold"},
            {"name": "Omar", "active": True, "spend": 200, "tier": "platinum"},
        ],
        120,
        ["NIA (gold)", "OMAR (platinum)"],
    ),
]

submit_cases = run_cases + [
    (
        [],
        50,
        [],
    ),
    (
        [
            {"name": "Ivy", "active": False, "spend": 500, "tier": "gold"},
            {"name": "Jae", "active": True, "spend": 40, "tier": "silver"},
        ],
        100,
        [],
    ),
    (
        [
            {"name": "Lena", "active": True, "spend": 100, "tier": "silver"},
            {"name": "Pia", "active": True, "spend": 250, "tier": "gold"},
            {"name": "Quin", "active": False, "spend": 400, "tier": "platinum"},
            {"name": "Rae", "active": True, "spend": 180, "tier": "gold"},
        ],
        100,
        ["LENA (silver)", "PIA (gold)", "RAE (gold)"],
    ),
]


def format_records(records):
    if len(records) == 0:
        return "  (empty)"

    lines = []
    for record in records:
        line = (
            "  * "
            + record["name"]
            + " | active="
            + str(record["active"])
            + " | spend="
            + str(record["spend"])
            + " | tier="
            + record["tier"]
        )
        lines.append(line)
    return "\n".join(lines)


def test(records, minimum_spend, expected_output):
    print("---------------------------------")
    print("Input records:")
    print(format_records(records))
    print(f"Minimum spend: {minimum_spend}")
    print("")
    result = get_priority_member_labels(records, minimum_spend)
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
