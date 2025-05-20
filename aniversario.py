#calculando idade.
dataDeAniversario = int(input('Em que ano nasceu? '))
anoAtual = int(input('Ano atual? '))
idade = anoAtual - dataDeAniversario
print(f'Você está com {idade} anos.')
#calculando...
if idade >= 18:
    print('Você pode dirigir.')
else:
    print('Não pode dirigir!')