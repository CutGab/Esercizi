def binary_search (lista1: list, number) -> bool:

    while len(lista1) > 0:

        mid = len(lista1)//2

        x = lista1[mid:]

        y = lista1[:mid]

        for i in x, y:

            if number in x:
                return True

            elif number in y:
                return True
            
            else:
                return False

lista = list(range(1, 51))
print(binary_search(lista, 1))