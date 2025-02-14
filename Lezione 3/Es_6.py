n = int (input("Inserisci un numero: "))

if n > 0:
    i = 0
    somma = 0

    while i <= 4:
        num = int (input("Inserisci dei numeri: "))
        
        if n%2 == 0:
            if num > n/2:
                somma += num
                
                i+= 1

            else:
                i+= 1


        else: 
            if num < n:
                somma += num
                i+= 1

            else:
                i+=1


print(f"La somma equivale a {somma}")