numeros = [10, 5, 7, 8, 1]
print(numeros[3])

numeros[2] = 30
print(numeros[2])

print(len(numeros))

print("----------------")


for i in numeros:
        print(i," com o for")
        
print("-----------------")

i = 0
while i < len(numeros):
    print(numeros[i], " com o while")
    i += 1
    
print("-----------------")

for i in range(len(numeros)):
    print(i+1, " -> ", numeros[i], " com o length")

print("-----------------")