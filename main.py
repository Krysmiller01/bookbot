from stats import count_words 
from stats import count_char
from stats import sort_on
from stats import sorted_list
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path = sys.argv[1]

def report(book):
    count = count_words(path)
    list_of_dict = sorted_list(path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"{count}")
    print("--------- Character Count -------")
    for item in list_of_dict:
        ch = item["char"]
        count = item["val"]
        if ch.isalpha():
            print(f"{ch}: {count}")
    print("============= END ===============")


def main():
    report(path)

main()