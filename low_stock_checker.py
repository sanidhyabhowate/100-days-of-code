products = [
    {"name": "Notebook", "quantity": 12},
    {"name": "Pen", "quantity": 3},
    {"name": "Pencil", "quantity": 8},
    {"name": "Eraser", "quantity": 2},
    {"name": "Marker", "quantity": 5}

]

def check_low_stock(products):
    low_stock = []

    for product in products:
        if product["quantity"] <= 5:
            
            low_stock.append(product)

    return low_stock

result = check_low_stock(products)
print(result)
