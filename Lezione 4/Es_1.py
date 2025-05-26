num = (int(input("Inserisci un numero: ")))

def check_value(num: int):

    if num > 5:
        print(f"This number {num} is bigger than 5")

    elif num < 5:
        print(f"The number {num} is smaller than 5")

    else:
        print(f"The number {num} is equal to 5")


check_value(num)