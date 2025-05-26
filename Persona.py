'''

Di una persona dobbiamo sapere delle informazioni.
Queste informazioni vengno chiamate attributi (della classe Persona)
Le informazioni saranno:

    - Nome
    - Cognome
    - Età

Come li rappresento in Python?

    self.name: str = name
    self.last_name: str = last_name
    self.age: int = age

'''

class Persona:

    # costruttore della classe Persona

    def __init__(self, name, last_name, age):

        self.name = name
        self.last_name = last_name
        self.age = age

    # funzione che mostri in output tutti i dati di una persona

    def displayData(self):
        
        print(f"Name: {self.name}\nCognome: {self.last_name}\nEtà: {self.age}")


g: Persona = Persona("Gabriele", "Cutolo", 21)


g.displayData()