import random
import time

class Creatura:
    def __init__(self, nome="Creatura Generica"):
        self.setNome(nome)

    def setNome(self, nome):
        if isinstance(nome, str):
            self._nome = nome
        else:
            self._nome = "Creatura Generica"

    def getNome(self):
        return self._nome

    def __str__(self):
        return f"Nome Creatura: {self._nome}"


class Alieno(Creatura):
    def __init__(self, nome):
        super().__init__(nome)

        self.__setMatricola()
        self.__setMunizioni()

        if nome != "Robot":
            print("Attenzione! Tutti gli Alieni devono avere il nome 'Robot' seguito dal numero di matricola! Reimpostazione nome Alieno in corso!")
            time.sleep(3)
            super().setNome(f"Robot-{self.__matricola}")

        else:
            super().setNome(f"Robot-{self.__matricola}")

    def __setMatricola(self):
        self.__matricola = random.randint(10000, 90000)

    def getMatricola(self):
        return self.__matricola

    def __setMunizioni(self):
        self.__munizioni = [i**2 for i in range(1, 16)]

    def getMunizioni(self):
        return self.__munizioni

    def __str__(self):
        return (f"Alieno: {self.getNome()}, "
                f"Matricola: {self.__matricola}, "
                f"Munizioni: {self.__munizioni}")


# c1 = Creatura("DISMOND")
# print(c1)

a1 = Alieno("Robot")
print(a1)
