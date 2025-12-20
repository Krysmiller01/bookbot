#gets the book and returns its contents, then counts the words
def count_words(book):
    with open(book) as f:
        file_contents = f.read()
        words = file_contents.split()
        return f"Found {len(words)} total words"


#takes book and counts each character and makes a dictionary
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

#calls on val
def sort_on(item):
    return item["val"]

#takes the dictionary of count_char and turns into a list
def sorted_list(characters):
    dictionary = count_char(characters)
    the_list = []
    for char in dictionary:
        value = dictionary[char]
        nm = {
            f"name": char,
            f"val": value
        }
        the_list.append(nm)
    
    the_list.sort(reverse=True, key=sort_on)
    return the_list



def main():
    print(count_words("books/frankenstein.txt"))
    print(sorted_list("books/frankenstein.txt"))
main()
