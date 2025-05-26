age: int = (int(input("Inserisci la tua età: ")))

if age < 2:
    print("Sei un bimbo")

elif age >= 2 and age < 4:
    print("Sei un regazzino")

elif age >= 4 and age < 13:
    print("Sei un kid")

elif age >= 13 and age < 20:
    print("sei un teenager")

elif age >= 20 and age < 65:
    print("Sei un adult")

else:
    print("Sei un anziano")