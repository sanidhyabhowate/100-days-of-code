import random

def get_guess():
    while True:
        try:
            guess = int(input("Enter you guess between 1 and 20: "))
            if guess < 1 or guess > 20:
                print("Please enter a number between 1 and 20. ")
                continue
            return guess
        except ValueError:
            print("Invalid Input! Please enter a number.")


def give_hint(guess, number):
    if guess < number: 
        print("Your number is low")
    elif guess > number:
        print("Your guess is high.")

    if abs(guess - number) == 1:
        print("Quite close! Try again. ")
    

def play_game():
    number = random.randint(1, 20)
    chances = 5

    while chances > 0:
        guess = get_guess()

        if guess == number:
            print("Congratulationd! You guessed the cprrect number.")
            break

        print("Sprry! You guessed the wrong number.")
        give_hint(guess, number)

        chances = chances - 1
        print("Chances left:", chances)

    else:
        print("Game over. The correct number was", number)

play_game()