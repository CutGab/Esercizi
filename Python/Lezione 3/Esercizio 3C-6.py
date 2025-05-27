mammiferi: list = ["cane", "gatto", "cavallo", "elefante", "leone", "balena", "delfino"]
rettili: list = ["serpente", "lucertola", "tartaruga", "coccodrillo"]
uccelli: list = ["aquila", "pappagallo", "gufo", "falco", "cigno", "anatra", "gallina", "tacchino"]
pesci: list = ["squalo", "trota", "salmone", "carpa"]

habitat: list = ["acqua", "aria", "terra"]


myanimal: dict = {}

while True:

    opzione = (str(input("Vuoi inserire un'animale? (Y/N): ").lower()))

    if opzione == "y":

        animale = (str(input("Inserire un'animale: ").lower()))
        myanimal["Nome"] = animale

        habitat = (str(input("Inserire un habitat: ").lower()))
        myanimal["Habitat"] = habitat


        match animale:
            
            case animale if animale in mammiferi:
                animal_type = "mammiferi"
                print(f"{animale} appartiene alla categoria dei mammiferi!.")

            case animale if animale in rettili:
                animal_type = "rettili"
                print(f"{animale} appartiene alla categoria dei rettili!.")

            case animale if animale in uccelli:
                animal_type = "uccelli"
                print(f"{animale} appartiene alla categoria degli uccelli!.")

            case animale if animale in pesci:
                animal_type = "pesci"
                print(f"{animale} appartiene alla categoria dei pesci.")

            case _:
                animal_type = "Unknown"
                print(f"Non so dire in quale categoria classificare l'animale {animale}!")

        
        myanimal["Tipo"] = animal_type


        match habitat:

            case habitat if habitat == "acqua":
                pass

            case habitat if habitat == "aria":
                pass

            case habitat if habitat == "terra":
                pass

            case _:
                print(f"Non sono in grado di fornire informazioni sull'habitat {habitat}")

        match myanimal:

            #casi balena, delfino, squalo, trota, salmone, carpa
            case {"Nome": "balena", "Tipo": animal_type, "Habitat": habitat} | \
                 {"Nome": "delfino", "Tipo": animal_type, "Habitat": habitat} | \
                 {"Nome": "squalo", "Tipo": animal_type, "Habitat": habitat} | \
                 {"Nome": "trota", "Tipo": animal_type, "Habitat": habitat} | \
                 {"Nome": "salmone", "Tipo": animal_type, "Habitat": habitat} | \
                 {"Nome": "carpa", "Tipo": animal_type, "Habitat": habitat}:
                
                match habitat:
                    case "acqua":
                        print(f"l'animale {animale} è uno dei {animal_type} che può vivere nell'habitat {habitat}!")

                    case "terra" | "aria":
                        print(f"Non ho mai visto l'animale {animale} vivere nell'habitat {habitat}")

            #casi cane, gatto, cavallo, elefante, leone, serpente, lucertola
            case {"Nome": "cane", "Tipo": animal_type, "Habitat": habitat} | \
                 {"Nome": "gatto", "Tipo": animal_type, "Habitat": habitat} | \
                 {"Nome": "cavallo", "Tipo": animal_type, "Habitat": habitat} | \
                 {"Nome": "elefante", "Tipo": animal_type, "Habitat": habitat} | \
                 {"Nome": "leone", "Tipo": animal_type, "Habitat": habitat} | \
                 {"Nome": "serpente", "Tipo": animal_type, "Habitat": habitat} | \
                 {"Nome": "lucertola", "Tipo": animal_type, "Habitat": habitat}:
                
                match habitat:
                    case "terra":
                        print(f"l'animale {animale} è uno dei {animal_type} che può vivere nell'habitat {habitat}!")

                    case "aria" | "acqua":
                        print(f"Non ho mai visto l'animale {animale} vivere nell'habitat {habitat}")

            #casi aquila, pappagallo, gufo, falco, gallina, tacchino
            case {"Nome": "aquila", "Tipo": animal_type, "Habitat": habitat} | \
                 {"Nome": "pappagallo", "Tipo": animal_type, "Habitat": habitat} | \
                 {"Nome": "gufo", "Tipo": animal_type, "Habitat": habitat} | \
                 {"Nome": "falco", "Tipo": animal_type, "Habitat": habitat} | \
                 {"Nome": "gallina", "Tipo": animal_type, "Habitat": habitat} | \
                 {"Nome": "tacchino", "Tipo": animal_type, "Habitat": habitat}:
                
                match habitat:
                    case "terra" | "aria":
                        print(f"l'animale {animale} è uno dei {animal_type} che può vivere nell'habitat {habitat}!")

                    case "acqua":
                        print(f"Non ho mai visto l'animale {animale} vivere nell'habitat {habitat}")

            #casi cigno, anatra
            case {"Nome": "cigno", "Tipo": animal_type, "Habitat": habitat} | \
                 {"Nome": "anatra", "Tipo": animal_type, "Habitat": habitat}:
                
                match habitat:
                    case "acqua" | "aria" | "terra":
                        print(f"l'animale {animale} è uno dei {animal_type} che può vivere nell'habitat {habitat}!")


    elif opzione == "n":
        break

    elif opzione != "n" and opzione != "y":
        print("La prego di inserire una delle opzioni valide.")