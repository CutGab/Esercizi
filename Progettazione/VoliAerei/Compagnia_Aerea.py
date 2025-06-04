from Anno import Anno

class CompagniaAerea:
    def __init__(self, nome: str, data_fondazione: Anno):
        # Validazione del nome (deve essere una stringa non vuota)
        if not nome or not isinstance(nome, str):
            raise ValueError("Il nome della compagnia deve essere una stringa non vuota.")
        
        self.set_nome(nome)
        self.data_fondazione = data_fondazione

    def get_nome(self) -> str:
        return self.nome

    def set_nome(self, nome: str):
        if not nome or not isinstance(nome, str):
            raise ValueError("Il nome della compagnia deve essere una stringa non vuota.")
        self.nome = nome

    def get_data_fondazione(self) -> Anno:
        return self.data_fondazione

    def __str__(self):
        return f"Compagnia: {self.nome}, Fondata nel: {self.data_fondazione}"