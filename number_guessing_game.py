guess = int(input("Enter your guess (between 1 and 20) : "))
number = 17

if guess == number:
    print("Congratulations!You guessed the correct Number.")
else:
    print("Sorry:You guessed the wrong Number.")

    if guess < number:
        print("Your guess is low")
    if guess > number:
        print("Your guess is high")
    if number <= 16 or number >= 18:
        print("Quite close!Try again.")


