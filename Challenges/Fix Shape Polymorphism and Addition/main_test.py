from main import Shape, Rectangle, Square, CompositeShape


def describe_shape(shape):
    shape_type = type(shape).__name__
    if isinstance(shape, Square):
        return f"Square(side={shape.width})"
    if isinstance(shape, Rectangle) and not isinstance(shape, Square):
        return f"Rectangle(width={shape.width}, height={shape.height})"
    if isinstance(shape, CompositeShape):
        inner = ", ".join(describe_shape(s) for s in shape.shapes)
        return f"CompositeShape([{inner}])"
    return shape_type


# Build shapes for tests
r1 = Rectangle(2, 3)          # area 6
s1 = Square(4)                # area 16
combo1 = r1 + s1              # area 22

r2 = Rectangle(3, 3)          # area 9
r3 = Rectangle(2, 5)          # area 10
s2 = Square(2)                # area 4
combo2 = CompositeShape([r2, r3, s2])  # area 23

combo3 = combo2 + Square(1)  # area 24
combo4 = combo1 + Square(1)  # area 23
combo5 = Square(5) + combo4  # area 48
combo6 = combo1 + combo2     # area 45

run_cases = [
    (r1, 6, "Rectangle(2, 3)"),
    (s1, 16, "Square(4)"),
    (combo1, 22, "Rectangle(2, 3) + Square(4)"),
]

submit_cases = run_cases + [
    (combo2, 23, "CompositeShape([Rectangle(3, 3), Rectangle(2, 5), Square(2)])"),
    (combo3, 24, "CompositeShape([...]) + Square(1)"),
    (combo5, 48, "Square(5) + (Rectangle(2, 3) + Square(4) + Square(1))"),
    (combo6, 45, "(Rectangle(2, 3) + Square(4)) + CompositeShape([...])"),
]


def test(shape, expected_area, label):
    print("---------------------------------")
    print(f"Test case: {label}")
    print(f"Input shape: {describe_shape(shape)}")
    print("")
    try:
        result = shape.area()
    except Exception as e:
        print("Error while calling area():", e)
        print("Expected area:", expected_area)
        print("Actual:   <error>")
        print("Fail")
        return False

    print(f"Expected area: {expected_area}")
    print(f"Actual area:   {result}")
    if result == expected_area:
        print("Pass")
        return True
    else:
        print("Fail")
        return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)

    for shape, expected, label in test_cases:
        correct = test(shape, expected, label)
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
