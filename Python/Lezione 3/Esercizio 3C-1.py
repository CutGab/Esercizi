# Esercizio 3C-1. Scrivere un programma in Python che utilizzi un match statement per classificare un voto scolastico in base alla scala italiana.
# Il programma deve accettare in input un voto numerico intero da 1 a 10 e stampare la valutazione corrispondente:

# - 10 → "Eccellente"
# - 8-9 → "Molto buono"
# - 6-7 → "Sufficiente"
# - 4-5 → "Insufficiente"
# - 1-3 → "Gravemente insufficiente"
# - Altro caso → "Voto non valido"

# Expected Output:

# Inserisci il voto: 5
# Output: Insufficiente
# - - - - - - - - - - -
# Inserisci il voto: 11
# Output: Voto non valido

voto = (float(input("Inserisci un voto (1-10): ")))

match voto:

    case voto if voto == 1 or voto <= 3.9:
        print("Gravemente insufficiente")

    case voto if voto == 4 or voto <=5.9:
        print("Insufficiente")

    case voto if voto == 6 or voto <= 7.9:
        print("Sufficiente")

    case voto if voto == 8 or voto <= 9.9:
        print("Molto buono")

    case voto if voto == 10:
        print("Eccellente")

    case _:
        print("Voto non valido.")