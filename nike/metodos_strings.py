#Métodos de Strings

# upper() e lower()
test = 'isso é um exemplo'
print(test.upper())
print(test.lower())


# split()

texto = 'asdasdsaf'
lista = texto.split()
print(lista)


# join()

''.join(lista)

# capitalize()
frase = 'frase Show'.capitalize()
print(frase)
#Outra Alternativa
slice1 = frase[0].upper()
slice2 = frase[1::].lower()
nova = slice1 + slice2
print(nova)

#Replace()
frase = input('Digite uma frase: ')

nova_frase = frase.replace('a', 'e')
print(nova_frase)

#find() e index()

string = 'isso é uma string!'
print(string.find('y'))
print(string.index('!'))


# count()

string = 'isso é uma string!'
contagem = string.count('m')
print(contagem)