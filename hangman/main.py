# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import random


def hangman():
    word_list = ["bobby", "hill", "camel"]
    num_of_lives = 5
    random_choice = random.choice(word_list)
    word_length = len(random_choice)

    display = ["_" for _ in random_choice]

    end_of_game = False

    while not end_of_game:
        letter = input("guess a letter ")
        if letter in display:
            print(f"you've already guessed {letter}")
        for i in range(word_length):
            if letter == random_choice[i]:
                display[i] = random_choice[i]
        if letter not in random_choice:
            num_of_lives -= 1
            print(num_of_lives)
            if num_of_lives == 0:
                end_of_game = True
                print("You lose!")
        print(display)
        if "_" not in display:
            end_of_game = True
            print("You win!")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    hangman()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
