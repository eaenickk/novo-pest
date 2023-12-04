def primeira_questao():
    def calculadora(num1, num2, operacao):
        if operacao == "soma":
            return num1 + num2
        elif operacao == 'subtracao':
            return num1 - num2
        elif operacao == 'multiplicacao':
            return num1 * num2
        elif operacao == 'divisao':
            if num2 == 0:
                return ('Não é possivel dividir por 0')
            return num1 / num2
        else:
            return ("Operação Invalida.")
        
    resultado = calculadora(2, 2, 'subtracao')
    print(type(resultado))
    print(resultado)

def segunda_questao():
    def cumprimentar(nome, saudacao = 'olá'):
        print(f'{saudacao}, {nome}!')

    cumprimentar('joao')
    cumprimentar('jonas', 'Salve')

def terceira_questao():
    def converter_moeda(valor_em_reais, para_dolar= True):
        taxa_de_conversao = 5.0

        if para_dolar:
            return valor_em_reais / taxa_de_conversao
        else:
            return valor_em_reais
        

    valor_em_reais = converter_moeda(100)
    print(valor_em_reais)

def menu():
    print('|----------------------------------|')
    print('| Digite qual questão vc quer ver? |')
    print('| 1 - Primeira Questão             |')
    print('| 2 - Segunda Questão              |')
    print('| 3 - Terceira Questão             |')
    print('|----------------------------------|')



while True:
    menu()
    perg = int(input('--- '))

    if perg == 1:
        primeira_questao()
    elif perg == 2:
        segunda_questao()
    elif perg == 3:
        terceira_questao()
    else:
        print('Tente Novamente...')

