from curses.ascii import isalpha
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()

        return file_contents

def word_count(book):
     x = book.split()

     return len(x)

def letter_count(book):
    b1 = book.lower()
    dict ={}
    for char in set(b1):
        count=0
        for i in b1:
            if i == char:
                count+=1
        dict[char]=count

    return dict

def sorted_dict(dict):
    list =[]
    for key in sorted(dict.keys()):
        if isalpha(key):
            list.append({"char" : key, "num": dict[key]})

    return list
