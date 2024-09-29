import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

display = "_" * len(chosen_word)
print(display)

game_over = False
correct_letters = []
wrong_guesses = -1

stages = [
    '''
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
          |
          |
          |
          |
    =========
    '''
]

while not game_over:
    print(stages[wrong_guesses])
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You already guessed the letter '{guess}'.")
        continue

    correct_letters.append(guess)

    new_display = ""
    for letter in chosen_word:
        if letter in correct_letters:
            new_display += letter
        else:
            new_display += "_"

    display = new_display
    print(display)

    if guess not in chosen_word:
        wrong_guesses -= 1

    if "_" not in display:
        game_over = True
        print("You win!")

    if wrong_guesses == -7:
        game_over = True
        print(stages[wrong_guesses])
        print("You lose! The word was: " + chosen_word)


