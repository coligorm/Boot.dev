from main import get_revenue_per_item

run_cases = [
    (
        [
            {
                "id": 1,
                "items": [
                    {"name": "health_potion", "quantity": 2},
                    {"name": "iron_sword", "quantity": 1},
                ],
            },
            {
                "id": 2,
                "items": [
                    {"name": "health_potion", "quantity": 3},
                ],
            },
        ],
        {
            "health_potion": 10,
            "iron_sword": 50,
        },
        {
            "health_potion": 50,
            "iron_sword": 50,
        },
    ),
    (
        [
            {
                "id": 1,
                "items": [
                    {"name": "magic_ring", "quantity": 1},
                ],
            },
        ],
        {
            "health_potion": 10,
        },
        {},
    ),
]

submit_cases = run_cases + [
    (
        [],
        {
            "health_potion": 10,
        },
        {},
    ),
    (
        [
            {
                "id": 10,
                "items": [
                    {"name": "mana_potion", "quantity": 5},
                    {"name": "health_potion", "quantity": 1},
                ],
            },
            {
                "id": 11,
                "items": [
                    {"name": "mana_potion", "quantity": 2},
                    {"name": "leather_armor", "quantity": 1},
                ],
            },
        ],
        {
            "mana_potion": 7,
            "health_potion": 10,
            "leather_armor": 30,
        },
        {
            "mana_potion": 49,  # (5 + 2) * 7
            "health_potion": 10,  # 1 * 10
            "leather_armor": 30,  # 1 * 30
        },
    ),
    (
        [
            {
                "id": 21,
                "items": [
                    {"name": "arrow", "quantity": 10},
                    {"name": "bow", "quantity": 1},
                ],
            },
            {
                "id": 22,
                "items": [
                    {"name": "arrow", "quantity": 15},
                    {"name": "shield", "quantity": 2},
                ],
            },
            {
                "id": 23,
                "items": [
                    {"name": "arrow", "quantity": 5},
                    {"name": "bow", "quantity": 2},
                    {"name": "shield", "quantity": 1},
                ],
            },
        ],
        {
            "arrow": 1,
            "bow": 40,
            "shield": 25,
        },
        {
            "arrow": 30,   # (10 + 15 + 5) * 1
            "bow": 120,    # (1 + 2) * 40
            "shield": 75,  # (2 + 1) * 25
        },
    ),
]


def test(orders, prices, expected_output):
    print("---------------------------------")
    print("Input orders:")
    for order in orders:
        print(f"  Order id: {order.get('id')}")
        print("    Items:")
        for item in order["items"]:
            print(
                f"      - name: {item['name']}, quantity: {item['quantity']}"
            )
    if not orders:
        print("  (no orders)")
    print("")
    print(f"Prices: {prices}")
    print("")
    result = get_revenue_per_item(orders, prices)
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
