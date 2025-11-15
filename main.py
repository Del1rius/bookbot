from stats import get_num_words, get_char_counts

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    text = get_book_text("books/frankenstein.txt")

    num_words = get_num_words(text)
    print(f"Found {num_words} total words")

    char_counts = get_char_counts(text)
    print(char_counts)

main()