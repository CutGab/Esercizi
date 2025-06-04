from CodiceIATA import CodiceIATA

class Aeroporto:
    def __init__(self, codice: CodiceIATA, nome: str):
        # Validazione del nome (deve essere una stringa non vuota)
        if not nome or not isinstance(nome, str):
            raise ValueError("Il nome dell'aeroporto deve essere una stringa non vuota.")
        
        self.codice = codice
        self.nome = nome

    def get_codice(self) -> CodiceIATA:
        return self.codice

    def get_nome(self) -> str:
        return self.nome

    def set_nome(self, nome: str):
        if not nome or not isinstance(nome, str):
            raise ValueError("Il nome dell'aeroporto deve essere una stringa non vuota.")
        self.nome = nome

    def __str__(self):
        return f"Aeroporto: {self.nome}, Codice IATA: {self.codice}"