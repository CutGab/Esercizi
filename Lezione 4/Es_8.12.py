def sandwiches_items (*args):
    
    sandwich: list = []

    while True:

        option = (input("Vuoi inserire un condimento all'interno del sandwich?: (Y/N)").lower())

        if option == "y":

            item = (input("Inserisci un condimento: "))
            sandwich.append(item)

        elif option == "n":

            break

    return sandwich 

print(sandwiches_items())