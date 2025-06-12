def sum_primary_diagonal(matrix: list[list]):

    diagonal: list = []

    index = 0

    for i in matrix:

        diagonal.append(i[index])

        index += 1

    return sum(diagonal)

def sum_secondary_diagonal(matrix: list[list]):

    diagonal: list = []

    index = -1

    for i in matrix:

        diagonal.append(i[index])

        index -= 1

    return sum(diagonal)

mat1 = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]

print(sum_primary_diagonal(mat1))
print(sum_secondary_diagonal(mat1))




