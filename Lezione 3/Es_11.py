n = float (input("Inserisci un numero: "))

while n%1 != 0:
    n = float (input("Inserisci un numero: "))

if n%2 == 0 and n > 10:
    print("Numero valido.")

else:
    print("Numero invalido.")