credito = float(input('Seu crédito: R$ '))
while credito > 0:
    item = float(input('Preço do item: R$ '))
    if item > credito:
        print('Compra negada! Ultrapassa seu crédito.')
        break
    credito -= item                             ##else desnecessario
print(f'Crédito restante: R$ {credito:.2f}')
