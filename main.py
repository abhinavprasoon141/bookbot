from stats import get_book_text , word_count , letter_count , sorted_dict
from operator import itemgetter

if __name__ == "__main__":
    filepath = "/Users/abhinavprasoon/Desktop/programming/bookbot/bookbot/books/frankenstein.txt"

    book_text = get_book_text(filepath)
    num_words = word_count(book_text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    list = sorted_dict(letter_count(book_text))
    for item in sorted(list, key=lambda x: x["num"], reverse=True):
        d1 = {item["char"]:item["num"]}
        for key, value in d1.items():
            print("{}: {}".format(key,value))
    print("============= END ===============")
