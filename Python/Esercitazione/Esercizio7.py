#Scrivere un programma che inizializzate due liste a e b della stessa lunghezza n, entrambe contenenti valori interi, calcoli la somma incrociata degli elementi.

#Esempio:

#a[1] + b[n-1], a[2] + b[n-2], ...


#definisco la lunghezza delle liste
elementi = (int(input("Inserisci quanti elementi entrambe le liste dovranno avere: ")))

a: list = []

b: list = []

c: list = []

#aggiungo elementi alla lista a e controllo che siano numeri interi
while len(a) < elementi:
    n = (float(input("Inserisci un numero alla prima lista: ")))
    if n.is_integer() == True:
        a.append(int(n))
    else: 
        print("Errore, i numeri devono essere interi.")

#aggiungo elementi alla lista b e controllo che siano numeri interi
while len(b) < elementi:
    n = (float(input("Inserisci un numero alla seconda lista: ")))
    if n.is_integer() == True:
        b.append(int(n))
    else: 
        print("Errore, i numeri devono essere interi.")


#scorro entrambe le liste, se per esempio elementi == 3, quando i == 0 prendera a[0], il suo primo elemento 
#mentre invece "elementi - 1 - i" corrisponde a 3 - 1 - 0 = 2, andando a prendere b[2], ovvero l'ultimo elemento di b
#quando i == 1, prenderà a[1] e 3 - 1 - 1 = 2, ovvero b[1], e così via
for i in range(elementi):
    somma = a[i] + b[elementi - 1 - i]
    c.append(somma)

print(c)
