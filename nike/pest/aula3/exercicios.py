'''def eh_primo(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    

#Segunda questão = Defina uma função chamada contagem_regressiva que aceita um número inteiro positivo como parâmetro e imprime uma contagem regressiva a partir desse número até zero.

def contagem_regressiva(num):
    if num < 0:
        print('O numero deve ser positivo')
    else:
        for i in range(num, -1, -1):
            print(i)

contagem_regressiva(10)

#Terceira Questão = Escreva uma função chamada calcular_media que aceite três argumentos (notas) e retorne a média dessas notas. Certifique-se de que a variável utilizada para armazenar a soma das notas seja local à função.
def calcular_media(nota1, nota2, nota3):
    soma = nota1 + nota2 + nota3
    media = soma/3
    return media

nota1 = 7.0
nota2 = 6.5
nota3 = 6.0

media = calcular_media(nota1, nota2, nota3)
print(f'A média das notas é {media}')

#Quarta Questão = Crie uma variável local chamada contador e defina-a como 0. Em seguida, escreva uma função chamada incrementar_contador que não aceite nenhum argumento, mas incrementa o valor de contador em 1 cada vez que a função é chamada.
contador = 0
def incrementar_contador():
    global contador
    contador +=1

incrementar_contador()
print(contador)
incrementar_contador()
print(contador)
incrementar_contador()
print(contador)
'''
#Quinta Questão = Escreva uma função chamada potencia que aceite dois argumentos base e expoente, e retorne a potência de base elevada a expoente. Use uma função aninhada (função dentro de função) de potencia para calcular a potência.


