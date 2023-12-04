#Trabalho de Nicolas Emanuel Oliveira de Castro

lista_de_tarefas = []
lista_de_tarefas_pendentes = []
lista_de_tarefas_execução = []
lista_de_tarefas_concluidas = []


def menu():
    print('LISTA DE TAREFAS')
    print('[0] - SAIR')
    print('[1] - Cadastrar tarefa')
    print('[2] - Editar tarefa')
    print('[3] - Iniciar tarefa')
    print('[4] - Concluir tarefa')
    print('[5] - Listar todas as tarefas')
    print('[6] - Listar tarefas pendentes')
    print('[7] - Listar tarefas em execução')
    print('[8] - Listar tarefas concluídas')



def add_tarefa(tarefa):
    nova_tarefa = [tarefa, 'to-do']
    lista_de_tarefas.append(nova_tarefa)
    lista_de_tarefas_pendentes.append(nova_tarefa)
    print(f'{tarefa} adicionada em Lista de Tarefas: {lista_de_tarefas}')
    print('')


def edit_tarefa(nome_da_tarefa):
    for tarefa in lista_de_tarefas:
        if nome_da_tarefa in lista_de_tarefas:
            pass
            

            

def concluir_tarefa(nome_da_tarefa, status = 'doing'):
    for tarefa in lista_de_tarefas_execução:
        for i in tarefa:
            if nome_da_tarefa == i and status == 'doing':
                nova_tarefa = [nome_da_tarefa, 'done']

                lista_de_tarefas.remove(tarefa)
                lista_de_tarefas_execução.remove(tarefa)

                lista_de_tarefas_concluidas.append(nova_tarefa)
                return nova_tarefa


def iniciar_tarefa(nome_da_tarefa, status = 'doing'):
    for tarefa in lista_de_tarefas:
        for i in tarefa:
            if nome_da_tarefa == i and status == 'to-do':
                nova_tarefa = [nome_da_tarefa, 'doing']

                lista_de_tarefas.remove(tarefa)
                lista_de_tarefas_pendentes.remove(tarefa)

                lista_de_tarefas.append(nova_tarefa)
                lista_de_tarefas_execução.append(nova_tarefa)
                return nova_tarefa

        
while True:
    menu()
    print('')
    op = int(input('Digite a opção que deseja: '))
    if op == 0:
        break
    elif op == 1:
        nome_da_tarefa = input('Qual o nome da Tarefa: ')
        add_tarefa(nome_da_tarefa)

    elif op == 2:
        tarefa_editada = input('Qual tarefa vc quer editar: ')
        edit_tarefa(tarefa_editada)

    elif op == 3:
        nome_da_tarefa_iniciar = input('Digite o nome da tarefa para iniciar :')
        status = input('Qual o status: ')
        iniciar_tarefa(nome_da_tarefa_iniciar, status)

    elif op == 4:
        nome_da_tarefa_concluida = input('Digite o nome da tarefa para concluir :')
        status = input('Qual o status: ')
        concluir_tarefa(nome_da_tarefa_concluida, status)

    elif op == 5:
        print(lista_de_tarefas)

    elif op == 6:
        print(lista_de_tarefas_pendentes)

    elif op == 7:
        print(lista_de_tarefas_execução)

    elif op == 8:
        print(lista_de_tarefas_concluidas)
    