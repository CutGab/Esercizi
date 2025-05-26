# Hai ricevuto una lista di numeri interi, contenente valori compresi tra 1 e n, dove n è la lunghezza della lista. 
# 
# Tuttavia, alcuni numeri potrebbero mancare: la lista può contenere duplicati, ma non tutti i numeri da 1 a n sono presenti.

# Il tuo compito è individuare i numeri mancanti.

# Scrivi una funzione che, data in input una lista, restituisca una nuova lista ordinata contenente tutti i numeri da 1 a n che non sono presenti nella lista originale.

# print(find_disappeared_numbers([4,3,2,7,8,2,3,1])) #[5,6]

# def find_disappeared_numbers(nums: list[int]) -> list[int]:

#     newlist = []

#     nums.sort()

#     for i in nums:

#         if nums.count(i) > 1:

#             nums.pop(i)

#         newlist.append(i)
    
#     for i in newlist:

#         if i > len(newlist):
#             break

#         if i + 1 not in newlist:

#             newlist.append(i + 1)

#     newlist

#     return newlist

# print(find_disappeared_numbers([4,3,2,7,8,2,3,1]))

for i in range(3):
    print(hash("ciao"))


def collatz(n: int):
        
        if n % 2 == 0:
            
            b = n/2
            
            return b
        
        else:
            
            b = 3 * n + 1
            
            return b
        

def collatz_1 (n: int):
     
    r = n
    while r != 1:
          
        r = collatz(r)

        
    

collatz_1(5)