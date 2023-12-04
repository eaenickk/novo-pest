#PROVA PROGRAMAÇÃO ESTRUTURADA
#DUAS QUESTÕES

#PRIMEIRA QUESTÃO (1)
'''numero = int(input('Digite um numero de 3 dígitos: '))
digito_1 = numero // 10
digito_1 = digito_1 * 0.1
digito_1 = int(digito_1)

digito_3 = numero % 10

if digito_1 == digito_3:
    print('É um palindromo')
else:
    print('Não é um Palindromo')

'''



#SEGUNDA QUESTÃO (4)
numero = int(input('Digite um numero: '))
numero_contrario = 0

while numero != 0:
    digito = numero % 10
    numero_contrario = numero_contrario * 10 + digito
    numero = (numero - digito) / 10

print(numero_contrario)
print(int(numero_contrario))