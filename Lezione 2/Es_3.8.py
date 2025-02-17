places: list =  []

for i in range (5):
    p: str = input("Insert a place you'd like to visit: ")
    places.append(p)

#Raw list print
print(places)

#List print in alphabetical order
print(sorted(places))

#Print to show the list is still in its original order
print(places)

#Print in reverse alphabetical order
print(sorted(places, reverse = True))

#Print to show the list is stil in its original order
print(places)

#Reverse function to change the order of the list
places.reverse()

#Print to show the list order has changed
print(places)

#Reverse function to show it's back to its original order
places.reverse()

#Print to show its back to its original order
print(places)

#Sort function to change it into an alphabetic order
places.sort()

#List print in alphabetical order
print(places)

#Sort function to change its order into reverse alphabetical order
places.sort(reverse = True)

#List print in reverse alphabetical order
print(places)