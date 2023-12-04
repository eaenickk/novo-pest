numeros = []

for i in range(10):
    num = int(input('Digite um número: '))
    numeros.append(num)

print(numeros)

numeros_pares = numeros[:]


for num in numeros_pares:
    if num % 2 == 0:
        numeros.remove(num)
    

print(numeros)



    