from DurataVolo import DurataVolo
from CodiceVolo import CodiceVolo

class Volo:
    def __init__(self, codice_volo: CodiceVolo, durata: DurataVolo):
        self.codice_volo = codice_volo
        self.durata = durata

    def get_codice_volo(self) -> CodiceVolo:
        return self.codice_volo

    def set_codice_volo(self, codice_volo: CodiceVolo):
        self.codice_volo = codice_volo

    def get_durata(self) -> DurataVolo:
        return self.durata

    def set_durata(self, durata: DurataVolo):
        self.durata = durata

    def __str__(self):
        return f"Codice Volo: {self.codice_volo}, Durata: {self.durata}"