import random

class Die:

    def __init__(self, sides):

        self.sides = sides

    def roll_die (self):
        
        print(random.choice(range(1, self.sides)))



d1 = Die (6)

d2 = Die (10)

d3 = Die (20)


d1.roll_die()
d2.roll_die()
d3.roll_die()







