shopping_cart: list = []
products: list = []

def product(name, price, quantity):

    name = name
    price = price
    quantity = quantity

    products.append(name)


def add_product(name):

    if name in products:

        shopping_cart.append(name)

def remove_product(name):

    if name in shopping_cart:

        shopping_cart.remove(name)

def view_products():

    print(shopping_cart)



product("Salmone", 13.99, 50)
product("Bistecca", 20.90, 50)

add_product("Salmone")

print(products)

view_products()



