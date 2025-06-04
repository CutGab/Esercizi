numbers = [64, 34, 25, 12]
print(f"Lista Originale: {numbers}")

for i in range(len(numbers)):
     for j in range(0, len(numbers)-i-1):
            
            temp = numbers[j]

            if numbers[j] > numbers[j+1]:
                numbers[j] = numbers[j+1]
                numbers[j+1] = temp


print(f"Lista Ordinata: {numbers}")