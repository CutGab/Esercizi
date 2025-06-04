from RealGEZ import RealGEZ

class Citta:
    def __init__(self, nome: str, num_abitanti: RealGEZ):
        # Validazione del nome (deve essere una stringa non vuota)
        if not nome or not isinstance(nome, str):
            raise ValueError("Il nome della città deve essere una stringa non vuota.")
        
        if num_abitanti <= 0:
            raise ValueError("Il numero di abitanti deve essere un valore maggiore di 0.")
        
        self.set_nome(nome)
        self.set_num_abitanti(num_abitanti)

    def get_nome(self) -> str:
        return self.nome

    def set_nome(self, nome: str):
        if not nome or not isinstance(nome, str):
            raise ValueError("Il nome della città deve essere una stringa non vuota.")
        self.nome = nome

    def get_num_abitanti(self) -> RealGEZ:
        return self.num_abitanti

    def set_num_abitanti(self, num_abitanti: RealGEZ):
        if num_abitanti <= 0:
            raise ValueError("Il numero di abitanti deve essere un valore maggiore di 0.")
        self.num_abitanti = num_abitanti

    def __str__(self):
        return f"Città: {self.nome}, Numero di abitanti: {self.num_abitanti}"