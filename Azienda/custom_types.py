from typing import Self, Any
from datetime import datetime
import re

class RealGEZ(float):

    def __new__(cls, x: float = float|int|str|bool|Self) -> Self:

        n: float = float.__new__(cls, x)

        if n >= 0:
            return n
        
        raise ValueError(f"Il valore {n} è negativo")
