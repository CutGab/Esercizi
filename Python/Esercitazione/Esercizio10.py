# Scrivere un programma che permetta di analizzare una lista di numeri interi inseriti dall’utente.

# Il programma deve:

# acquisire una sequenza di numeri interi, terminando l’inserimento quando l’utente digita 0 (che non deve essere considerato nei calcoli);
# calcolare e visualizzare la somma di tutti i numeri pari inseriti;
# calcolare e visualizzare la media di tutti i numeri dispari inseriti;
# determinare e visualizzare il numero con la frequenza più alta (cioè quello che compare più volte nella lista);
# se più numeri hanno la stessa frequenza massima, visualizzarli tutti.
# Esempio di input e output
# Input:

# Inserisci un numero (0 per terminare): 4
# Inserisci un numero (0 per terminare): 7
# Inserisci un numero (0 per terminare): 2
# Inserisci un numero (0 per terminare): 7
# Inserisci un numero (0 per terminare): 3
# Inserisci un numero (0 per terminare): 4
# Inserisci un numero (0 per terminare): 0
# Output:

# Somma dei numeri pari: 10
# Media dei numeri dispari: 5.67
# Numero più frequente: 7 (2 volte)

#variabile che uso per calcolare la media
media = 0

#variabile che uso per calcolare la somma
somma = 0

#contatore che incrementa ogni volta che inserisco un numero dispari che servirà per trovare la media
cont_dispari = 0

#lista dei numeri inseriti dall'utente
numbers: list = []

#dizionario con coppia numero: frequenza 
frequenze: dict = {}

#ciclo infinito che si ripete finché il numero inserito non è 0 (non calcolato nelle operazioni)
while True:

    n = (float(input("Inserisci un numero (0 per terminare): ")))
    
    #se il numero è 0 interrompo il ciclo
    if n == 0:
        break

    #se il numero è intero proseguo    
    if n.is_integer() == True:

        #aggiungo il numero alla lista numbers
        numbers.append(int(n))

        #se è pari incremento somma
        if n%2 == 0:
            somma += n

        #se è dispari incremento media e contatore dispari
        else:
            media += n
            cont_dispari +=1

    #se il numero non è intero stampo errore e richiedo il numero in input           
    else:
        print("Errore i numeri devono essere interi.")

#itero sulla lista per trovare se un numero è presente nel dizionario frequenze
#se la chiave i è presente in frequenze, incremento di uno il suo valore
#altrimenti la imposto ad 1
for i in numbers:
    if i in frequenze:
        frequenze[i] += 1
        
    else:
        frequenze[i] = 1

#trovo il valore più grande presente all'interno del dizionario frequenze con la funzione values
frequenza_max = max(frequenze.values())

#stampa dei vari risultati
print(f"Somma dei numeri pari: {somma}")

print(f"Media dei numeri dispari: {media/cont_dispari}")

#itero sul dizionario frequenze e se la chiave j ha come valore corrispondente lo stesso di frequenza_max che ho calcolato in precedenza vuol dire che j è il/i numero/i che è/sono ripetuto/i più volte, dopodiché li stampa
for j in frequenze:
    if frequenze[j] == frequenza_max:
        print(f"numero più frequente: {j} ({frequenze[j]} volte)")