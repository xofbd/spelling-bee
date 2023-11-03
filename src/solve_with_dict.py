def load_dict(path):
    with open(path, "r") as f:
        for line in f:
            yield line.strip().lower()


def check(center_letter, letters, word):
    if len(word) < 4:
        return False

    if center_letter not in word:
        return False

    if not (set(word) - letters):
        return True

    return False


def solve(letters, dict_):
    center_letter = letters[0]
    letters = set(letters)

    return {word for word in dict_ if check(center_letter, letters, word)}
