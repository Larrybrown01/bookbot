# from typing import Counter


def main():
    number_of_words = 0
    
    book_path = "bookbot/books/frankenstein.txt"
    data_uitlezen = get_book_text(book_path)
    woorden_splitsen = data_uitlezen.split()
    number_of_words += len(woorden_splitsen)
    print(number_of_words)
   


# #def print_text():
#   #  book_path = "bookbot/books/frankenstein.txt"
#   #  text = get_book_text(book_path)
#   #  print(text)

def get_book_text(path):
    with open(path) as f:
        return f.read()

# def word_count(book):
#     words = book.split(" ")
#     return Counter(words)



main()

# with open(r"/Users/vincentprovoost/workspace/bookbot/books/frankenstein.txt",'r') as file:
#     data = file.read()
#     lines = data.split()
#     number_of_words += len(lines)
 
# print(number_of_words)