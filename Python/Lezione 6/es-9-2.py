class Restaurant:

    def __init__(self, restaurant_name: str, cuisine_type: str):

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


    def describe_restaurant(self):

        print(f"Nome: {self.restaurant_name}\nTipo cucina: {self.cuisine_type}")

    def open_restaurant(self):

        print(f"{self.restaurant_name} is now open!")


r1 = Restaurant ("Mamami", "Rosticceria")
r2 = Restaurant ("Skibidi", "Pizzeria")
r3 = Restaurant ("Sigma", "Sushi")

r1.describe_restaurant()
r2.describe_restaurant()
r3.describe_restaurant()