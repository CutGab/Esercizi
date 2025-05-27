class Restaurant:

    def __init__(self, restaurant_name: str, cuisine_type: str):

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number = 0


    def describe_restaurant(self):

        print(f"Nome: {self.restaurant_name}\nTipo cucina: {self.cuisine_type}")

    def open_restaurant(self):

        print(f"{self.restaurant_name} is now open!")

    def set_number_served(self, number):

        self.number_served = number

    
    def increment_number_served(self, number):

        self.number_served += number


restaurant = Restaurant ("Da Vito", "Italiana")

restaurant.number_served = 50
print(restaurant.number_served)

print("-------------------------")

restaurant.set_number_served(100)
print(restaurant.number_served)

print("-------------------------")

restaurant.increment_number_served(25)
print(restaurant.number_served)