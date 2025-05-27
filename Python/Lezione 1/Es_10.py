r = float (input("Inserisci il reddito familiare: ")) 
m = float (input("Inserisci la media dei voti: "))

if r < 20000 and m > 27:
    print ("Borsa di studio approvata.")

else:
    print("Borsa di studio rifiutata (Motivo: Reddito o Media insufficiente.)")