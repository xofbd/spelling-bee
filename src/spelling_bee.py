#!/usr/bin/env python3
from solve_with_dict import load_dict, solve as solve_with_dict
from solve_with_trie import load_trie, solve as solve_with_trie


def print_results(words):
    """Print words in sorted order by score"""
    for word in sorted(words, key=lambda word: (-score(word), word)):
        print(word)


def score(word):
    if len(word) == 4:
        return 1

    bonus = 7 if len(word) >= 7 else 0

    return len(word) + bonus


def main(letters, ds_path):
    if ds_path.endswith(".pkl"):
        solver = solve_with_trie
        loader = load_trie
    else:
        solver = solve_with_dict
        loader = load_dict

    data_structure = loader(ds_path)
    words = solver(letters.lower(), data_structure)
    print_results(words)


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser(description="Find valid words in spelling bee")
    parser.add_argument(
        "letters",
        help="letters to use with the center letter first"
    )
    parser.add_argument(
        "-d",
        "--dict",
        help="path to the dictionary or trie to search through",
        dest="ds_path",
        default="/usr/share/dict/words"
    )
    args = parser.parse_args()

    main(args.letters, args.ds_path)
