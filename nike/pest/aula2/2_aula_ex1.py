def primeira_questao():
    def receber_dois_num(num1, num2):
        if num1 > num2:
            maior = num1
        elif num1 == num2:
            print('São Iguais')
            
        else:
            maior = num2
        return maior

    numero_1 = float(input('Digite um numero: '))
    numero_2 = float(input('Digite um numero: '))

    maior = receber_dois_num(numero_1, numero_2)
    print(maior)


primeira_questao()