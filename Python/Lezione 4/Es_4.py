numbers: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def check_each(numbers: list):

    for i in numbers:

        if i < 5:
            print(f"The number {i} is smaller than 5.")

        elif i > 5:
            print(f"The number {i} is bigger than 5.")

        else:
            print(f"The number {i} is equal to 5.")


check_each(numbers)