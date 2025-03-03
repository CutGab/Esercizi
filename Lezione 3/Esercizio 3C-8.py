frase = (input("Inserisci una frase: "))

match frase:

    case frase if frase[-1] == "?" and len(frase) % 2 ==0:
        print("Sì!")

    case frase if frase[-1] == "?" and len(frase) % 2 !=0:
        print("No!")

    case frase if frase[-1] == "!":
        print("Wow!")

    case _:
        print('Tu dici ' + f'"{frase}"')