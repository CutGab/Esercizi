a = int(input("Inserisci un valore a: "))
b = int(input("Inserisci un valore b: "))

if a > b:
    print("Errore, il primo valore deve essere più piccolo del secondo.")
elif a < 0 or b < 0:
    print("Errore, entrambi i numeri devono essere positivi.")
elif a % 1 != 0 or b % 1 != 0:
    print("Errore, entrambi i numeri devono essere interi.")
else:
    somma = 0
    for i in range(a, b + 1):
        somma += i
    print(f"La somma totale è di {somma}")

    somma = sum(list(range(a, b+1)))