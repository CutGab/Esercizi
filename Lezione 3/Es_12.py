n = int (input("Inserisci un numero: "))

i = 0

while i != n:
    x = int (input("Inserisci il primo numero: "))
    y = int (input("Inserisci il secondo numero: "))

    i+= 1

    if x > 0 and y > 0:
        result = x*y
        print(f"Il prodotto equivale a: {result}")

    elif x < 0 and y < 0:
        print("Errore.")

    else:
        result = x+y
        print (f"Il risultato della somma equivale a: {result}")