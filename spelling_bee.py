#!/usr/bin/env python3

def load_dict(path):
    with open(path, "r") as f:
        for line in f:
            yield line.strip().lower()


def solve(letters, dict_):
    center_letter = letters[0]
    letters = set(letters)

    return [word for word in dict_ if check(center_letter, letters, word)]


def check(center_letter, letters, word):
    if len(word) < 4:
        return False

    if center_letter not in word:
        return False

    if not (set(word) - letters):
        return True

    return False


def print_results(words):
    """Print words in sorted order by score"""

    for word in sorted(words, key=lambda word: (-score(word), word)):
        print(word)


def score(word):
    if len(word) == 4:
        return 1

    bonus = 7 if len(word) >= 7 else 0

    return len(word) + bonus


def main(letters, dict_path):
    dict_ = load_dict(dict_path)
    words = solve(letters.lower(), dict_)
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
        help="path to the dictionary to search through",
        metavar="dictionary",
        dest="dict_path",
        default="/usr/share/dict/words"
    )
    args = parser.parse_args()

    main(args.letters, args.dict_path)
