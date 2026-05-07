from main import *

run_cases = [
    (5, "00000101", 0b00101101, 0b00100100, True, 0b00010000, 0b00000101, 0b00010101),
    (255, "11111111", 0b00000000, 0b00000001, False, 0b00000000, 0b00000000, 0b00000000),
    (128, "10000000", 0b01010101, 0b00000100, True, 0b01000000, 0b00000011, 0b01000011),
]

submit_cases = run_cases + [
    (0, "00000000", 0b11110000, 0b00001111, False, 0b10101010, 0b01010101, 0b11111111),
    (170, "10101010", 0b00001111, 0b00000000, True, 0b00000001, 0b10000000, 0b10000001),
    (15, "00001111", 0b11111111, 0b00001010, True, 0b00110000, 0b00001111, 0b00111111),
]


def test_case(n, expected_binary, value, flags, expected_has, base, add, expected_added):
    print("---------------------------------")
    print("Inputs:")
    print(f"  n     = {n} ({bin(n)})")
    print(f"  value = {value} ({bin(value)})")
    print(f"  flags = {flags} ({bin(flags)})")
    print(f"  base  = {base} ({bin(base)})")
    print(f"  add   = {add} ({bin(add)})")

    result_binary = to_8bit_binary(n)
    result_has = has_all_flags(value, flags)
    result_added = add_flags(base, add)

    print("\nExpected:")
    print(f"  to_8bit_binary(n)     = {expected_binary}")
    print(f"  has_all_flags(v,f)    = {expected_has}")
    print(f"  add_flags(base, add)  = {expected_added} ({bin(expected_added)})")

    print("\nActual:")
    print(f"  to_8bit_binary(n)     = {result_binary}")
    print(f"  has_all_flags(v,f)    = {result_has}")
    print(f"  add_flags(base, add)  = {result_added} ({bin(result_added)})")

    if result_binary != expected_binary:
        return False
    if result_has != expected_has:
        return False
    if result_added != expected_added:
        return False
    return True


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)

    for tc in test_cases:
        correct = test_case(*tc)
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
