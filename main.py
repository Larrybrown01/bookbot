# from collections import Counter

def main():
    book_path = "bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    # num_words = get_num_words(text)
    # print(f"{num_words} words found in the document")
    chars_dict = get_chars_dict(text)
    dictionary_keys = get_dict_key_value(chars_dict)
    print(dictionary_keys)

def get_dict_key_value(dictionary):
    keys = []
    values = []
    sorted = dictionary.sort(reverse = True)
    items = sorted.items()

    for i in items:
        keys.append(i[0]), values.append(i[1])
        print(f"The {str(keys)} character was found {str(values)} times")
        keys = []
        values = []

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()





























# def main():
#     number_of_words = 0
    
#     book_path = "bookbot/books/frankenstein.txt"
#     data_uitlezen = get_book_text(book_path)
#     woorden_splitsen = data_uitlezen.split()
#     number_of_words += len(woorden_splitsen)
#     print(number_of_words)
    # lowercase = text.lower()
    # dictionary = Counter(lowercase)
    # print(f'{dictionary}')
   


# #def print_text():
#   #  book_path = "bookbot/books/frankenstein.txt"
#   #  text = get_book_text(book_path)
#   #  print(text)

# def get_book_text(path):
#     with open(path) as f:
#         return f.read()

# def word_count(book):
#     words = book.split(" ")
#     return Counter(words)



# main()

# with open(r"/Users/vincentprovoost/workspace/bookbot/books/frankenstein.txt",'r') as file:
#     data = file.read()
#     lines = data.split()
#     number_of_words += len(lines)
 
# print(number_of_words)