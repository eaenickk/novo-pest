num = int(input("Digite um número inteiro: "))
fat = 1

while num >= 0:
    if num == 0:
        print(f'Fatorial: {fat}')
        break
    else:
        fat *= num
        num -= 1
else:
    print("Número Inválido")