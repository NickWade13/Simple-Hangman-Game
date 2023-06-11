import random

def hangman(word):
    wrong_guesses = 0
    stages = ["",
              "__________     ",
              "|        |      ",
              "|        O      ",
              "|       /|\     ",
              "|       / \     ",
              "|               "
             ]
    remaining_letters = list(word)
    board = ["_"] * len(word)
    game_won = False
    print("Welcome to Hangman")

    while wrong_guesses < len(stages) - 1:
        print("\n")
        guess = input("Guess a letter: ").lower()
        print("\n")
        if guess in remaining_letters:
            letter_index = remaining_letters.index(guess)
            board[letter_index] = guess
            remaining_letters[letter_index] = '$'
        else:
            wrong_guesses += 1
        print(" ".join(board))

        current_stage = wrong_guesses + 1
        print("\n".join(stages[0:current_stage]))

        if "_" not in board:
            print("You win!")
            print(" ".join(board))
            game_won = True
            break

    if not game_won:
        print("\n".join(stages[0:wrong_guesses]))
        print("You lose! The word was {}.".format(word))

word_list = ["cat", "dog", "bird", "elephant", "giraffe", "lion"]
word = random.choice(word_list)
hangman(word)
