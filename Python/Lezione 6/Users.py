class Users:

    def __init__(self, first_name: str, last_name: str, username: str, email: str):

        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email

    def describe_user(self):
        
        print(f"First Name: {self.first_name}\nLast Name: {self.last_name}\nUsername: {self.username}\nEmail: {self.email}\n")

    def greet_user(self):

        print(f"Hey {self.username}, welcome!")


class Privileges:

    def __init__(self, privileges: list):
        
        self.privileges = privileges

    def show_privileges(self):

        print(self.privileges)

class Admin:

    def __init__(self, user: Users, privileges: Privileges):
        
        self.user = user
        self.privileges = privileges

    def describe_user(self):
        self.user.describe_user()

    def show_privileges(self):
        self.privileges.show_privileges()