soglia = int (input("Quanto è la soglia di veicoli massimi possibili: "))

num_NS = int (input("Quanti veicoli stanno arrivando da direzione Nord-Sud: "))
num_EO = int (input("Quanti veicoli stanno arrivando da direzione Est-Ovest: "))

priorità = int (input("Quanto vale la priorità del semaforo: "))

if num_NS > soglia:
    if num_EO > soglia:
        tempo_NS = 50
        tempo_EO = 50

    else:
        tempo_NS = priorità
        tempo_EO = 100 - priorità

    
else:
    if num_EO > soglia:
        tempo_NS = 100 - priorità
        tempo_EO = priorità

    else:
        veicoli_tot = num_NS + num_EO
        tempo_NS = num_NS/veicoli_tot*100
        tempo_EO = 100 - tempo_NS



print(f"La priorità per i veicoli da Est-Ovest è settata a: {tempo_EO}")
print(f"La priorità per i veicoli da Nord-Sud è settata a: {tempo_NS}")

