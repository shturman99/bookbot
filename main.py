from stats import *
import sys

def get_text(path):
    with open(path) as f:
        contents = f.read(-1)

    return contents

def main():
    if len(sys.argv)<=1:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path = sys.argv[1]               
        contents = get_text(path)
        #print(contents)
        number = len(num_words(path=path))
        print(f"{number} words found in the document")
        dic = char_count(path=path)
        s_dic = sorted_dic(dic)
        #print(s_dic)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path}...")
        print("----------- Word Count ----------")
        print(f"Found {number} total words")
        print(f"--------- Character Count -------")
        for line in s_dic:
            if line['char'].isalpha():
                print(f"{line["char"]}: {line["count"]}")


main()