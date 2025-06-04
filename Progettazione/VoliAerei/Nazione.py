class Nazione:
    def __init__(self, nome: str):
        # Validazione del nome (deve essere una stringa non vuota)
        if not nome or not isinstance(nome, str):
            raise ValueError("Il nome della nazione deve essere una stringa non vuota.")
        
        self.set_nome(nome)

    def get_nome(self) -> str:
        return self.nome

    def set_nome(self, nome: str):
        if not nome or not isinstance(nome, str):
            raise ValueError("Il nome della nazione deve essere una stringa non vuota.")
        self.nome = nome

    def __str__(self):
        return f"Nazione: {self.nome}"