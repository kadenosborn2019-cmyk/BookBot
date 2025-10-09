from stats import get_num_words, letter_frequency, sort_by_count 
import sys

print(f"Script name:{sys.argv[0]}")
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    character_count = letter_frequency(text)
    sorted_characters = sort_by_count(character_count)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_characters:
        ch = item["char"]
        cnt = item["num"]
        if ch.isalpha():
            print(f"{ch}: {cnt}") 

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()

