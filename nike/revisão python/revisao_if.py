'''#1 Escreva um código em Python que utilize a estrutura de controle ‘if-elif-else' para verificar se um número inteiro dado é par ou ímpar. Se o número for par, armazene-o em uma variável chamada 'pares' e se for ímpar, armazene-o em uma variável chamada 'impares'. Utilize uma única linha de código dentro do bloco 'if' e outra dentro do bloco 'else’. OBS: considere zero como neutro (nem par, nem ímpar).

numero = int(input('Digite um inteiro: '))

if (numero%2) == 0:
    print("Par")

elif (numero%2) == 1:
    print("Impar")

else:
    print("Neutro")


#2 Escreva um código para classificar uma nota de 0 a 10 dada. Se a nota for maior ou igual a 9, imprima "A", se a nota for maior ou igual a 7 e menor que 9 imprima "B", se a nota for maior ou igual a 5 e menor que 7 imprima "C" e se a nota for menor que 5 imprima "D". Utilize uma única linha de código dentro de cada bloco 'if', 'elif' e 'else'.

nota = float(input('Digite sua nota: '))

if nota >= 9:
    print('A')
elif nota >= 7:
    print('B')
elif nota >= 5 and nota < 7:
    print('C')
else:
    print('D')

#3 Crie um programa para determinar se um número inteiro dado é maior que 10 e menor que 20, ou se é maior que 30 ou menor que 5. Utilize uma única linha de código dentro de cada bloco 'if' e 'else' para imprimir "maior que 10 e menor que 20", "maior que 30 ou menor que 5" ou "não é maior que 10 e menor que 20 e não é maior que 30 ou menor que 5" respectivamente.

num = int(input(' Digite um número inteiro: '))

if num > 10 and num < 20:
    print('maior que 10 e menor que 20')
elif num > 30 or num < 5:
    print('maior que 30 ou menor que 5')

else:
    print('não é maior que 10 e menor que 20 e não é maior que 30 ou menor que 5')

#4 Escreva um programa em Python para somar três números inteiros do usuário. No entanto, se dois valores forem iguais, a soma será zero.

num_1 = int(input('num1: '))
num_2 = int(input('num2: '))
num_3 = int(input('num3: '))

soma = num_1 + num_2 + num_3

if num_1 == num_2:
    print('Os valores num_1 e num_2 são iguais, a soma será zero')
elif num_1 == num_3:
    print('Os valores num_1 e num_3 são iguais, a soma será zero')
elif num_2 == num_1:
    print('Os valores num_2 == num_1 são iguais, a soma será zero')
elif num_2 == num_3:
    print('Os valores num_2 == num_3 são iguais, a soma será zero')
elif num_3 == num_1:
    print('Os valores num_3 == num_1 são iguais, a soma será zero')
elif num_3 == num_2:
    print('Os valores num_1 == num_3 são iguais, a soma será zero')
else:
    print(soma)
'''
#5 Crie um programa para determinar se um número inteiro dado é divisível por 2, 3 ou nenhum deles. Utilize uma única linha de código dentro de cada bloco 'if', 'elif' e 'else' para imprimir "divisível por 2", "divisível por 3" ou "não é divisível por 2 ou 3" respectivamente."

num_inteiro = int(input('Digite um número inteiro: '))

if num_inteiro % 2 == 0 and num_inteiro % 3 == 0:
    print('É divisivel por 2 e 3')

elif num_inteiro % 3 == 0:
    print('É divisivel por 3')

elif num_inteiro % 2 == 0:
    print('É divisivel por 2')
    
else:
    print('Não é Divisivel por 2 e 3')