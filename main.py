from stats import *
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return str(file_contents)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


    bookPath = sys.argv[1]
    bookText = get_book_text(bookPath)
    num_words = get_num_words(bookText)
    num_letters = get_num_letters(bookText)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {bookPath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in num_letters:
        print(f"{item['letter']}: {item['num']}")
    print("============= END ===============")


main()