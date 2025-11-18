import sys
from stats import word_count, char_count, sort_characters
from bookbot import get_book_text

def main():
    # Check if a book path argument was passed
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    text = get_book_text(book_path)

    # ----- WORD COUNT -----
    num_words = word_count(text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    # ----- CHARACTER COUNT -----
    characters = char_count(text)
    sorted_characters = sort_characters(characters)

    print("--------- Character Count -------")
    for item in sorted_characters:
        if item["char"].isalpha():  # only alphabetical
            print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

main()
