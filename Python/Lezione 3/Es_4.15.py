#Excercise 1

# List of numbers from 1 to 10
numbers: list = [
    1,2,3,
    4,5,6,
    7,8,9,
    10
    ]

# For loop using list comprehension
new_numbers = [i ** 3 for i in numbers]

# Print of the list with all the cubes starting from 1 to 10
print(new_numbers)

#Excercise 2

# Empty list
lista: list = []

# Append to list all numbers multiple of 3 starting from 3 to 30
for i in range (
    3, 
    31, 
    3
    ):
    lista.append(i)

# Print of the list 
print(lista)

#Excercise 3

# Empty list
numbers_BIG: list = []

# Append to list numbers from 1 to 100000000
for i in range (
    1, 
    1000001
    ):
    numbers.append(i)

# Print of the smallest, biggest and sum of all numbers
print(min(numbers))

print(max(numbers))

print(sum(numbers))