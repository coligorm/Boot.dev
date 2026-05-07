from main import *

run_cases = [
    (
        "Nova",
        [
            {"type": "mine", "item": "iron", "amount": 3, "energy": 4},
            {"type": "hit", "damage": 20},
            {"type": "charge", "energy": 5},
        ],
        {
            "pilot": "Nova",
            "health": 80,
            "energy": 11,
            "cargo": {"iron": 3},
            "cargo_text": "iron:3",
            "log": [
                "Mined iron x3",
                "Took 20 damage",
                "Charged 5 energy",
            ],
        },
    ),
    (
        "Orion",
        [
            {"type": "mine", "item": "ice", "amount": 2, "energy": 11},
            {"type": "charge", "energy": 4},
            {"type": "mine", "item": "ice", "amount": 2, "energy": 11},
        ],
        {
            "pilot": "Orion",
            "health": 100,
            "energy": 3,
            "cargo": {"ice": 2},
            "cargo_text": "ice:2",
            "log": [
                "Skipped ice",
                "Charged 4 energy",
                "Mined ice x2",
            ],
        },
    ),
]

submit_cases = run_cases + [
    (
        "Patch",
        [
            {"type": "hit", "damage": 10},
            {"type": "repair", "health": 50},
        ],
        {
            "pilot": "Patch",
            "health": 100,
            "energy": 10,
            "cargo": {},
            "cargo_text": "empty",
            "log": [
                "Took 10 damage",
                "Repaired 50 health",
            ],
        },
    ),
    (
        "Crash",
        [
            {"type": "hit", "damage": 120},
            {"type": "charge", "energy": 50},
            {"type": "mine", "item": "gold", "amount": 1, "energy": 2},
        ],
        {
            "pilot": "Crash",
            "health": 0,
            "energy": 10,
            "cargo": {},
            "cargo_text": "empty",
            "log": [
                "Took 120 damage",
                "Ship destroyed",
            ],
        },
    ),
    (
        "Atlas",
        [
            {"type": "mine", "item": "iron", "amount": 2, "energy": 3},
            {"type": "mine", "item": "ice", "amount": 4, "energy": 2},
            {"type": "hit", "damage": 35},
            {"type": "repair", "health": 10},
            {"type": "charge", "energy": 6},
            {"type": "mine", "item": "iron", "amount": 5, "energy": 7},
        ],
        {
            "pilot": "Atlas",
            "health": 75,
            "energy": 4,
            "cargo": {"iron": 7, "ice": 4},
            "cargo_text": "iron:7, ice:4",
            "log": [
                "Mined iron x2",
                "Mined ice x4",
                "Took 35 damage",
                "Repaired 10 health",
                "Charged 6 energy",
                "Mined iron x5",
            ],
        },
    ),
]


def format_events(events):
    lines = []
    for event in events:
        if event["type"] == "mine":
            lines.append(
                f"  - mine item={event['item']} amount={event['amount']} energy={event['energy']}"
            )
        elif event["type"] == "hit":
            lines.append(f"  - hit damage={event['damage']}")
        elif event["type"] == "charge":
            lines.append(f"  - charge energy={event['energy']}")
        elif event["type"] == "repair":
            lines.append(f"  - repair health={event['health']}")
    return "\n".join(lines)


def test(name, events, expected_output):
    print("---------------------------------")
    print(f"Pilot: {name}")
    print("Events:")
    print(format_events(events))
    print("")
    result = simulate_mission(name, events)
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
