#empresa quer calcular o aumento de salario 20% com mais de 5 anos de empresa
#caso ele tenha menos de 5 anos ele recebe so 10% de bonus...
salario = float(input('Qual seu salário? '))
ano_admissao = int(input('Qual seu ano de admissão na empresa? '))
ano_atual = int(input('Em que ano estamos? '))
tempo = ano_atual - ano_admissao

if (tempo > 10):
    bonus = salario * 0.3
else:
    if (tempo > 5) :
        bonus = salario * 0.2
    else:
        bonus = salario * 0.1

print(f'Você tem {tempo} anos dentro desta empresa.')
print(f'Seu Salário é de {salario}.')
print(f'E sua bonificação é de {bonus}.')
print(f'Salário final {bonus + salario}.')