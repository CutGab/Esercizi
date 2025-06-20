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
        return (f"Alieno: {self.getNome()}")

class Mostro(Creatura):
    def __init__(self, nome, urlo_vittoria: str = "GRAAAHHH", gemito_sconfitta: str = "Uuurghhh"):
        super().__init__(nome)

        self.__setAssalto()
        self.__setVittoria(urlo_vittoria)
        self.__setSconfitta(gemito_sconfitta)
        
        # Modifica del nome della creatura
        # in modo che le lettere in posizione pari siano minuscole e quelle in posizione dispari
        nome = super().getNome()
        self.risultato = ""
        for i, c in enumerate(nome):
            self.risultato += c.lower() if i % 2 == 0 else c.upper()

    def __setAssalto(self):

        self.assalto: list =[random.randint(1, 100) for i in range (1, 15)]

    def getAssalto(self):
        return self.assalto
    
    def __setVittoria(self, urlo_vittoria):
        if isinstance(urlo_vittoria, str):
            self.urlo_vittoria = urlo_vittoria
        else:
            self.urlo_vittoria = "GRAAAHHH"

    def __setSconfitta(self, gemito_sconfitta):
        if isinstance(gemito_sconfitta, str):
            self.gemito_sconfitta = gemito_sconfitta
        else:
            self.gemito_sconfitta = "Uuurghhh"

    def getVittoria(self):
        return self.urlo_vittoria
    
    def getSconfitta(self):
        return self.gemito_sconfitta

    def __str__(self):
        return (f"Mostro: {self.risultato}")

def pariUguali(a: list[int], b: list[int]):
    c: list[int] = []

    for i in range(min(len(a), len(b))):
        if a[i] % 2 == 0 and b[i] % 2 == 0:
            c.append(1)
        else:
            c.append(0)
    return c

def combattimento(a: Alieno, m: Mostro):
    
    if isinstance(a, Alieno) and isinstance(m, Mostro):
        munizioni = a.getMunizioni()
        assalto = m.getAssalto()
        risultato = pariUguali(munizioni, assalto)

        if risultato.count(1) > 4:
            for i in range(3):
                print(m.getVittoria())
            print("")
            print("I Mostri hanno vinto!")
            print("")
            proclamaVincitore(m)

        else:
            for i in range(3):
                print(m.getSconfitta())
            print("")
            print("Gli Alieni hanno vinto!")
            print("")
            proclamaVincitore(a)

def proclamaVincitore(c: Creatura):

    if isinstance(c, Alieno):
        etichetta = f"{c.__str__()}"

    elif isinstance(c, Mostro):
        etichetta = f"{c.__str__()}"

    else:
        etichetta = f"Creatura: {c.getNome()}"

    larghezza = len(etichetta) + 10
    bordo = '*' * larghezza
    spazio = ' ' * (larghezza - 2)

    print(bordo)
    print(spazio)
    print('*' + spazio + '*')
    print(spazio)
    print('*' + etichetta.center(larghezza - 2) + '*')
    print(spazio)
    print('*' + spazio + '*')
    print(spazio)
    print(bordo)

def main():
    a1 = Alieno("Robot")
    print(a1.__str__())
    print(a1.getMunizioni())

    print("")

    m1 = Mostro("GODZILLA")
    print(m1.__str__())
    print(m1.getAssalto())

    print("")

    combattimento(a1, m1)

main()


