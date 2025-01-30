# 15. Calcolo di intervalli condizionati

# Progettare un algoritmo che chieda all’utente di inserire un valore intero n.
# L'algoritmo deve:

#     Verificare se n è compreso tra 1 e 100:
#         se sì, calcolare e mostrare la somma di tutti i numeri pari compresi tra 1 e n.
#     Verificare se n è 0 o negativo:
#         Se sì, mostrare un messaggio di errore e terminare.
#     Altrimenti, calcolare e mostrare la somma di tutti i numeri dispari compresi tra 1 e n.



n = int (input("Inserisci un numero: "))
i = 0

if n >= 1 and n <= 100:
    intervallo_pari = ([i for i in range(1, n)])
    print(intervallo_pari)
