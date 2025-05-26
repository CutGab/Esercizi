posti_max = int (input("Inserisci il numero di posti massimi: "))

posti_liberi = posti_max

opzione = None

while opzione != "esci":

    opzione = str (input("Inserisci l'azione che vuole effettuare: "))

    if opzione == "ingresso":
        if posti_liberi > 0:
            posti_liberi -= 1

        else:
            print("Il parcheggio è pieno.")

    elif opzione == "uscita":
        if posti_liberi < posti_max:
            posti_liberi += 1

        else:
            print("Il parcheggio è già vuoto.")

    elif opzione == "stato":
        print(f"I posti liberi sono {posti_liberi}")
        print(f"I posti occupati sono {posti_max - posti_liberi}")


    elif opzione != "ingresso" and opzione != "uscita" and opzione != "stato" and opzione != "esci":
        print("Errore, inserire un'azione valida")

