def somatoria(n):
    soma = 0                    #Variavel acumuladora#
    qtd = 0                     #Variavel Contadora
    x = 1
    while qtd < n:
        soma += x
        qtd += 1
        x += 1
    return soma

while True:
    n = int(input())
    if 0 <= n <= 100: break

print(f"a soma é {somatoria(n)}")
