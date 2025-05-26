class User:
    def __init__(self, first_name, last_name, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = login_attempts

    def describe_user(self):

        return(print(f"First Name: {self.first_name}\nLast Name: {self.last_name}\nLogin Attempts: {self.login_attempts}"))
    
    def greet_user(self):

        return(print(f"Hey {self.first_name} {self.last_name}, nice to meet you!"))

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
   
p1 = User ("Gabriele", "Cutolo", 0)

p1.describe_user()

p1.increment_login_attempts()

p1.describe_user()

p1.increment_login_attempts()

p1.describe_user()

p1.reset_login_attempts()

p1.describe_user()