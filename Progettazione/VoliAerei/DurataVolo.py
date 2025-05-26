import re

class DurataVolo:
    durata: str

    def __init__(self, durata: str):

        pattern = re.fullmatch(r"\d+:(?:[01]\d|2[0-3]):[0-5]\d", durata)

        if pattern is None:
            raise ValueError("Date format not valid. Use the following format D:HH:MM")
        
        self.durata = pattern.group(0)

    def __str__(self):
        return self.durata