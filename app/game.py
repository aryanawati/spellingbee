import random
from datetime import date
import json
from pathlib import Path

WORD_FILE = Path(__file__).parent.parent / "assets" / "dictionaries" / "words_dictionary.json"

with open(WORD_FILE, "r") as file:
    words = json.load(file)

VALID_WORDS = set(words)

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

def update_score(word):
    return len(word) * 100

letters = generate_letters()
centerLetter = letters[3]
usedWords = []

def is_valid_word(word, letters, center_letter):
    word = word.lower()
    if word in VALID_WORDS:
        if len(word) < 4:
            return False
        if center_letter not in word:
            return False
        if not all(letter in letters for letter in word):
            return False
        if word in usedWords:
            return False
    usedWords.append(word)
    return True