#gets the book and returns its contents, then counts the words
def count_words(book):
    with open(book) as f:
        file_contents = f.read()
        words = file_contents.split()
        return f"Found {len(words)} total words"

def main():
    print(count_words("books/frankenstein.txt"))

main()
