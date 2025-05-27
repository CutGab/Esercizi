class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):

        return(print(f"First Name: {self.first_name}\nLast Name: {self.last_name}"))
    
    def greet_user(self):

        return(print(f"Hey {self.first_name} {self.last_name}, nice to meet you!"))
    
p1 = User ("Gabriele", "Cutolo")
p2 = User ("Giovanni", "Rana")

p1.describe_user()
p2.describe_user

print("--------------------")

p1.greet_user()
p2.greet_user()