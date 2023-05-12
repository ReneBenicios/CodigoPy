
x = int(input())
qtd_divisores = 0
candidato = 1

while candidato <= x:
    if x % candidato == 0:
        qtd_divisores += 1
    candidato += 1

if qtd_divisores == 2:
    print(f"{x} eh primo")
else:
    print(f"{x} nao eh primo")
