from datetime import date
from custom_types import RealGEZ
from dataclasses import dataclass

class Impiegato():

    _nome: str #mutabile
    _cognome: str #mutabile
    _data_nascita: date #immutabile
    _stipendio: RealGEZ #mutabile

    def __init__(self, nome: str, cognome: str, data_nascita: str, stipendio: RealGEZ) -> None:

        self.set_nome(nome)
        self.set_cognome(cognome)
        self._data_nascita = data_nascita
        self.set_stipendio(stipendio)


    def __str__(self) -> str:
        
        return f"Nome: {self._nome}\n\
                Cognome: {self._cognome}\n\
                Data di Nascita: {self._data_nascita}\n\
                Stipedio: {self._stipendio}"

    def set_nome(self, new_name: str):
        self._nome = new_name         
    
    def get_nome(self):
        return self._nome
    
    def set_cognome(self, new_cognome: str):
        self._nome = new_cognome    
    
    def get_cognome(self):
        return self._cognome
    
    def get_data_nascita(self):
        return self._data_nascita
    
    def set_stipendio(self, new_stipendio: RealGEZ):
        self._stipendio = new_stipendio
        
    def get_stipendio(self):
        return self._stipendio