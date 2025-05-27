from custom_types import Indirizzo

class Dipartimento:

    _nome: str  # mutabile
    _telefono: set  # immutabile
    _indirizzo: Indirizzo  # mutabile

    def __init__(self, nome: str, telefono: set, indirizzo: Indirizzo) -> None:
        self.set_nome(nome)
        self._telefono = telefono
        self.set_indirizzo(indirizzo)

    def __str__(self) -> str:
        return f"Nome: {self._nome}\n" \
               f"Telefono: {self._telefono}\n" \
               f"Indirizzo: {self._indirizzo}\n"

    def set_nome(self, new_name: str):
        self._nome = new_name

    def get_nome(self):
        return self._nome

    def add_telefono(self, new_telefono: str):
        self._telefono.add(new_telefono)

    def remove_telefono(self, telefono: str):

        if telefono in self._telefono:

            self._telefono.remove(telefono)

        else:
            raise ValueError(f"Telefono {telefono} non trovato.")

    def get_telefono(self):
        return frozenset(self._telefono)

    def set_indirizzo(self, indirizzo: Indirizzo):
        self._indirizzo = indirizzo

    def get_indirizzo(self):
        return self._indirizzo