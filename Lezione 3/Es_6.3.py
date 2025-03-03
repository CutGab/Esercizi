glossary: dict [str] = {"Indentation": "L'indentazione del codice, per una maggior leggibilità",
                        "Comments": "Sono stringhe di codice che non vengono lette e servono per far capire ad altri il codice che hai scritto",
                        "PEP8": "Documento con dentro le pratiche standard da seguire quando si scrive codice",
                        "Dead Code": "Codice che non verrà mai letto",
                        "Memory leak": "Consumo di memoria non voluto"
                        }

for i, values in glossary.items():

    print(f"{i}: {values}\n")