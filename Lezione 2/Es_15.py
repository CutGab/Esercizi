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
somma = 0

if n < 0 or n == 0:
    print("Il numero non può essere negativo.")
    exit(0)

elif n >= 1 and n <= 100:
    for i in range(1, n):
        if i%2 == 0:
             somma = somma + i

elif n > 100:
        for i in range(1, n):
            if i%2 != 0:
                 somma = somma + i

print(f"la somma dei numeri pari equivale a: {somma}")