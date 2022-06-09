
import random

from hangman_words import word_list

chosen_word = random.choice(word_list)
print(chosen_word)

word_lenth = len(chosen_word)

lives = 6

display = []
for _ in range(word_lenth):
    display += "_"
print(display)

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
      print(f"You've already guessed {guess}")

    for position in range(word_lenth):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:

        print(f"You guessed {guess}, that's not in the word. you lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose.")

    print(f"{' '.join(display)}")


    if "_" not in display:
        end_of_game = True
        print("You win!")

    from hangman_art import stages
    print(stages[lives])

