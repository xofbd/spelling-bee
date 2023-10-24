#!/usr/bin/env python3
import pickle
import re

from trie import CharTrie

MIN_WORD_LENGTH = 4


def load_dict(path):
    with open(path, "r") as f:
        for line in f:
            yield line.strip().lower()


def build(path):
    trie = CharTrie(data=[])

    for word in load_dict(path):
        if len(word) < MIN_WORD_LENGTH or re.search(r"^[a-zA-Z]+$", word) is None:
            continue

        signature = sorted(set(word))

        if trie[signature] is None:
            trie[signature] = []
        trie[signature].append(word)

    return trie


def dump_trie(trie, path):
    with open(path, "wb") as f:
        pickle.dump(trie, f)


def main(path_in, path_out):
    trie = build(path_in)
    dump_trie(trie, path_out)


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser = ArgumentParser(description="Build trie data structure from dictionary")
    parser.add_argument(
        "-d",
        "--dict",
        help="path to the dictionary to build the trie",
        metavar="dictionary",
        dest="path_in",
        default="/usr/share/dict/words",
    )
    parser.add_argument(
        "-o",
        "--output",
        help="path of the output file of the trie",
        dest="path_out",
        default="data/trie.pkl",
    )
    args = parser.parse_args()

    main(args.path_in, args.path_out)
