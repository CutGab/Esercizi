n = None

cont = 0
i = 0

n = float (input("Inserisci un numero: "))

if n > 0 and n%1 == 0:
    while i !=  10:
        num =  int (input("Inserisci 10 numeri: "))

        if num%n == 0:
            cont += 1
            i += 1

        else:
            i += 1

else:
    print("Errore, il numero deve essere intero e positivo.")
    exit(0)

print(f"I numeri divisibili per {n} sono: {cont}")


