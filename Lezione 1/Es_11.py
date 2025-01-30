posti_liberi = 20

opzione = None


while opzione != "esci":
    
    opzione = str (input("Inserisci un opzione: "))
    opzione = opzione.lower()

    if opzione == "prenota":
        if posti_liberi == 0:
            print("Non ci sono posti disponibili.")
        
        else:
            posti_liberi -= 1

    if opzione == "libera":
        if posti_liberi < 20:
            posti_liberi += 1

        else:

            print ("Tutti i posti sono già disponibili.")

    if opzione == "visualizza":
        print(f"I posti disponibili sono {posti_liberi}")
        print(f"I posti occupati sono {20 - posti_liberi}")