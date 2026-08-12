#def check_even_odd(number):
 #   if number % 2 == 0:
  #      return "Even"
   # else:
    #    return "Odd"

#for i in range(5):
    #number = int(input("Choose a Value:"))
    #result = check_even_odd(number)

    #print(result)


#def calculate_square(number):
    #return number * number

#for i in range(3):
   # number = int(input("Choose a Value:"))
# result = calculate_square(number)

   # print(result)


#def find_larger(a, b):
 #   if a > b:
  #      return a
   # elif a < b:
    #    return b
   # else:
    #    return "Equal"

#for i in range(3):
 #   a = int(input("Select first number:"))
  #  b = int(input("Select second number:"))

   # result = find_larger(a, b)
    #print(result)


def calculate_total(price, quantity):
    return price * quantity

grand_total = 0

for i in range(3):
    price = int(input("What is the price?"))
    quantity = int(input("How many products?"))

    result = calculate_total(price, quantity)
    grand_total += result 

    print(result)

print("Grand Total:", grand_total)

    
    

    




