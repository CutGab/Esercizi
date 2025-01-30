n_tutor: int = 3
attesa: int = 0

while n_tutor > 0 or attesa < 10:

    studente = str (input("Inserisca il nome dello studente: "))

    
    if n_tutor > 0:
        n_tutor -= 1
        print("Tutor assegnato con successo.")
        
    else:
        attesa += 1
        print("Studente in attesa.")

