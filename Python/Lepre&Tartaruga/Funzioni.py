import random
import time

def steps_tartaruga(tartaruga_pos: int):
    move1 = random.choice(range(1, 10))

    match move1:
        case _ if move1 <= 5:
            tartaruga_pos += 3
        case _ if 6 <= move1 <= 7:
            tartaruga_pos -= 6
        case _ if 8 <= move1 <= 10:
            tartaruga_pos += 1

    if tartaruga_pos < 0:
        tartaruga_pos = 1
    
    return tartaruga_pos

def steps_lepre(lepre_pos: int):
    move2 = random.choice(range(1, 10))

    match move2:
        case _ if move2 <= 2:
            lepre_pos += 0
        case _ if 3 <= move2 <= 4:
            lepre_pos += 9
        case _ if move2 == 5:
            lepre_pos -= 12
        case _ if 6 <= move2 <= 8:
            lepre_pos += 1
        case _ if 9 <= move2 <= 10:
            lepre_pos -= 2

    if lepre_pos < 0:
        lepre_pos = 1
    
    return lepre_pos

def gara():

    tartaruga_pos = 1
    lepre_pos = 1

    while tartaruga_pos < 70 and lepre_pos < 70:

        if tartaruga_pos >= 70 and lepre_pos >= 70:

            tartaruga_pos = 70

            lepre_pos = 70

            print("IT'S A TIE.")

            break
        
        time.sleep(1)
        
        print("#################################################################################")
        
        pista = ["_"] * 70
        
        lepre_pos = steps_lepre(lepre_pos)
        
        if lepre_pos >= 70:
            
            lepre_pos = 70
            
            print ("HARE WINS || YOUCH!!")
            
            break
        
        
        tartaruga_pos = steps_tartaruga(tartaruga_pos)
        
        if tartaruga_pos >= 70:
            
            tartaruga_pos = 70
            
            print ("TORTOISE WINS || YAY!!")
            
            break
        
        pista[tartaruga_pos - 1] = "T"
        pista[lepre_pos - 1] = "H"
        
        if tartaruga_pos == lepre_pos:
            pista[tartaruga_pos - 1] = "OUCH!!!"
            
        print(f"The hare is currently in position: {lepre_pos}")
        print(f"The tortoise is currently in position: {tartaruga_pos}")
        print(*pista)




