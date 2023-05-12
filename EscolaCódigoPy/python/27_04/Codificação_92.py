salario = [0, 0, 0, 0,]
soma = 0
i = 0

while i < 4:
    salario[i] = float(input())
    soma += salario[i]
    i += 1
media = soma / 4
print(f"Média = R$ {media:.2f}")

i = 0

while i< 4:
    if salario[i] < media:
        print(f"Abaixo da média: R$ {salario[i]:.2f}")
    i += 1
    
