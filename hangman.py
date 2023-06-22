import random

def load_word_list(filename):
    with open(filename, 'r') as file:
        word_list = file.read().splitlines()
    return word_list

def hangman(word):
    wrong_guesses = 0
    stages = [
        "__________     ",
        "|        |      ",
        "|        O      ",
        "|       /|\     ",
        "|       / \     ",
        "|               "
    ]
    remaining_letters = list(word)
    board = ["_"] * len(word)
    guessed_letters = []
    game_won = False
    hint_used = False  # New variable to keep track of hint usage
    print("\n------ Welcome to Hangman! ------\n"
          "\nGuess a word from a list of 69,903 English words!\n")

    while wrong_guesses < len(stages):
        print("\n")
        for i in range(wrong_guesses):
            print(stages[i])
        print("\n")
        print(" ".join(board))
        print("Guesses remaining: {}".format(len(stages) - wrong_guesses))
        guess = input("Guess a letter (or type 'hint' for 1 free letter): ").lower()
        print("\n")

        if guess == "hint":
            if not hint_used:
                get_hint(word, board)
                hint_used = True
            else:
                print("You have already used a hint.")
            continue

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You have already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in remaining_letters:
            letter_indices = [i for i, letter in enumerate(remaining_letters) if letter == guess]
            for index in letter_indices:
                board[index] = guess
                remaining_letters[index] = '$'
        else:
            wrong_guesses += 1

        if "_" not in board:
            print("You win!")
            print(" ".join(board))
            game_won = True
            break

    if not game_won:
        for i in range(wrong_guesses):
            print(stages[i])
        print("\n")
        print("You lose! The word was {}.".format(word))

def replay():
    while True:
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again == "yes":
            return True
        elif play_again == "no":
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def get_hint(word, board):
    masked_indices = [i for i, letter in enumerate(board) if letter == "_"]
    if masked_indices:
        hint_index = random.choice(masked_indices)
        hint_letter = word[hint_index]
        board[hint_index] = hint_letter
        print("Hint: The letter '{}' is at position {}.".format(hint_letter, hint_index + 1))
    else:
        print("There are no more hidden letters in the word.")

word_list = load_word_list("word_list.txt")

while True:
    word = random.choice(word_list)
    hangman(word)

    if not replay():
        break
