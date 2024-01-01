from wordle import Wordle
from colorama import *
from letter_state import LetterState
import random


def main():
    word_set = load_word_set("data/wordle_words.txt")
    secret = random.choice(list(word_set))
    wordle = Wordle(secret)

    while wordle.canAttempt:
        x = input("\nType your guess : ")

        if len(x) != wordle.WORD_LENGTH:
            print(
                Fore.RED
                + f"Word must be {wordle.WORD_LENGTH} characters long."
                + Fore.RESET
            )
            continue

        if x not in word_set:
            print(
                Fore.RED
                + f"{x} is not a valid word."
                + Fore.RESET
                )
            continue

        wordle.attempt(x)
        displayResult(wordle)

    if wordle.isSolved:
        print("You've solved the puzzle.")
    else:
        print("You've failed to solve the puzzle.")
        print(f"The secret word was {wordle.secret}")


def load_word_set(path: str):
    word_set = set()
    with open(path, "r") as f:
        for line in f.readlines():
            word = line.rstrip().upper()
            word_set.add(word)
    return word_set


def displayResult(wordle: Wordle):
    print("\nYour results so far...")
    print(f"You have {wordle.remainingAttempts} attempts remaining.\n")

    lines = []

    for word in wordle.attempts:
        result = wordle.guess(word)
        colored_result_str = convert_result_to_color(result)
        lines.append(colored_result_str)

    for _ in range(wordle.remainingAttempts):
        lines.append(" ".join(["_"] * wordle.WORD_LENGTH))

    drawBorderAround(lines)


def drawBorderAround(lines: list[str], size: int = 9, padding: int = 1):
    content_length = size + padding * 2
    top_border = "┌" + "─" * content_length + "┐"
    bottom_border = "└" + "─" * content_length + "┘"
    space = " " * padding
    print(top_border)

    for line in lines:
        print("│" + space + line + space + "│")

    print(bottom_border + "\n")


def convert_result_to_color(result: list[LetterState]):
    result_with_color = []
    for letter in result:
        color = ""
        if letter.is_in_position:
            color = Fore.GREEN
        elif letter.is_in_word:
            color = Fore.YELLOW
        else:
            color = Fore.WHITE + Style.DIM
        colored_letter = color + letter.character + Fore.RESET + Style.RESET_ALL
        result_with_color.append(colored_letter)

    return " ".join(result_with_color)


if __name__ == "__main__":
    main()
