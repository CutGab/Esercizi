from typing import Any

favorite_places: dict [Any] = {"Luca" : ["Roma", "Ravenna", "Rimini"],
               "Abete": ["Milano", "Monza", "Montenero"],
               "Pierpaolo" : ["Ischia", "Imola", "India"]
              }

for i, values in favorite_places.items():
    print({f"{i}: {values}"})