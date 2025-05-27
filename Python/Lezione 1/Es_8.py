soglia = int (input("Inserisci la soglia: "))

i = 0

while i < 7:
    n = int (input("Inserisci un numero: "))

    if n > soglia:
        print(f"il numero {n} è maggiore della soglia {soglia}")
        
    i+=1