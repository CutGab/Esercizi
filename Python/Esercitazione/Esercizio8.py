# Un'applicazione interessante dei computer è la rappresentazione grafica di dati.
# Scrivere un programma che acquisisca cinque numeri interi (ognuno compreso tra 1 e 30) e visualizzi in output un grafico a barre testuale con asterischi *.

# Per ogni numero letto, il programma deve stampare una riga contenente tanti asterischi quanti il valore del numero stesso.

# Esempio di output:
# Se l'utente inserisce i numeri 5, 8, 3, 12, 7, il programma deve stampare:

# *****
# ********
# ***
# ************
# *******

#lista in cui vado a salvare i numeri che l'utente inserisce da input
numbers: list  = []

#contatore che controlla che l'utente inserisca 5 numeri
i = 0

#ciclo while in cui l'utente inserisce i numeri in input, controllo che il numero sia compreso nell'intervallo tra 1 e 30 e che sia intero
while i < 5:
    n = (float(input("Inserisci un numero compreso tra 1 e 30: ")))
    if n.is_integer() == True and n >= 1 and n <= 30:
        i += 1
        numbers.append(int(n))


    else:
        print("Errore, i numeri devono essere interi e compresi tra 1 e 30.")

#ciclo e stampo un numero di * pari al prodotto di un asterisco e ogni elemento presente nella lista numbers
for j in numbers:
    print("*" * j)