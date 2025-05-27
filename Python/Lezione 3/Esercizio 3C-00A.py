# Esercizio 3C-00A. Scrivere un programma in Python che richieda all'utente di inserire un numero intero rappresentante il numero di neonati e 
# utilizzi lo statement match per fornire una risposta appropriata:

# - Se il numero inserito è 1, stampare "Congratulazioni!"
# - Se il numero inserito è 2, stampare "Wow! Gemelli!"
# - Se il numero inserito è 3, stampare "Wow! Tre!"
# - Se il numero inserito è 4, stampare "Mamma mia Quattro! Wow!"
# - Se il numero inserito è 5, stampare "Incredibile! Cinque!"
# - Altrimenti, stampare "Non ci credo! n bambini!", sostituendo n con il numero inserito.

# Expected Output:

# Inserire il numero di neonati: 2
# Wow! Gemelli!

# - - - - - - - - - - - - - - - - - -

# Inserire il numero di neonati: 5
# Incredibile! Cinque!

# - - - - - - - - - - - - - - - - - -

# Inserire il numero di neonati: 7
# Non ci credo! 7 bambini!

n = (float(input("Inserisci un numero: ")))

match n:

    case n if n == 1:
        print("Congratulazioni!")

    case n if n == 2:
        print("Wow! Gemelli!")

    case n if n == 3:
        print("Wow! Tre!")

    case n if n == 4:
        print("Mamma mia Quattro! Wow!")

    case n if n == 5:
        print("Incredibile! Cinque!")

    case n if n.is_integer() == False:
        print("Errore il numero deve essere intero.")
        
    case _:
        print(f"Non ci credo! {int(n)} bambini!")