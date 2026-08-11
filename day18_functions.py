def greet_user():
    name =  input("What is your name?")
    print("Hello", name)

# greet_user()


def check_number():
    number = int(input("Choose a number:"))
    if number > 0:
        print("Positive")
    elif number < 0:
        print("Negative")
    else:
        print("Zero")

# check_number()


def show_square(number):
    print(number*number)

#square_number = int(input("Choose a number for square:"))
 
#show_square(square_number)


def calculate_numbers(a, b):
    print( a + b)
    print(a*b)

    if b == 0:
        print("Number cannot be divided")
    else:
        print(a/b)
        print(a//b)

#a = int(input("Choose first number:"))

#b = int(input("Choose second number:"))

#calculate_numbers(a, b)


#def multiply_numbers(a, b):
    #return a*b

#a = int(input("Choose first number:"))
#b = int(input("Choose second number:"))

#result = multiply_numbers(a, b)

#print(result)


#def calculate_total(price, quantity):
    #return price * quantity

#price = int(input("What is the price?"))
#quantity = int(input("Total number of items?"))

#total = calculate_total(price, quantity)

#if total >= 500:
 #   print("Free delivery")
#else:
  #  total = total + 50

#print("Final amount", total)


def calculate_discount(price):
    if price >= 1000:
        return price*0.90
    else:
        return price

price = int(input("Total amount you have spent?"))

final_price = calculate_discount(price)

print("Final price", final_price)