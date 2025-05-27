from Person import Persona


fm: Persona = Persona()

# richiamo il metodo __str__ della classe Persona per mostrare in output le informazioni relative all'oggetto fm 
print(fm)

print("--------------")

msg = str(fm)
print(msg)

# modifico il nome della persona fm 
fm.setName("Federico")

print("--------------")

print(fm)

# modifico il cognome della persona fm
fm.setLastname("March")

# modifico l'età della persona fm
fm.setAge(29)

print("--------------")

print(fm)

print("--------------")
print(fm.getName(), fm.getLastname(), fm.getAge())