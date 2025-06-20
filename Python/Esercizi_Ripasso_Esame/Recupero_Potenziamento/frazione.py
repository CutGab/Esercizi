class Frazione:

    def __init__(self, numeratore = 13, denominatore = 5):

        self.setNumeratore(numeratore)
        self.setDenominatore(denominatore)

    def setNumeratore(self, numeratore: int):

        if isinstance(numeratore, int):
            self.__numeratore = numeratore

        else:
            raise TypeError("Il numeratore deve essere un numero intero!")

    def setDenominatore(self, denominatore: int):

        if denominatore == 0:
            raise ValueError("Il denominatore non può essere uguale a 0!")

        if isinstance(denominatore, int):
            self.__denominatore = denominatore

        else:
            raise TypeError("Il denominatore deve essere un numero intero!")

    def getNominatore(self):

        return self.__numeratore
    
    def getDenominatore(self):

        return self.__denominatore
    
    def __str__(self):

        return (f"{self.__numeratore}/{self.__denominatore}")
    
    def value(self):

        return round(self.__numeratore/self.__denominatore, 3)
    
# frazione = Frazione(1, 20)
# print(frazione.__str__())
# print(frazione.value())


def mcd(x: int, y: int):

        divisori: list = []

        i = 1
        
        for i in range(1, min(x,y) + 1):

            if y%i == 0 and x%i == 0:

                divisori.append(i)

                i+= 1

            else:

                i+= 1

        return max(divisori)

# print(mcd(12,18)) #Output 6

l = [
    Frazione(1, 2),
    Frazione(3, 4),
    Frazione(5, 6),
    Frazione(7, 8),
    Frazione(9, 10)
]

def semplifica(lista: list):
    new_list: list = []

    for element in lista:
        numeratore = element.getNominatore()
        denominatore = element.getDenominatore()

    if mcd(numeratore, denominatore) > 1:
            numeratore = numeratore // mcd(numeratore, denominatore)
            denominatore = denominatore // mcd(numeratore, denominatore)
            new_list.append(f"{numeratore}/{denominatore}")
            
    if mcd(numeratore, denominatore) == 1:
        new_list.append(str(element))


    return new_list


print(semplifica(l))



