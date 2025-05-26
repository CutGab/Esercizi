#Scrivere un programma che acquisisca una stringa inserita dall'utente e calcoli il numero totale di spazi presenti nella stringa. Il risultato deve essere visualizzato in output.

#inserimento stringa
word: str = str(input("Inserisci una parola o una frase: "))

#stampa del numero di spazi presenti nella stringa
print(f"Il numero di spazi presenti nella stringa è " + str(word.count(" ")))
