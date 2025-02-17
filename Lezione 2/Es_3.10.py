things: list = []

for i in range (4):
    t = (input("Insert something: "))
    things.append(t)

print(len(things))

print(things)

print(sorted(things))

things.reverse()

print(things)

things.sort()

print(things)

things.pop(1)

print(things)

del things[2]

print(things)

