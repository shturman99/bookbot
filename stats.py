def num_words(path):
    with open(path) as f:
        words = f.read(-1).split()

    return words

def char_count(path):
    dic = {}
    with open(path) as f:
        for line in f.readlines():
            for char in line.lower():
                #print(f"Char is {char}")
                if char in dic.keys():
                    dic[char] +=1
                else:
                    dic[char] = 1

    return dic

def sort_on(item):
    return item["count"]

def sorted_dic(dic):
    list = []
    for key, val in dic.items():
        list.append({"char":key, "count":val})

    list.sort(reverse=True, key=sort_on)

    return list
