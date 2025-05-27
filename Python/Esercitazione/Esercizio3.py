#Scrivere un programma che acquisisca una stringa inserita dall'utente e generi una nuova stringa che corrisponda alla versione invertita della stringa originale. 
#Il programma deve poi visualizzare la stringa ottenuta in output. 
#Per risolvere il problema non si deve utilizzare alcun tipo di funzione, ma esclusivamente i cicli.

#inserimento stringa
word: str = str(input("Inserisci una parola o una frase: "))

#variabile che uso per poi stampare la stringa invertita
rev: str = " "

#ciclo for che poi va a sommare i singoli caratteri alla variabile rev
#per esempio ciao sarà c + " ", i + c, a + ic, o + aic
for i in word:
    rev =  i + rev

#stampando infine la stringa invertita (in caso dell'esempio oaic)
print(rev)