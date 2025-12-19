#gets the book and returns its contents, then counts the words
def count_words(book):
    with open(book) as f:
        file_contents = f.read()
        words = file_contents.split()
        return f"Found {len(words)} total words"

#takes book and counts each character by updating a dictionary
def count_char(book):
    with open(book) as f:
        file_contents = f.read()
        book_in_lowcase = file_contents.lower()
        char_in_book = list(book_in_lowcase)
        #Officially a list of lowercase characters in list
        char_dict = {}
        for char in char_in_book:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
        return char_dict

def main():
    print(count_words("books/frankenstein.txt"))
    print(count_char("books/frankenstein.txt"))
main()
