user: dict = {}

first_name = (input("Insert their first name: "))

user["First Name"] = first_name

last_name = (input("Insert their last name: "))

user["Last Name"] = last_name

age = (int(input("Insert their age: ")))

user["Age"] = first_name

hair = (input("Insert their hair color: "))

user["Hair Color"] = hair

weight = (input("Insert their weight: "))

user["Weight"] = weight

def build_profile(first_name: str, last_name: str, age: str, hair: str, weight: float):

    return print(user)

build_profile(first_name, last_name, age, hair, weight)