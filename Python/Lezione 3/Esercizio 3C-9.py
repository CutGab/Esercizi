coordinate: tuple = ()

x = (float(input("Inserisci il primo punto: ")))

y = (float(input("Inserisci il secondo punto: ")))

coordinate = x,y

match coordinate:

    case (0, 0):
        print("Il punto si trova in origine")

    case (x, 0):
        print("Il punto si trova sull'asse X.")

    case (0, y):
        print("Il punto si trova sull'asse Y.")

    case (x, y) if x > 0 and y > 0:
        print("Il punto si trova nel primo quadrante")

    case (x, y) if x < 0 and y > 0:
        print("Il punto si trova nel secondo quadrante")

    case (x, y) if x < 0 and y < 0:
        print("Il punto si trova nel terzo quadrante")

    case (x, y) if x > 0 and y < 0:
        print("Il punto si trova nel quarto quadrante")

print(coordinate)