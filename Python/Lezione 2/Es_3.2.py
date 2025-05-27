# 3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, print a message to them. 
# The text of each message should be the same, but each message should be personalized with the person’s name.

Names: list = []

for i in range (5):
    name: str = (input("Insert a name: "))
    Names.append(name)


for name in Names:
    print(f"Giochiamo a pallone {name}")
