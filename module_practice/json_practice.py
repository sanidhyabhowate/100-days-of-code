#import json

#product = {
 #   "name": "Notebook",
  #  "price": 50,
   # "quantity": 3,
    #"available": True
#}

#with open("product.json", "w", encoding="utf-8") as file:
   # json.dump(product, file, indent=4)

    #print("Product data saved!")

#with open("product.json", "r", encoding="utf-8") as file:
  #  c_product = json.load(file)

#print(c_product["name"])
#print(c_product["price"] * product["quantity"])
#print(c_product["available"])


import json

student = {
    "name": "Amit",
    "age": 20,
    "course": "Engineering"
}

json_text = json.dumps(student)

print(json_text)
print(type(json_text))

converted = json.loads(json_text)

print(converted["course"])
print(type(converted))
                       
                    