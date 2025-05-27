lanci:int = 0

tot_testa: int = 0

tot_croce: int = 0

while lanci < 8:

    lancio = input(f"Lancio {lanci}: ")

    match lancio:
        
        case lancio if lancio == "t" | "T":
            tot_testa += 1
            lanci += 1

        case lancio if lancio == "c" | "C":
            tot_croce += 1
            lanci += 1

        case _:
            print("Lancio non valido, riprovare.")
    
percentuale_testa = (tot_testa * 100 / lanci)

percentuale_croce = (tot_croce * 100 / lanci)


print(f"Totale Testa = {tot_testa}\n"
      f"Percentuale: {percentuale_testa: .2f}%")

print(f"Totale Croce = {tot_croce}\n"
      f"Percentuale: {percentuale_croce: .2f}%")