#Criação do vetor.
X = 10 * [0]

#Preenchimento do vetor
for i in range(10):
    X[i] = int(input())

#Alteração de itens do vetor
for i in range(10):
    if X[i] <= 0:
        X[i] = 1

#Exibição do itens do vetor
for i in range(10):
    print(f"X[{i}] = {X[i]}")
