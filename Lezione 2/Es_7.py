cont = 0
sum = 0

scelta = str (input("Vuoi inserire un voto?: "))

while scelta == "si":
    voto = int (input("Inserisci un voto: "))

    if voto > 0:
        cont += 1
        sum += voto

    else: "Errore."
    
    scelta = str (input("Inserisci si o no: "))


if scelta == "no":
    media = sum/cont

    print(f"La media è: {media}")
