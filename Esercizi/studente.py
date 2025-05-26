from Person import Persona

class Studente(Persona):

    '''
    Attributi della classe Persona (in quanto Studente eredita da PErsona)
    self.name: str
    self.lastname: str
    self.age: int

    Attributi della classe Studente
    self.matricola: str
    '''

    def __init__(self, name: str, lastname: str, age: int, matricola: str):

        #inizializzare la classe Persona richiamando il metodo init della superclasse
        super().__init__(name, lastname, age)

        #istruzioni che inizializzano un'oggeto della classe Studente
        self.setMatricola(matricola)

    #metodi setter

    #metodo che imposta il valore dell'attributo self.matricola

    def setMatricola (self, matricola):

        if matricola:
            self.matricola = matricola

        else:
            
            print("Errore! La matricola non può essere rappresentata da una stringa vuota")

    #metodo getter

    #metodo che ritorna il valore di self.matricola

    def getMatricola(self):

        return self.matricola
    

    def __str__(self):

        return f"Nome: {self.name}\nCognome: {self.getLastname()}\nMatricola: {self.getMatricola()}"


