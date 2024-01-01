# Wordle Clone Using Python

This project simulates a simplified version of the popular word-guessing game called Wordle, implemented in Python. The game utilizes terminal-based interactions and incorporates color-coded feedback to guide players in their attempts to guess a secret word.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Setup Instructions](#setup-instructions)
3. [Script Descriptions](#script-descriptions)
    - [play_wordle.py : Main Game Logic](/script-descriptions/#play_wordle-main-game-logic)
    - [wordle.py : Wordle Class Definition](/script-descriptions/#wordle-wordle-class-definition)
    - [letter_state.py : LetterState Class Definition](/script-descriptions/#letter_state-letterstate-class-definition)

## Project Overview

- **Objective**: Guess the secret word within a limited number of attempts by receiving feedback on each guess.
- **Features**:
    - Randomly selects a word from a predefined set.
    - Provides color-coded feedback on each guess:
        - Green: Correct letter in the correct position.
        - Yellow: Correct letter but in the wrong position.
        - Dim white: Incorrect letter.
    - Visual representation of guesses and remaining attempts.

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/gpsgaurav18/wordle-clone-mini-project.git
   cd wordle-clone-mini-project
   ```

2. **Install Dependencies**:
   Ensure you have Python installed. Install the required packages using pip:
   ```bash
   pip install colorama
   ```

3. **Run the Game**:
   Execute the main script to start the Wordle game simulation:
   ```bash
   python play_wordle.py
   ```

## Script Descriptions

### play_wordle : Main Game Logic

- **Filename**: `play_wordle.py`
- **Description**: 
    - Handles the main game flow.
    - Initializes the game with a secret word.
    - Manages user input, validation, and feedback.
    - Determines game outcomes (success/failure).

### wordle : Wordle Class Definition

- **Filename**: `wordle.py`
- **Description**: 
    - Defines the `Wordle` class responsible for managing the game state.
    - Manages attempts, checks for correct guesses, and calculates remaining attempts.

### letter_state : LetterState Class Definition

- **Filename**: `letter_state.py`
- **Description**: 
    - Defines the `LetterState` class, representing the state of each letter in the guessed word.
    - Tracks whether the letter is present in the secret word and its correct position.
