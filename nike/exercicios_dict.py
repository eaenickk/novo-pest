'''
# Questão 1
dicionario = {
    "nome": "João da Silva",
    "idade": 30,    
    "cidade": "Maranguape"
}


#Questão 2



lista_de_compras = {}

while True:
    opçao = input('Digite 0 para sair... ')
    if opçao == '0':
        break
    else:

        k = input('Digite o nome do produto: ')
        v = int(input('Diga a quantidade: '))
        lista_de_compras[k] = v  

    print(lista_de_compras)


#Questão 3

aluno_notas = {}

while True:
    opçao = input('Digite 0 para sair... ')
    if opçao == '0':
        break
    else:

        k = input('Digite a disciplina: ')
        v = float(input('Diga a nota: '))
        aluno_notas[k] = v  

    print(aluno_notas)

'''
# Questão 4

dict = {
    'Nicolas': 18, 
    'Cruz': 18, 
    'Daniel': 20}

for chave, valor in dict.items():
    print(f'{chave} : {valor}')
