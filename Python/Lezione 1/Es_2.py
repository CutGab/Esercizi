Max: int = (input("Insert the biggest number: "))
i = 1

while i < 4:
    i += 1
    n: int = (input("Insert a number: "))

    if n > Max:
        Max = n

print(f"The biggest number is: {Max}")