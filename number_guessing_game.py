# Day 9 - Improved Number Guessing Game

number = 17
chances = 5

while chances > 0:
    try:
        guess = int(input("Enter your guess between 1 and 20: "))

        if guess == number:
            print("Congratulations! You guessed the correct number.")
            break

        else:
            print("Sorry! You guessed the wrong number.")

            if guess < number:
                print("Your guess is low.")

            elif guess > number:
                print("Your guess is high.")

            if guess == number - 1 or guess == number + 1:
                print("Quite close! Try again.")

            chances = chances - 1
            print("Chances left:", chances)

    except ValueError:
        print("Invalid input! Please enter a number.")

else:
    print("Game over. The correct number was", number)


