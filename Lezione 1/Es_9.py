i = 0

nome = str (input("Inserisci il nome del venditore: "))
vendite = int (input("Inserisci il numero di vendite: "))

max_nome = nome

max_vendite = vendite

min_nome = nome

min_vendite = vendite

while i < 20:

    new_nome = str(input("Inserisci il nome del venditore: "))
    new_vendite = int (input("Inserisci il numero di vendite: "))

    if new_vendite > max_vendite:
        max_nome = new_nome
        max_vendite = new_vendite

    else:

        if new_vendite < min_vendite:

            min_nome = new_nome
            min_vendite = new_vendite
    i+=1


print(f"Il venditore con vendite più alte è stato {max_nome} con un numero di vendite pari a {max_vendite}")
print(f"Il venditore con vendite più basse è stato {min_nome} con un numero di vendite pari a {min_vendite}")