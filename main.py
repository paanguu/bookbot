import sys
from stats import find_num_words, find_each_char, sort_dictionary

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    book_text = get_book_text(file_path)
    num_words = find_num_words(book_text)
    char_counts = find_each_char(book_text)
    sorted_char_list = sort_dictionary(char_counts)

    print(f"""
    ============ BOOKBOT ============
Analyzing book found at {file_path}
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------""")

    for x in sorted_char_list:
        if not x["char"].isalpha():
            continue
        print(f"{x["char"]}: {x["count"]}")

    print("============= END ===============")



main()