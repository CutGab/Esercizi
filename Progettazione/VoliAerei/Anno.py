import re
from re import Match

class Anno:

    def __init__(self, anno: str):

        pre_check: Match = re.fullmatch(r"^19\d\d$|2[0-1]\d\d$", anno)

        if pre_check is None:
            raise ValueError("Invalid foundation date")
        
        self.anno = pre_check.group(0)

    def __str__(self):
        return self.anno