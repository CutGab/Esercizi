oggetti: list = []

for i in range (3):
    oggetto = (str(input("Inserisci un oggetto: ")))
    oggetti.append(oggetto.lower())


match oggetti:

    case oggetti if oggetti == ["penna", "matita", "quaderno"]:
        print("Materiale scolastico")

    case oggetti if oggetti == ["pane", "uova", "latte"]:
        print("Prodotti alimentari")

    case oggetti if oggetti == ["sedia", "tavolo", "armadio"]:
        print("Mobili")

    case oggetti if oggetti == ["telefono", "computer", "tablet"]:
        print("Materiale scolastico")

    case _:
        print("Categoria sconosciuta")