from itertools import combinations
import pickle


def load_trie(path):
    with open(path, "rb") as f:
        return pickle.load(f)


def gen_signatures(letters):
    middle_char = letters[0]
    letters = letters[1:]

    for k in range(1, len(letters) + 1):
        for signature in combinations(letters, k):
            yield sorted((middle_char,) + signature)


def solve(letters, trie):
    words = set()

    for signature in gen_signatures(letters):
        words.update(trie.get(signature, []))

    return words
