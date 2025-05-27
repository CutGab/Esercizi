from custom_types import RealGEZ


class Progetto():

    _nome: str #mutabile
    _budget: RealGEZ #mutabile

    def __init__(self, nome: str, budget: RealGEZ) -> None:

        self.set_nome(nome)
        self.set_budget(budget)


    def __str__(self) -> str:
        
        return f"Nome: {self._nome}\n\
                Budget: {self._budget}\n"

    def set_nome(self, new_name: str):
        self._nome = new_name         
    
    def get_nome(self):
        return self._nome
    
    def set_budget(self, new_budget: RealGEZ):
        self._budget = new_budget

    def get_budget(self):
        return self._budget