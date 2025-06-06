def Action (numbers: list):

    if len(numbers) < 3 and  numbers[0] == 1 or numbers[2] == 5:

        print("Azione permessa")

    else:

        print("Azione negata")

    
Action([1, 2, 5])
Action([0, 2, 5])
Action([1, 4, 8])