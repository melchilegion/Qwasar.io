# Welcome to My Mastermind
***

## Task
- What is the problem? And where is the challenge?
The code is organized into several functions:
generate_code(): Generates a random secret code.
print_code(char *code): Prints the secret code.
count_well_placed(char *guess): Counts the number of well-placed digits in a guess.
count_misplaced(char *guess): Counts the number of misplaced digits in a guess.
play_game(): The main game loop, which handles user input and feedback.
main(int argc, char **argv): The entry point of the program, which parses command-line arguments and starts the game.

## Description
- How have you solved the problem?
- Mastermind Game
A command-line implementation of the classic Mastermind game.
- How to Play
- The goal of the game is to guess a secret code of 4 digits, each digit being a number from 0 to 8. You have a limited number of attempts to guess the code

## Installation
- How to install your project? npm install? make? make re?
Compile the code and run the executable. You can customize the game by providing command-line arguments:
-c <code>: Set the secret code manually (e.g. -c 1234)
-t <attempts>: Set the maximum number of attempts (e.g. -t 5)
Example: ./mastermind -c 1234 -t 5
Gameplay
The game will generate a secret code or use the one provided as an argument.
You will be prompted to enter a guess, which should be a 4-digit number.
The game will provide feedback on your guess, indicating how many digits are well-placed and how many are misplaced.
Keep guessing until you correctly guess the secret code or run out of attempts.

## Usage
The code is organized into several functions:
generate_code(): Generates a random secret code.
print_code(char *code): Prints the secret code.
count_well_placed(char *guess): Counts the number of well-placed digits in a guess.
count_misplaced(char *guess): Counts the number of misplaced digits in a guess.
play_game(): The main game loop, which handles user input and feedback.
main(int argc, char **argv): The entry point of the program, which parses command-line arguments and starts the game.

### The Core Team


<span><i>Made at <a href='https://qwasar.io'>Qwasar SV -- Software Engineering School</a></i></span>
<span><img alt='Qwasar SV -- Software Engineering School's Logo' src='https://storage.googleapis.com/qwasar-public/qwasar-logo_50x50.png' width='20px' /></span>
