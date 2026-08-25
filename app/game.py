import random
from datetime import date


LETTER_WEIGHTS = {
    "a": 8,  "b": 2,  "c": 3,  "d": 4,
    "e": 13, "f": 2,  "g": 2,  "h": 6,
    "i": 7,  "j": 1,  "k": 1,  "l": 4,
    "m": 2,  "n": 7,  "o": 8,  "p": 2,
    "q": 1,  "r": 6,  "s": 6,  "t": 9,
    "u": 3,  "v": 1,  "w": 2,  "x": 1,
    "y": 2,  "z": 1
}


def generate_letters():
    seed = int(date.today().strftime("%Y%m%d"))
    rng = random.Random(seed)

    letters = list(LETTER_WEIGHTS.keys())
    weights = list(LETTER_WEIGHTS.values())

    chosen = []

    while len(chosen) < 7:
        letter = rng.choices(
            letters,
            weights=weights,
            k=1
        )[0]

        if letter not in chosen:
            chosen.append(letter)

    return chosen

# def buttonClick(letter):
