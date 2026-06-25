number = 17 

for chance in range(1, 6):
    guess = int(input("Enter your guess between 1 and 20: "))

    if guess == number:
        print("Congratulations! You guessed the correct number. ")
        break
    
    else:
        print("Sorry! You guessed the wrong number. ")

        if guess < number:
            print("Your guess is low")

        if guess > number:
            print("Your guess is high")

        if guess == number - 1 or guess == number + 1:
            print("Quite close! Try again. ")

        else:
            print("Game over")


