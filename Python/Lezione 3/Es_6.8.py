from typing import Any

pet1: dict [Any] = {"Kind" : "Fox",
               "Owner": "Luca",
              }

pet2: dict [Any] = {"Kind" : "Dog",
               "Owner": "Sorrentino",
              }

pet3: dict [Any] = {"Kind" : "Cat",
               "Owner": "Joel"
              }

pets: list [dict] = [pet1,
                    pet2,
                    pet3
                    ]

for i in pets:
    print(f"{i}")
