pizzas: list =  []

friend_pizzas: list = []


for i in range (3):
    p = (input("Insert a pizza you like: "))
    pizzas.append(p)

for p in pizzas:
    print(p)

for p in pizzas:
    print(f"I really like {p}!")

print("I'm crazy for pizza,\nIt's so good!\nI love pizza!")

#[:] crea una copia della lista 
friend_pizzas = pizzas[:]

pizzas.append("Bolognese")

friend_pizzas.append("Con i funghi")

print("My favorite pizzas are: ")

for j in pizzas:
    print(j)

print("My friend's favorite pizzas are: ")

for k in friend_pizzas:
    print(k)
