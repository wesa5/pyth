
import random

word_list = ['ardvark', 'baboon', 'camel']

chosen_word = random.choice(word_list)

word_lenth = len(chosen_word)

display = []
for _ in range(word_lenth):
    display += "_"
print(display)

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for position in range(word_lenth):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    print(display)


if "_" not in display:
    end_of_game = True
    print("You win!")

