a = (int(input("Inserisci il primo numero: ")))

b = (int(input("Inserisci il secondo numero: ")))

def subtract (a: int, b: int):
    result: int = 0
    
    if a > b:
        result = a - b

    elif b > a:
        result = b - a

    return result

print(f"The difference between {a} and {b} is {subtract(a, b)}")