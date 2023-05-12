soma = 0

salario0 = float(input)
soma += salario0

salario1 = float(input)
soma += salario1

salario2 = float(input)
soma += salario2

salario3 = float(input)
soma += salario3

media = soma / 4
print(f"Média = R$ {média:.2f}")

if salario0 < media:
    print(f"Abaixo da média: R$ {salario0:.2f}")
if salario1 < media:
    print(f"Abaixo da média: R$ {salario1:.2f}")
if salario2 < media:
    print(f"Abaixo da média: R$ {salario2:.2f}")
if salario3 < media:
    print(f"Abaixo da média: R$ {salario3:.2f}")
