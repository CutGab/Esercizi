Sum = 0
Cont = 0


while Cont < 5:
    
    n = int (input("Insert a number: "))
    Cont+=1

    if n > 0:
        Sum = Sum + n

print(f"The sum is: {Sum}")