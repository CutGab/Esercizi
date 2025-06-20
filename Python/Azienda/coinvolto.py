from progetto import Progetto
from impiegato import Impiegato
from datetime import date
from typing import Any

Impiegati_Coinvolti: dict[str, list[dict]] = {}
 
class _coinvolto:
    
    _impiegato: Impiegato #immutabile
    _progetto: Progetto #immutabile
    _data_afferenza: date #immutabili

    def __init__(self, impiegato: Impiegato, progetto: Progetto, data_afferenza: date) -> None:
        self._impiegato = impiegato
        self._progetto = progetto
        self._data_afferenza = date.today()
        
    def coinvolto_add(impiegato: Impiegato, progetto: Progetto, data_afferenza: date):
        
        if progetto not in Impiegati_Coinvolti:
            Impiegati_Coinvolti[progetto] = []
            
            for i in Impiegati_Coinvolti[progetto]:
                if i["impiegato"] == impiegato:
                    print("L'impiegato è già coinvolto in questo progetto.")
                    
        coinvolto = {
            "impiegato": impiegato,
            "data_afferenza": data_afferenza
            }
        
        Impiegati_Coinvolti[progetto].append(coinvolto)
        
        print(f"Impiegato {impiegato} aggiunto al progetto {progetto} con data {data_afferenza}.")


    def __hash__(self) -> int:
        return hash((self._impiegato, self._progetto))
    
    def __eq__(self, other: Any) -> bool:
        if type(self) != type(other) or hash(self) != hash(other):
            return False

        return self._impiegato() is other.impiegato() \
            and self._progetto() is other.progetto()\
            and self._data_afferenza() is other.data_afferenza

    def __repr__(self) -> str:
        return f"{self._impiegato()} prende {self._progetto()} a {self._data_afferenza()}"