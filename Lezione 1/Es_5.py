n = int (input("Insert a number: "))
prime = True

for i in range(2,n):
    if n%i==0:
        prime=False
if prime:
    print ("Prime number.")
else:
    print("Not a prime number.")

