from typing import Self, Any

class RealGEZ(float):
	# Tipo di dato specializzato Reale >= 0
	def __new__(cls, v: float|int|str|bool|Self) -> Self:
		n: float = float.__new__(cls, v) # prova a convertire v in un float

		if n >= 0:
			return n

		raise ValueError(f"Il valore {n} è negativo!")