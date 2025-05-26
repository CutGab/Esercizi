# Progettare un algoritmo che simuli un gioco basato sul lancio di due dadi virtuali a sei facce, D1 e D2. L'algoritmo deve eseguire le seguenti operazioni:

#     Simulare il lancio dei due dadi.
#     Calcolare la somma dei valori ottenuti dai due dadi.
#     Applicare le seguenti regole di gioco per determinare il punteggio:
#         Se entrambi i dadi mostrano numeri pari e la somma è maggiore di 8, il giocatore vince e il punteggio è impostato direttamente a 100.
#         Se uno dei dadi mostra 6 oppure la somma è uguale a 7, il punteggio del giocatore viene incrementato di 10.
#         In tutti gli altri casi, il giocatore perde e il punteggio è impostato a 0.
#     Mostrare il risultato del gioco e il punteggio ottenuto.

# Il gioco continua finché il punteggio totale del giocatore non raggiunge 100 (vittoria) oppure scende a zero (sconfitta).


import random

D1: list = [1, 2, 3, 4, 5, 6]
D2: list = [1, 2, 3, 4, 5, 6]

punteggio = 0

while punteggio != 100:

    lancio_1 = random.choice(D1)
    lancio_2 = random.choice(D2)

    somma = lancio_1 + lancio_2
    
    if lancio_1%2 == 0 and lancio_2%2 == 0 and somma > 8:
        punteggio = 100
        print ("Complimenti, la somma dei dadi è pari, hai vinto!")
        print(punteggio)
        
    elif lancio_1 == 6 or lancio_2 == 6 or somma == 7:
        punteggio += 10
        print ("Complimenti, il tuo punteggio è aumentato di 10!")
        print (punteggio)
        
    else:
        punteggio = 0
        print ("Spiacenti, hai perso.")
        print (punteggio)
        break


