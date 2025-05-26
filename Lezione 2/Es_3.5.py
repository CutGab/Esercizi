# 3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. 
# You’ll have to think of someone else to invite.
# • Start with your program from Exercise 3-4. Add a print() call at the end of your program, stating the name of the guest who can’t make it.
# • Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
# • Print a second set of invitation messages, one for each person who is still in your list.


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