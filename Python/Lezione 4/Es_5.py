n = (int(input("Insert a number: ")))

numbers: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def add_one(n: int):

    n += 1

    return n

def add_one_to_list(numbers: list):

    new_list: list = []

    for i in numbers:
        
        new_list.append(add_one(i))

    print(new_list)


add_one_to_list(numbers)