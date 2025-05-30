#Scrivere un programma che acquisisca in input due numeri interi, n1 e n2, e calcoli il prodotto di tutti i numeri compresi tra n1 e n2, inclusi gli estremi.
#Il programma deve gestire anche il caso in cui n1 > n2, calcolando comunque il prodotto correttamente.

n1 = (int(input("Inserisci il primo numero: ")))

n2 = (int(input("Inserisci il secondo numero: ")))

#variabile che utilizzo per calcolare il prodotto
prodotto: int = 1

#controllo il caso in cui il primo numero dato sia maggiore del secondo
if n1 > n2:
    for i in range(n2, n1+1):
        prodotto = prodotto * i
        i -= 1

#ciclo per calcolare il prodotto dei numeri compresi tra n1 e n2 estremi inclusi
for i in range (n1, n2+1):
    prodotto = prodotto * i
    i +=1

#stampa del risultato
print(f"Il prodotto tra tutti i numeri compresi tra {n1} e {n2} estremi inclusi equivale a {prodotto}")