def num_words(path):
    with open(path) as f:
        words = f.read(-1).split()

    return words
