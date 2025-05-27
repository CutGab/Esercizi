import time

total = 0
summation = 0
n = int(input("Inserisci un numero: "))

time_sec = time.time() 

start = time.time()
total = ([i**2 for i in range(1, n+1)])
end = time.time()

#print(f"La somma equivale a: {total}")

start_2 = time.time()
for i in range(1, n + 1):
    
    summation += i**2
end_2 = time.time()

print("Tempo in secondi dall'inizio della list c.:", end -start) 
print("Tempo in secondi dall'inizio del for:", end_2 - start_2) 