'''#Primeiro Exercicio
r = 5

volume = (4 / 3) * (3.14) * (r**3)

print(f"O volume de uma esfera de raio {r} é {volume}")

#Segundo Exercicio
livro = 24,95


#Terceiro Exercicio

hora = 14

alarme = (hora + 51) % 24

print(alarme)

#Quarto Exercicio

hora = int(input("Entre com o horário atual: "))
alarme = int(input("Qual número de horas que o alarme deverá esperar antes de tocar: "))

nova_hora = (hora + alarme) % 24

print(f"Agora são {hora} horas e daqui a {alarme} horas o alarme vai tocar em {nova_hora} horas!")

#Quinto Exercicio

num = int(input("Digite um número: "))

num_a = num
num_b = num * 11
num_c = num * 111

print(num_a, num_b, num_c)

#Sexto Exercicio

base = float(input("Digite o valor da base: "))
altura = float(input("Digite o valor da altura: "))

area_do_triangulo = (base * altura) / 2

print(f"A área do triângulo com base {base} e altura {altura} é {area_do_triangulo}.")


#Setimo Exercicio

x = int(input("Qual valor de x? "))
y = int(input("Qual o valor de y? "))

problema = (x+y) * (x+y)

print(problema)
'''
#Oitavo Exercicio

import math

x1 = float(input("x1 ="))
y1 = float(input("y1 ="))
x2 = float(input("x2 ="))
y2 = float(input("y2 ="))

d = math.sqrt((x2 - x1)** 2 + (y1 - y2)**2)

print(d)