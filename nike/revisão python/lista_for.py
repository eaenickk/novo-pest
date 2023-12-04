#1 Crie um código em Python que use um for loop para imprimir todos os números pares de 0 a 20.
for i in range(0, 21, 2):
    print(i)

print(20*('-'))

#2 Escreva um código em Python que utilize um laço for para imprimir os números de 1 a 15, mas pulando os números 5, 8 e 12.

for i in range(1, 15, 3):
    print(i)

print(20*('-'))

#3 Crie um programa em Python que imprima a soma dos números pares de 0 até um número inteiro dado pelo usuário. Utilize o comando for para percorrer os números e realizar a soma.

soma = 0
num = int(input('Digite um número: '))
for i in range(0, num + 1, 2):
    soma = (i+i)

print(soma)

#4 Crie um código em Python que use o comando for para percorrer de 0 até n números e calcule a média aritmética desses valores.

soma = 0
num = int(input('Digite um número: '))

for i in range(num):
    valor = float(input(f'Digite o {i+1}º valor:  '))
    soma += valor

media = soma / num

print(f'A media desses número é: {media}')

#5 Crie um programa para verificar se um número é primo ou não. Utilize o comando for.

