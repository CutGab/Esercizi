nome_corso = str (input("Inserisci il nome del corso: "))

max_posti = 100

opzione = None

while opzione != "esci":
    opzione = str (input("Inserisci l'azione che vuole effettuare: "))

    if opzione == "iscrivi":
        if max_posti > 0:
            max_posti -= 1

        else:
            print("Non ci sono posti disponibili.")


    if opzione == "annulla":
        if max_posti < 100:
            max_posti += 1
            
        else:
            print("Tutti i posti sono già disponibili.")


    if opzione == "visualizza":
        print(max_posti)
        print(100 - max_posti)


    if opzione == "elimina":
        print("Corso eliminato con successo.")
        nome_corso = str (input("Inserisci il nome del corso: "))
        max_posti = 100
