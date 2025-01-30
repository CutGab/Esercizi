pari = 0
dispari = 0
i = 1

while i <= 10:
    n = int (input("Insert a number: "))
    
    if n%2 == 0:
        pari += 1
        i+=1

    else:
        dispari += 1
        i+=1

print(f"i numeri pari sono {pari}")
print(f"i numeri dispari sono {dispari}")