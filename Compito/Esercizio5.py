# Si supponga di poter acquistare barrette di cioccolato da un distributore automatico al costo di 1 euro ciascuna. 
# Ogni barretta acquistata contiene un buono sconto, e con 6 buoni sconto si ottiene una barretta gratuita.

# Scrivere un programma che:

# Acquisisca in input un valore N (numero di euro disponibili).
# Calcoli e mostri in output il numero totale di barrette che si possono ottenere, considerando anche quelle ottenute con i buoni sconto.
# Mostri quanti buoni sconto avanzano al termine dell'acquisto.
# Esempio:
# Se l'utente inserisce N = 6, può acquistare 6 barrette ottenendo 6 buoni sconto, che gli permettono di riscattare 1 ulteriore barretta gratuita, per un totale di 7 barrette. Alla fine, non rimarranno buoni sconto inutilizzati.

# Il programma deve continuare a scambiare i buoni con nuove barrette finché ce ne sono abbastanza per ottenere almeno una barretta gratuita.

euro = (float(input("Inserire quanti euro ha disponibili: ")))

barretta_costo = 1.00

#numero buoni sconto
buono_sconto = 0

#numero barrette acquistate
numero_barrette = 0

#ciclo che va ad aumentare di uno il numero di barrette, a diminuire i soldi rimanenti e incrementare i numeri di buoni finché i buoni non arrivano a un multiplo di 6
#dopodiché perdi 6 buoni ma guadagni una barretta extra
while euro >= barretta_costo:

        numero_barrette +=1
        buono_sconto += 1
        euro -= barretta_costo
        
        if numero_barrette % 6 == 0:
              numero_barrette +=1
              buono_sconto -= 6

#stampa del numero barrette che puoi acquistare e i buoni rimanenti
print(f"Lei può comprare un numero totale di {numero_barrette} barrette.")
print(f"Le rimangono {buono_sconto} buoni sconto disponibili.")