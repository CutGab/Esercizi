#3-1. Names: Store the names of a few of your friends in a list called names. 
#Print each person’s name by accessing each element in the list, one at a time.

Names: list = []

for i in range (5):
    name: str = (input("Insert a name: "))
    Names.append(name)


for name in Names:
    print(name)