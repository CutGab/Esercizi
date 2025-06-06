def moltiplica (numbers: list, threshold: int) -> list:

    prodotto = 1

    for i in numbers:

        if i < threshold:
            
            prodotto *= i

    return prodotto

print(moltiplica([1,2,3,4,5,6,20,46], 10))


def fattoriale_ricorsivo(n):

    if n == 1:
        return 1
    else:
        return n * fattoriale_ricorsivo(n - 1)

print(fattoriale_ricorsivo(5))