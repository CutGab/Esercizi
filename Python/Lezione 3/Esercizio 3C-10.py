# Esercizio 3C-10. Scrivere un programma in Python che permetta all'utente di inserire una data (giorno e mese espressi in forma numerica), 
# salvi la data in una tupla e utilizzi un match statement per verificare se la data corrisponde a una festività o a un evento speciale:

# - Capodanno → 1 Gennaio → "Capodanno"
# - San Valentino → 14 Febbraio → "San Valentino"
# - Festa della Repubblica Italiana → " Giugno → "Festa della Repubblica Italiana"
# - Ferragosto → 15 Agosto → "Ferragosto"
# - Halloween → 31 Ottobre → "Halloween"
# - Natale → 25 Dicembre → "Natale"
# - Altro caso → "Nessuna festività importante in questa data."

# Expected Output:

# Inserisci il giorno: 25
# Inserisci il mese: 12
# Output: Il 25/12 è Natale!

# - - - - - - - - - - - - - - -

# Inserisci il giorno: 5
# Inserisci il mese: 3
# Output: Nessuna festività importante in questa data.

day = (int(input("Inserisci a day: ")))

month = (int(input("Insert a month: ")))

festive: tuple = (day, month)

match festive:

    case (1, 1):
        print(f"Il {festive} è Capodanno!")

    case (14, 2):
        print(f"Il {festive} è San Valentino!")

    case (2, 6):
        print(f"Il {festive} è la festa della Repubblica Italiana!")

    case (15, 8):
        print(f"Il {festive} è Ferragosto!")

    case (31, 10):
        print(f"Il {festive} è Halloween!")

    case (25, 12):
        print(f"Il {festive} è Natale!")

    case (day, month) if day > 31 or month > 12 or day == 0 or month == 0:
        print("Errore, giorno o mese errati!")

    case _:
        print("Nessuna festività importante in questa data.")

