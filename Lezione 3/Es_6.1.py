from typing import Any
person: dict [Any] = {"First_Name" : "",
               "Last_Name": "",
              "Age" : "",
              "City" : ""
              }

first_name = (input("Insert your friend's name: " ).title())
person["First_Name"] = first_name

last_name = (input("Insert your friend's last name: ").title())
person["Last_Name"] = last_name

age = (int(input("Insert your friend's age: ")))
person["Age"] = age

city = (input("Insert the city your friend lives in: ").title())
person["City"] = city

for i, value in person.items():
    print(f"{i}: {value}")