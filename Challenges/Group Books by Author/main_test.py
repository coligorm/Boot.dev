from main import *


run_cases = [
    (
        [
            {"title": "The Hobbit", "author": "J.R.R. Tolkien"},
            {"title": "The Fellowship of the Ring", "author": "J.R.R. Tolkien"},
            {"title": "1984", "author": "George Orwell"},
        ],
        {
            "J.R.R. Tolkien": ["The Hobbit", "The Fellowship of the Ring"],
            "George Orwell": ["1984"],
        },
    ),
    (
        [
            {"title": "Dune", "author": "Frank Herbert"},
            {"title": "Dune Messiah", "author": "Frank Herbert"},
            {"title": "Foundation", "author": "Isaac Asimov"},
            {"title": "I, Robot", "author": "Isaac Asimov"},
        ],
        {
            "Frank Herbert": ["Dune", "Dune Messiah"],
            "Isaac Asimov": ["Foundation", "I, Robot"],
        },
    ),
    (
        [],
        {},
    ),
]

submit_cases = run_cases + [
    (
        [
            {"title": "Animal Farm", "author": "George Orwell"},
            {"title": "The Silmarillion", "author": "J.R.R. Tolkien"},
            {"title": "Homage to Catalonia", "author": "George Orwell"},
        ],
        {
            "George Orwell": ["Animal Farm", "Homage to Catalonia"],
            "J.R.R. Tolkien": ["The Silmarillion"],
        },
    ),
    (
        [
            {"title": "Book A", "author": "Author One"},
            {"title": "Book B", "author": "Author Two"},
            {"title": "Book C", "author": "Author Three"},
        ],
        {
            "Author One": ["Book A"],
            "Author Two": ["Book B"],
            "Author Three": ["Book C"],
        },
    ),
    (
        [
            {"title": "Repeat", "author": "Same Author"},
            {"title": "Repeat", "author": "Same Author"},
            {"title": "Another", "author": "Same Author"},
        ],
        {
            "Same Author": ["Repeat", "Repeat", "Another"],
        },
    ),
]


def test(books, expected_output):
    print("---------------------------------")
    print("Input books:")
    for book in books:
        print(f"  - title='{book['title']}', author='{book['author']}'")
    if not books:
        print("  (no books)")
    print("")
    result = group_books_by_author(books)
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
