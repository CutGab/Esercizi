from Person import Persona
from studente import Studente

fm: Persona = Persona ("Federico", "March", 29)

# creare un'ggetto della classe Studente

s1: Studente = Studente ("Gabbrone", "Ciccio", 21, "BLABLA")

print(s1)

# controllo che s1 sia istanza della classe Studente
# usiamo isistance(obj, Class) > controlla che l'oggetto obj sia istanza della classe Class.
# In caso affermativo ritorna True
# In caso negativo    ritorna False


if isinstance(s1, Studente):

    print("\nStudente è istanza della classe Studente")

if isinstance(s1, Persona):

    print("\nStudente è anche istanza della classe Persona")

if isinstance(fm, Studente):

    print("\nL'oggetto fm è istanza della classe Persona")

else: 

    print("\nL'oggeto s1 non è istanza della classe Persona")

#controllare che la classe Studente sia sottoClasse della classe Persona
#issubClass(Class, Class) controlla se Class1 sia sottoclasse della classe Class2

if issubclass(Studente, Persona):
    print("\nLa classe Studente è sottoclasse della classe Persona")