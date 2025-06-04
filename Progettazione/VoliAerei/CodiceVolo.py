import re

class CodiceVolo:

    def __init__(self, codice: str):

        match = re.fullmatch(r"[A-Z]{2} \d{1,4}", codice)

        if match is None:
            raise ValueError("Flight code not valid. It has to be in the following: 2 letters followed by 1-4 numbers.")
        
        self.codice = match.group(0)

    def __str__(self):
        return self.codice
    
    def __hash__(self):
        return hash(self.codice)