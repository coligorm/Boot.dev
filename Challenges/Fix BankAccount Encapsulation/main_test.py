from main import BankAccount


def fmt_account(acct):
    return (
        "BankAccount(\n"
        f"  owner_name: {acct.get_owner_name()}\n"
        f"  account_number: {acct.get_account_number()}\n"
        f"  balance: {acct.get_balance()}\n"
        f"  daily_withdraw_limit: {acct.get_daily_withdraw_limit()}\n"
        f"  transactions: {acct.get_transactions()}\n"
        ")"
    )


def test_unique_account_numbers(starting_next, owners, expected_numbers):
    print("---------------------------------")
    print("Test: unique account numbers")
    print(f"Input starting BankAccount.next_account_number: {starting_next}")
    print(f"Input owners: {owners}")
    print("")

    BankAccount.next_account_number = starting_next

    accounts = []
    for name in owners:
        accounts.append(BankAccount(name))

    actual_numbers = []
    for a in accounts:
        actual_numbers.append(a.get_account_number())

    print(f"Expected account_numbers: {expected_numbers}")
    print(f"Actual account_numbers:   {actual_numbers}")

    if actual_numbers == expected_numbers:
        print("Pass")
        return True
    print("Fail")
    return False


def test_daily_limit_is_instance_state():
    print("---------------------------------")
    print("Test: daily withdraw limit is per-account")

    BankAccount.next_account_number = 1000
    BankAccount.default_daily_withdraw_limit = 200

    a = BankAccount("Ava")
    b = BankAccount("Ben")

    a.set_daily_withdraw_limit(50)

    print("\nInput:")
    print("  * default_daily_withdraw_limit:", BankAccount.default_daily_withdraw_limit)
    print("  * a.set_daily_withdraw_limit(50)")
    print("\nExpected:")
    print("  * a.get_daily_withdraw_limit() == 50")
    print("  * b.get_daily_withdraw_limit() == 200")
    print("  * BankAccount.default_daily_withdraw_limit == 200")

    ok = True
    if a.get_daily_withdraw_limit() != 50:
        ok = False
    if b.get_daily_withdraw_limit() != 200:
        ok = False
    if BankAccount.default_daily_withdraw_limit != 200:
        ok = False

    print("\nActual:")
    print("  * a.get_daily_withdraw_limit() =", a.get_daily_withdraw_limit())
    print("  * b.get_daily_withdraw_limit() =", b.get_daily_withdraw_limit())
    print("  * BankAccount.default_daily_withdraw_limit =", BankAccount.default_daily_withdraw_limit)

    if ok:
        print("Pass")
        return True
    print("Fail")
    return False


def test_transactions_are_not_mutable_from_outside():
    print("---------------------------------")
    print("Test: get_transactions does not leak internal list")

    BankAccount.next_account_number = 1000
    acct = BankAccount("Nora")
    acct.deposit(10)
    acct.withdraw(5)

    external = acct.get_transactions()
    external.append({"type": "hack", "amount": 999})

    expected = [{"type": "deposit", "amount": 10}, {"type": "withdraw", "amount": 5}]
    actual = acct.get_transactions()

    print("\nInput:")
    print(fmt_account(acct))
    print("\nAction:")
    print("  external = acct.get_transactions()")
    print("  external.append({type: 'hack', amount: 999})")
    print("\nExpected acct.get_transactions():")
    print(expected)
    print("Actual acct.get_transactions():")
    print(actual)

    if actual == expected:
        print("Pass")
        return True
    print("Fail")
    return False


def test_happy_path_summary():
    print("---------------------------------")
    print("Test: happy path account behavior")

    BankAccount.next_account_number = 7000
    BankAccount.default_daily_withdraw_limit = 200

    acct = BankAccount("Kai")
    acct.deposit(100)
    acct.set_daily_withdraw_limit(80)
    acct.withdraw(60)

    expected_balance = 40
    expected_number = 7000
    expected_limit = 80

    print("\nInput actions:")
    print("  * acct = BankAccount('Kai')")
    print("  * acct.deposit(100)")
    print("  * acct.set_daily_withdraw_limit(80)")
    print("  * acct.withdraw(60)")

    print("\nExpected:")
    print("  * account_number:", expected_number)
    print("  * daily_withdraw_limit:", expected_limit)
    print("  * balance:", expected_balance)

    print("\nActual:")
    print("  * account_number:", acct.get_account_number())
    print("  * daily_withdraw_limit:", acct.get_daily_withdraw_limit())
    print("  * balance:", acct.get_balance())

    ok = True
    if acct.get_account_number() != expected_number:
        ok = False
    if acct.get_daily_withdraw_limit() != expected_limit:
        ok = False
    if acct.get_balance() != expected_balance:
        ok = False

    if ok:
        print("Pass")
        return True
    print("Fail")
    return False


run_cases = [
    ("unique_numbers", 1000, ["Ava", "Ben", "Cal"], [1000, 1001, 1002]),
    ("daily_limit_instance",),
]

submit_cases = run_cases + [
    ("transactions_copy",),
    ("unique_numbers", 42, ["X", "Y"], [42, 43]),
    ("happy_path",),
]


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)

    for case in test_cases:
        name = case[0]
        if name == "unique_numbers":
            correct = test_unique_account_numbers(case[1], case[2], case[3])
        elif name == "daily_limit_instance":
            correct = test_daily_limit_is_instance_state()
        elif name == "transactions_copy":
            correct = test_transactions_are_not_mutable_from_outside()
        elif name == "happy_path":
            correct = test_happy_path_summary()
        else:
            print("Unknown test case:", case)
            correct = False

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
