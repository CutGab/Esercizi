a = (int(input("Inserisci il primo numero: ")))

b = (int(input("Inserisci il secondo numero: ")))

def calculation (a: int, b: int):
    
    subtract: int = 0
    summation: int = 0

    summation = a + b

    if a > b:
        subtract = a - b

    elif b > a:
        subtract = b - a

    return summation, subtract

print (calculation(a, b))