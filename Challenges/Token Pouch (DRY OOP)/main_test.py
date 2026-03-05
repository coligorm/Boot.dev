from main import TokenPouch


def expect_raises(error_type, fn):
    try:
        fn()
    except Exception as e:
        print(f"Error: {e}")
        return type(e) is error_type
    return False


def test_happy_path_deposit_withdraw(starting, deposit_amount, withdraw_amount, expected_tokens):
    print("---------------------------------")
    print("Input:")
    print(f"  starting_tokens: {starting}")
    print(f"  deposit: {deposit_amount}")
    print(f"  withdraw: {withdraw_amount}")
    pouch = TokenPouch(starting)
    pouch.deposit(deposit_amount)
    result = pouch.withdraw(withdraw_amount)
    print(f"Expected tokens: {expected_tokens}")
    print(f"Actual tokens:   {result}")
    return result == expected_tokens and pouch.tokens == expected_tokens


def test_happy_path_transfer(a_start, b_start, amount, expected_a, expected_b):
    print("---------------------------------")
    print("Input:")
    print(f"  pouch_a starting_tokens: {a_start}")
    print(f"  pouch_b starting_tokens: {b_start}")
    print(f"  transfer amount: {amount}")
    a = TokenPouch(a_start)
    b = TokenPouch(b_start)
    result = a.transfer_to(b, amount)
    print(f"Expected return: ({expected_a}, {expected_b})")
    print(f"Actual return:   {result}")
    print(f"Expected tokens: a={expected_a}, b={expected_b}")
    print(f"Actual tokens:   a={a.tokens}, b={b.tokens}")
    return result == (expected_a, expected_b) and a.tokens == expected_a and b.tokens == expected_b


def test_invalid_amounts():
    print("---------------------------------")
    print("Input:")
    print("  starting_tokens: 5")
    print("  invalid deposit amount: 0")
    print("  invalid withdraw amount: -2")
    pouch = TokenPouch(5)

    ok1 = expect_raises(ValueError, lambda: pouch.deposit(0))
    ok2 = expect_raises(ValueError, lambda: pouch.withdraw(-2))

    print("Expected: both operations raise ValueError")
    print(f"Actual:   deposit(0) ValueError={ok1}, withdraw(-2) ValueError={ok2}")
    return ok1 and ok2


def test_insufficient_funds_withdraw():
    print("---------------------------------")
    print("Input:")
    print("  starting_tokens: 2")
    print("  withdraw amount: 3")
    pouch = TokenPouch(2)
    ok = expect_raises(ValueError, lambda: pouch.withdraw(3))
    print("Expected: withdraw raises ValueError")
    print(f"Actual:   ValueError={ok}")
    return ok


def test_transfer_invalid_other_type():
    print("---------------------------------")
    print("Input:")
    print("  pouch_a starting_tokens: 5")
    print("  other_pouch: 'not a pouch'")
    print("  transfer amount: 1")
    a = TokenPouch(5)
    ok = expect_raises(TypeError, lambda: a.transfer_to("not a pouch", 1))
    print("Expected: transfer_to raises TypeError")
    print(f"Actual:   TypeError={ok}")
    return ok


def test_big_happy_path_sequence():
    print("---------------------------------")
    print("Input:")
    print("  pouch_a starting_tokens: 100")
    print("  pouch_b starting_tokens: 25")
    print("  operations:")
    print("    a.withdraw(30)")
    print("    b.deposit(10)")
    print("    a.transfer_to(b, 50)")
    a = TokenPouch(100)
    b = TokenPouch(25)

    a.withdraw(30)
    b.deposit(10)
    result = a.transfer_to(b, 50)

    expected_a = 20
    expected_b = 85

    print(f"Expected return: ({expected_a}, {expected_b})")
    print(f"Actual return:   {result}")
    print(f"Expected tokens: a={expected_a}, b={expected_b}")
    print(f"Actual tokens:   a={a.tokens}, b={b.tokens}")
    return result == (expected_a, expected_b) and a.tokens == expected_a and b.tokens == expected_b


run_cases = [
    ("happy deposit+withdraw", test_happy_path_deposit_withdraw, (10, 5, 3, 12)),
    ("happy transfer", test_happy_path_transfer, (10, 3, 4, 6, 7)),
    ("invalid amounts", test_invalid_amounts, ()),
]

submit_cases = run_cases + [
    ("insufficient withdraw", test_insufficient_funds_withdraw, ()),
    ("transfer invalid other type", test_transfer_invalid_other_type, ()),
    ("big happy path sequence", test_big_happy_path_sequence, ()),
]


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)

    for name, fn, args in test_cases:
        print(f"TEST: {name}")
        correct = fn(*args)
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
