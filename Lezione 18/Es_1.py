# Safe Square Root: Write a function safe_sqrt(number) that calculates the square root of a number using math.sqrt(). 
# Handle ValueError if the input is negative by returning an informative message.

import math

def safe_sqrt (n: int) -> int:

    if n <= 0:

        raise ValueError ("Il numero non può essere negativo.")
    

    return print(math.sqrt(n))



safe_sqrt(-16)

