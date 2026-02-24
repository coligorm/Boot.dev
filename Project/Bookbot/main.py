import sys
from stats import count_words, count_characters, get_sorted_dict

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()

        # Read file task
        # print(file_contents)

        # Count Words task
        num_words = count_words(file_contents)
        # print(f"Found {num_words} total words")

        # Count Characters task
        char_count = count_characters(file_contents)
        # print(char_count)

        # Print Report Task
        sorted_dicts = get_sorted_dict(char_count)

        print_report(path_to_file, num_words, sorted_dicts)

def print_report(path_to_book, w_count, c_count):
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}")
    print(f"----------- Word Count ----------")
    print(f"Found {w_count} total words")
    print(f"--------- Character Count -------")
    
    for d in c_count:
        print(f"{d['char']}: {d['num']}")
    
    print(f"============= END ===============")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    get_book_text(sys.argv[1])


main()