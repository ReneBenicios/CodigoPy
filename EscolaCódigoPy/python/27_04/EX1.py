#Crie um programa que receba como entrada um numero
#natural N e peça N salarios para o usuario.
#O programa deverá exibir a média salarial e apenas os
#Salarios abaixo da média.

qtd_salario = int(input())

salario = qtd_salario *[0] ##[0,0,0,....]
soma = 0
i = 0

while i < qtd_salario:
    salario[i] = float(input())
    soma += salario[i]
    i += 1

media = soma / qtd_salario
print(f"Média Salarial : R${media:.2f}")

i = 0

while i < qtd_salario:
    if salario[i] < media:
        print(f"Abaixo da média: R$ {salario[i]:.2f} ")
    i += 1
