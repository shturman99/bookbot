from stats import *

def get_text(path):
    with open(path) as f:
        contents = f.read(-1)

    return contents

def main():
    contents = get_text("books/frankenstein.txt")
    #print(contents)
    number = len(num_words("books/frankenstein.txt"))
    print(f"{number} words found in the document")

main()