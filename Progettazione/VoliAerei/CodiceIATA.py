import re

class CodiceIATA:

    def __init__(self, codice: str):

        check = re.fullmatch(r"[A-Z]{2,3}", codice)
        
        if check is None:
            raise ValueError("IATA code not valid, it has to be a 2 or 3 letter string.")
        
        self.codice = check.group(0)


    def __str__(self):
        return self.codice
    
    def __eq__(self, other):
        if isinstance(other, CodiceIATA):
            return self.codice == other.codice
        return False
    
    def __hash__(self):
        return hash(self.codice)