user: dict = {"Nome" : "", 
              "Ruolo" : "",
              "Età" : ""}

nome = (input("Inserisci il nome dello user: " ).title())
user["Nome"] = nome
ruolo = (input("Inserisci il ruolo dello user: ").title())
user["Ruolo"] = ruolo
età = (int(input("Inserisci l'età dello user: ")))
user["Età"] = età


match user:

        case {"Nome": nome, "Ruolo": "Admin", "Età": età}:
            print("Accesso completo a tutte le funzionalità")

        case {"Nome": nome, "Ruolo": "Moderatore", "Età": età}:
            print(f"Salve {nome}, Può gestire i contenuti ma non modificare le impostazioni")

        case {"Nome": nome, "Ruolo": "Utente Adulto", "Età": età} if età >= 18:
            print("Accesso standard a tutti i servizi")

        case {"Nome": nome, "Ruolo": "Utente Minorenne", "Età": età} if età <= 18:
            print("Accesso limitato! Alcune funzionalità sono bloccate")

        case {"Nome": nome, "Ruolo": "Ospite", "Età": età}:
            print("Accesso ristretto! Solo visualizzazione dei contenuti")

        case _:
            print("Attenzione! Ruolo non riconosciuto! Accesso Negato.")







