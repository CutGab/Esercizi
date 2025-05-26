a = (int(input("Inserisco lo start del range: ")))

b = (int(input("Inserisco la fine del range: ")))

def sum_range (a: int, b: int):
    result: int = 0

    for i in range(a, b + 1):
        result = result + i

    return result

print(f"The sum of numbers from {a} to {b} is {sum_range(a, b)}")