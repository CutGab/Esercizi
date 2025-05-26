Invited: list = []

for i in range (3):
    name: str = (input("Insert the guest's name: "))
    Invited.append(name)


for name in Invited:
    print(f"Congratulation {name}, you are invited to my dinner!")


print(f"Sadly, {Invited[1]} can't make it to the dinner.")

Invited[1] = "Domingo"

for name in Invited:
    print(f"Congratulation {name}, you are invited to my dinner!")

print(len(Invited))