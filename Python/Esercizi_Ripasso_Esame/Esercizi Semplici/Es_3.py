prodotti: dict = {"Carne": 19.99, "Pesce": 12.40, "Bevande": 70.40, "Playstation": 50.89}

def rounding (prodotti: dict) -> dict:

    new_prodotti: dict = {}

    for key, value in prodotti.items():

        if value < 50:

            increase = round((value * 10)/100, 2)

            new_prodotti[key] = value + increase


    return new_prodotti

print(rounding(prodotti))