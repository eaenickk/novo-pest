
def saudacao(nome_da_pessoa= 'Joao', sexo= 'm'):
    if sexo == 'm':
        print(f'Seja bem vindo, {nome_da_pessoa}')
    elif sexo == 'f':
        print(f'Seja bem vinda, {nome_da_pessoa}')

saudacao()
saudacao('Kah', 'f')
saudacao('Maria')
saudacao('m')