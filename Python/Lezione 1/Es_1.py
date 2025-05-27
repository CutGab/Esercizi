import math

a = float (input("Insert a number: "))
b = float (input("Insert a number: ")) 

if a > b:
    c = math.sqrt(a * a - b * b)
    print(f"{c:.1f}")

else:
    print("Errore: Impossibile calcolare.")