#Scrivere un programma che consenta all'utente di inserire una sequenza di numeri reali non negativi (sia interi che decimali). 
#L'inserimento termina quando viene fornito un numero negativo, che funge da sentinella e non deve essere considerato nei calcoli.
#Il programma deve:
# - Calcolare la media dei soli numeri interi inseriti. Utilizzate la funzione is_integer() per verificare se il numero inserito è un intero.
# - Determinare e visualizzare il numero più grande e il numero più piccolo tra tutti quelli inseriti (sia interi che decimali).

#variabile dove sommo i numeri inseriti per la media
media = 0

#variabile per stabilire il numero più grande
num_max = 0

#variabile per stabilire il numero più piccolo
num_min = 0

#variabile che userò per inserire i numeri
n: float = 1.0

#Contatore dei numeri inseriti per la media
i = 0
    
#ciclo per l'inserimeto dei numeri    
while n > 0:
    
    n = (float(input("insert a number: ")))

    #controllo numero più grande e più piccolo
    if n > num_max:
        num_max = n

    if n < num_min:
        num_min = n
    
    #controllo che il numero sia intero e non negativo e lo sommo alla media, aggiornando il contatore
    if n.is_integer() == True and n > 0:
        media += n
        i += 1

#stampa media, numero più piccolo e numero più grande
print(f"La media dei numeri interi positivi inseriti equivale a {media/i}.")

print(f"Il numero più grande tra quelli inseriti equivale a {num_max}.")

print(f"Il numero più piccolo tra quelli inseriti equivale a {num_min}.")

