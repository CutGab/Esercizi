from typing import Any

Cities: dict [Any] = {"NY" : ["America", 20000000, "La grande mela"],
               "Rome": ["Italy", 5000000, "Capitale del mondo"],
              "Milan" : ["Italy", 10000000, "Roma più bella e costosa"],
              }

for i, values in Cities.items():
    print(f"{i} : {values}")