print ('Boas Vindas na Loja da Nicole ')
produto = float(input('Insiria o valor do produto:'))
qnt = int(input('Digite a quantidade do produto:'))

#culculo das quantidade e a compra inteira sera atribuida as condicionais
valor_total = produto * qnt

#calcular valor de porcentagem
#Sem desconto...
if valor_total <= 2500 :
    print('Você não tem direito a desconto neste produto. ')

#desconto de 4%
elif valor_total <= 6000: 
    desconto =  0.04
    valor_desconto = valor_total * desconto
    valor_final = valor_total - valor_desconto
    print (f'O valor total e de: {valor_total:.2f}') #.2f serve pra alinhar e deixar bonito o número...
    print(f'Você ganhou 4% de desconto ! O valor ficou: {valor_desconto:.2f}')

 #desconto de 7%   
elif valor_total <= 10000:
 desconto = 0.07
 valor_desconto = valor_total *desconto
 valor_final = valor_total - valor_desconto
 print (f'O valor total e de: {valor_total:.2f}')
 print (f'Você ganhou 7% de desconto ! O valor ficou: {valor_desconto:.2f}')

 #desconto de 11% 
else:
 valor_total >= 10000
 desconto = 0.11
 valor_desconto = valor_total *desconto
 valor_final = valor_total - valor_desconto
 print (f'O valor total e de: {valor_total:.2f}')
 print (f'Você ganhou 11% de desconto ! O valor ficou: {valor_desconto:.2f}')