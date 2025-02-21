pizzas: list =  []

for i in range (3):
    p = (input("Insert a pizza you like: "))
    pizzas.append(p)

for p in pizzas:
    print(p)

for p in pizzas:
    print(f"I really like {p}!")

print("I'm crazy for pizza,\nIt's so good!\nI love pizza!")