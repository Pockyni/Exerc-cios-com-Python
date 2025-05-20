print('Escolha a fruta que deseja comprar')
print('1 - Maçã')
print('2 - Banana')
print('3 - Laranja')
produto = int(input('Escolha a fruta: '))
qnt = int(input('Insira a quantidade: '))

if produto == 1:
    pagar = qnt * 2.3
    print(f'Você comprou {qnt} de maçãs. Total a pagar é: {pagar}')
elif produto == 2:
    pagar = qnt * 5.0
    print(f'Você comprou {qnt} de bananas. Total a pagar é: {pagar}')
elif produto == 3:
    pagar = qnt * 3.5  # Preço da laranja (você pode ajustar)
    print(f'Você comprou {qnt} de laranjas. Total a pagar é: {pagar}')
else:
    print('Opção de fruta inválida.')