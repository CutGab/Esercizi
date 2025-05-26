#Scrivere un programma che permetta all'utente di inserire una serie di parole in input, terminando l'inserimento quando viene digitata la parola "fine" (che non deve essere considerata nell'elaborazione).
#Per ogni parola inserita, il programma deve verificare se il primo e l'ultimo carattere sono uguali e visualizzare un messaggio corrispondente.

answer: str = None

#ciclo per l'inserimeto delle parole
while answer != "fine":
    
    #scelta utente
    answer: str = str(input("Vuoi inserire una parola? (Si/Fine)").lower())

    #controllo che l'utente voglia inserire un'ulteriore parola, altrimenti termino
    if answer == "fine":
        exit()

    #controllo se l'utente ha scelto un'opzione diversa
    if answer != "si" and answer != "fine":
        print("La prego di inserire una delle due opzioni.")
        continue
    
    #insertimento stringa
    word: str = str(input("Inserisci una parola: ").lower())
    
    #controllo che la stringa sia effettivamente una parola unica
    if word.count(" ") > 0:
        print("Errore, la parola non può contenere spazi.")
        continue

    #controllo che il primo e l'ultimo carattere della stringa combaciano
    match word:
         case word if word[0] == word[-1]:
            print(f"Il primo e l'ultimo carattere di {word} combaciano!")
