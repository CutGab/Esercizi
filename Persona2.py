class Persona:
    def __init__(self):

        self.name = ""
        self.last_name = ""
        self.age = 0

    def displayData(self):
        
        print(f"Name: {self.name}\nCognome: {self.last_name}\nEtà: {self.age}")

    #mi consente di impostare un valore per self.name, self.last_name e self.age

    def setName(self, name: str):
        self.name = name

    def setLastName(self, last_name: str):
        self.last_name = last_name
    
    def setAge(self, age: int):
        self.age = age

        if age < 0 or age > 130:
            self.age = 0
    
    #Lettura variabili

    def getName (self) -> str:
        return self.name
    
    def getLastName (self) -> str:
        return self.last_name
    
    def getAge (self) -> int:
        return self.age

g : Persona = Persona()

g.setName("Gabriele")
g.setLastName("Cutolo")
g.setAge(21)

g.displayData()

print("----------------------")

print(g.getName(), g.getLastName(), g.getAge())