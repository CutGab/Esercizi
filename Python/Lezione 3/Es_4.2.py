#4-2. Animals: Think of at least three different animals that have a common characteristic. 
# Store the names of these animals in a list, and then use a for loop to print out the name of each animal.
# • Modify your program to print a statement about each animal, such as A dog would make a great pet.
# • Add a line at the end of your program, stating what these animals have in common. 
# You could print a sentence, such as Any of these animals would make a great pet!

animals: list =  []

for i in range (3):
    a = (input("Insert an animal you like: "))
    animals.append(a)


animals.sort()

for a in animals:
    print(a)


for p in animals:
    print(f"A {p} would make a great pet")


print("These animals have in common the fact that they're animals.")