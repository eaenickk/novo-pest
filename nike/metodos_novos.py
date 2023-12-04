#1
reservas = []

reservas.append("Fulano")
reservas.append("Beltrano")
reservas.append("Xico")
reservas.append("Ze")
reservas.append("Maria")

print(reservas)

print('')
#2

#Modelo que eu fiz
'''estoque = [['camiseta', 5], ['calça', 3], ['sapato', 4]]
produto_vendido = 'calça'
quantidade_vendida = 1
def realizar_venda(produto, quantidade):
    for item in estoque:
        if item[0] == produto:
            if item[1] >= produto:
                item[1] -= quantidade
                print(f'{quantidade} unidades de {produto} vendidas com sucesso!')
            else:
                print(f'Não há quantidade suficiente de {produto} em estoque.')
                break
        else:
            print(f'{produto} não encontrado!')

#Modelo do Thomaz
estoque = [
    ["camiseta", 5],  
    ["calça", 3], 
    ["sapato", 4]
    ]

def vender_produto(nome):
#    global estoque
    for item in estoque:
        if item[0] == nome:
            if (item[1] - 1) <= 0:
                estoque.remove(item)
            else:
                item[1] -= 1


print(f"Antes: {estoque}")
vender_produto("calça")
vender_produto("calça")
print(f"Depois: {estoque}")
vender_produto("calça")
print(f"Final: {estoque}")

print('')
#3


#4
despesas = [['01_11_2023', 'supermercado', 1000.0], ['01_11_2023','restaurante', 50.0]]

nova_data = input('Digite a data: ')
nova_descricao = input('Digite uma nova descrição de uma nova despesa: ')
novo_valor = float(input('Digite o valor da despesa: '))

posicao = int(input('Digite a posição para inserir a nova despesa: '))

if posicao >= 0 and posicao <= len(despesas):
    nova_despesa = [nova_data, nova_descricao, novo_valor]
    despesas.insert(posicao, nova_despesa)
    print('Despesa Adicionada')
else:
    print('Posição Inválida')

print('Lista de despesas atualizadas: ')
for despesa in despesas:
    if len(despesa) == 3:
        print('Data: ', despesa[0], 'Descrição:', despesa[1], 'Valor: ', despesa[2])

'''
#8
lista_de_temperaturas = [25, 26, 32, 30, 29, 23, 31]

print(lista_de_temperaturas)
limpar_dados = lista_de_temperaturas.clear()
print(lista_de_temperaturas)


#9








# Crie um programa que permita ao usuário registrar
# informações de alunos incluindo nome, matrícula e
# notas em várias disciplinas. Use uma listra aninhada
# para representar os alunos, onde cada aluno é uma
# lista com três elementos: nome, matrícula e uma
# lista de notas. O programa deve permitir adicionar
# novos alunos.


def pegar_dados():
    aluno = []
    nome = input("Nome: ")
    matricula = int(input("Matrícula: "))
    qtd_de_notas = int(input("Quantas notas? "))
    notas = pegar_notas(qtd_de_notas)
    aluno.append(nome)
    aluno.append(matricula)
    aluno.append(notas)
    return aluno


def pegar_notas(qtd):
    notas = []
    for i in range(qtd):
        notas.append(float(input(f"Nota {i}: ")))
    return notas


def mostra_alunos(alunos):
    for item in alunos:
        print(item)
    
def atualizar_aluno():
    

def remover_aluno(matricula):
    for aluno in alunos:
        if matricula in aluno:
            alunos.remove(aluno)
            print(alunos)


add_aluno = True
alunos = []
while add_aluno:
    aluno = pegar_dados()
    alunos.append(aluno)
    perg = input('Quer remover algum aluno:')
    if perg == 's':
        matri = int(input('Qual matricula quer remover: '))
        remover_aluno(matri)
    else:
        temp = input("Digite S para sair: ")
        if temp in "sS":
            add_aluno = False

mostra_alunos(alunos)