#3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? 
# Make a list that includes at least three people you’d like to invite to dinner. 
# Then use your list to print a message to each person, inviting them to dinner.

Invited: list = []

for i in range (3):
    name: str = (input("Insert the guest's name: "))
    Invited.append(name)


for name in Invited:
    print(f"Congratulation {name}, you are invited to my dinner!")
