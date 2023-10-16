#!/usr/bin/env python3

def load_vocab(path):
    with open(path, "r") as f:
        for line in f:
            yield line.strip().lower()


def solve(letters, vocab):
    center_letter = letters[0]
    letters = set(letters)

    return [word for word in vocab if check(center_letter, letters, word)]


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


def main(letters, vocab_path):
    vocab = load_vocab(vocab_path)
    words = solve(letters.lower(), vocab)
    print_results(words)


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser(description="Find valid words in spelling bee")
    parser.add_argument(
        "letters",
        help="letters to use with the center letter first"
    )
    parser.add_argument(
        "--vocab",
        help="path to the vocabulary to search through",
        metavar="vocab",
        dest="vocab_path",
        default="/usr/share/dict/words"
    )
    args = parser.parse_args()

    main(args.letters, args.vocab_path)
