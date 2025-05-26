# Il valore di π può essere approssimato utilizzando la seguente serie infinita:

# π = 4 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 + ...

# Scrivere un programma che calcoli il valore di π utilizzando questa serie e determini quanti termini sono necessari per ottenere approssimazioni sempre più accurate. Quindi:

# progettare un algoritmo che mostri in output quanti termini della serie devono essere usati per ottenere il valore di π ≈ 3.14;
# modificare l'algoritmo, mostrando in output quanti termini della serie devono essere usati per ottenere il valore di π ≈ 3.141;
# modificare l'algoritmo, mostrando in output quanti termini della serie devono essere usati per ottenere il valore di π ≈ 3.1415;
# modificare l'algoritmo, mostrando in output quanti termini della serie devono essere usati per ottenere il valore di π ≈ 3.14159.
# Nota: Il programma deve iterare fino a raggiungere ciascuna delle soglie indicate, contando il numero di termini necessari.

denominatore: int = 1

target: list = [3.14, 3.141, 3.1415, 3.14159]

pi = 0

termini = 0

#ciclo che uso per iterare su ogni valore di target
for i in target:

    #ciclo infinito che applica Leibniz, andando a sottarre o aggiungere il termine a pi a seconda dell'indice pari o dispari
    while True:
        if termini % 2 == 0:
            pi = pi + 4/denominatore
        else:
            pi = pi - 4/denominatore
        
        denominatore += 2
        termini += 1

        # 1e-5 è una notazione usata per rappresentare 0.00001 (sarebbe 1 * 10^-5)
        # In pratica quando nota che che la differenza tra il valore corrente di p e il nostro target è inferiore a 0.00001 il ciclo si interrompe
        # Abs invece è una funzione che restituisce un numero sempre positivo
        # Permette di approssimare sena preoccuparsi che la differenza sia negativa o positiva
        if abs (pi - i) < 1e-5:
            break

    print(f"Per raggiungere {i}, sono serviti {termini} termini.")
