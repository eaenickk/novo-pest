lista = ['casa', 'rato', 'luz']
dicionario = {
    'casa' : 'house',
    'rato' : 'mouse',
    'luz' : 'light',
}

for item in lista:
    print(dicionario[item])

#Alterando elementos

dicionario['casa'] = 'home'
print(dicionario['casa'])
dict= {
    'um': 'one',
    1: 'um',
    '1': 1,
    'um' : 1,
    1 : 1
}

#Percorrendo
for chave, valor in dict.items():
    print(f'{chave} : {valor}')

#Adicionar Elementos
dict['chave'] = 'valor qualquer'                                        
print(dict)

#Remover elementos
del dict['chave']
print(dict)
