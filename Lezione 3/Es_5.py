
n = int (input("Inserisci un numero: "))

if n%1 == 0 and n > 0:
    sum = 0
    i = 1
    
    while i < n+1:
        sum += i**2
        i += 1
        
    

    print(f"La somma equivale a: {sum}")


else: 
    print("Il numero deve essere positivo.")