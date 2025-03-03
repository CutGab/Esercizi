mammiferi: list = ["cane", "gatto", "cavallo", "elefante", "leone"]
rettili: list = ["serpente", "lucertola", "tartaruga", "coccodrillo"]
uccelli: list = ["aquila", "pappagallo", "gufo", "falco"]
pesci: list = ["squalo", "trota", "salmone", "carpa"]

while True:

    opzione = (str(input("Vuoi inserire un animale? (Y/N)").upper()))

    if opzione == "Y":
        animale = (str(input("Inserisci un animale: ").lower()))
        
        match animale:

            case animale if animale in mammiferi:
                print(f"{animale} appartiene alla lista Mammiferi.")

            case animale if animale in rettili:
                print(f"{animale} appartiene alla lista Rettili.")

            case animale if animale in uccelli:
                print(f"{animale} appartiene alla lista Uccelli.")

            case animale if animale in pesci:
                print(f"{animale} appartiene alla lista Pesci.")

            case _:
                print("Spiacente non sono in grado di classificare questo animale.")

    else:
        print("Arrivederci.")
        break