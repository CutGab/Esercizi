from typing import Self, Any
from datetime import datetime
import re

class RealGEZ(float):

    def __new__(cls, x: float = float|int|str|bool|Self) -> Self:

        n: float = float.__new__(cls, x)

        if n >= 0:
            return n
        
        raise ValueError(f"Il valore {n} è negativo")

class Indirizzo:
    def __init__(self, cap: str, civico: str, via: str) -> None:

        if not re.match(r"^\d{5}$", cap):

            raise ValueError(f"CAP non valido: {cap}")
        
        self.cap = cap
        self.civico = civico
        self.via = via

    def __str__(self) -> str:
        return f"{self.via}, {self.civico}, {self.cap}"