numbers: list[int] = [2, 3, 6, -4, -7, -8]

def separate(numbers: list) -> dict:
    dct: dict[str, list] = {"Positivi": [], "Negativi": []}

    for i in numbers:

        if i > 0:
            dct["Positivi"].append(i)

        else:
            dct["Negativi"].append(i)

    return dct

print(separate(numbers))