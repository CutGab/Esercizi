#3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and now you have space for only two guests.
# • Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
# • Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
# • Print a message to each of the two people still on your list, letting them know they’re still invited.
# • Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.

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

Invited.insert(2, "Mirco")

Invited.append("Massimo")

print(Invited)


print(f"Nevermind I can only invite 2 guests.")

print(f"Sorry {Invited[5]} you can't come")
Invited.pop(5)
print(f"Sorry {Invited[4]} you can't come")
Invited.pop(4)
print(f"Sorry {Invited[3]} you can't come")
Invited.pop(3)
print(f"Sorry {Invited[2]} you can't come")
Invited.pop(2)

print(f"Only {Invited[0]} can come.")

print(f"Only {Invited[1]} can come.")

del Invited[1]

del Invited[0]

print(Invited)