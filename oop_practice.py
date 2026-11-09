#class Student:
 #   pass

#student1 = Student()

#student1.name = "Rahul"
#student1.age = 19

#print(student1.name)
#print(student1.age)

#student2 = Student()

#student2.name = "Amit"
#student2.age = 20

#print(student2.name)
#print(student2.age)

#class Product:

   # def __init__(self, name, price, quantity):
    #    self.name = name
    #    self.price = price
     #   self.quantity = quantity


    #def calculate_total(self):
     #   total = self.price * self.quantity
      #  return total

    #def discounted_price(self):
     #   total = self.calculate_total()

      #  discount = total * 10 / 100

       # return total - discount

#product1 = Product("Notebook", 50, 3)

#print(product1.calculate_total())
#print(product1.discounted_price())


#class Product:
   # def __init__(self, name, price):
    #    self.name = name
     #   self.price = price

    #def show_details(self):
     #   print(self.name, self.price)


#class DigitalProduct(Product):
 #   def download(self):
  #      print("Downloading", self.name)

   # def file_info(self):
    #    print(self.name, "is available as a digital file.")


#product1 = DigitalProduct("Python Ebook", 200)

#product1.show_details()
#product1.download()
#product1.file_info()


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class DigitalProduct(Product):
    def __init__(self, name, price, file_size):
        super().__init__(name, price)
        self.file_size = file_size

product1 = DigitalProduct("Python Course", 500, 250)

print(product1.name)
print(product1.price)
print(product1.file_size)