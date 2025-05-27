from typing import Any

person1: dict [Any] = {"First_Name" : "Luca",
               "Last_Name": "Abete",
              "Age" : 20,
              "City" : "Rome"
              }

person2: dict [Any] = {"First_Name" : "Marco",
               "Last_Name": "Sorrentino",
              "Age" : 24,
              "City" : "Milano"
              }

person3: dict [Any] = {"First_Name" : "Billy",
               "Last_Name": "Joel",
              "Age" : 19,
              "City" : "New York"
              }

people: list [dict] = [person1,
                       person2,
                       person3
                       ]

for i in people:
    print(f"{i}")


