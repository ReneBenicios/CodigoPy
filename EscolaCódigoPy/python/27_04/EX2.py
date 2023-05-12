#Crie um programa que receba como entrada um numero
#natural N e peça N salarios para o usuario.
#O programa deverá exibir a média salarial e apenas os
#Salarios abaixo da média.

salarios = []
soma = 0

for _ in range(4):
    salario = float(input())
    soma += salario
    salarios.append(salario)

media = soma / 4
print(f"Média = r$ {media:.2f}")

for salario in salarios:
    if salario < media:
        print(f"Abaixo da média:R$ {salario:.2f}")
