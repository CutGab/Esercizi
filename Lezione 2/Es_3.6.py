#3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
# • Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, informing people that you found a bigger table.
# • Use insert() to add one new guest to the beginning of your list.
# • Use insert() to add one new guest to the middle of your list.
# • Use append() to add one new guest to the end of your list.
# • Print a new set of invitation messages, one for each person in your list.

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


print("I just found a bigger table!")

Invited.insert(0,"Lucas")

Invited.insert(len(Invited)//2, "Mirco")

Invited.append("Massimo")

for name in Invited:
    print(f"Congratulation {name}, you are invited to my dinner!")