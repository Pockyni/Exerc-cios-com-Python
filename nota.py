#saber se a nota foi alcançada.
m1 = float(input('Digite a primeira nota'))
m2 = float(input('Digite a segunda nota'))
m3 = float(input('Digite a terceira nota'))
if m1 >= 7 and m2 >= 7 and m3 >= 7:
 print ('Você passou no semestre')
else:
 print ('Você não passou no semestre.')


#criterios atigindos..
x = int(input('Digite um valor qualquer inteiro'))
if x >= 1 and x <= 100 or x >= -100 and x <=  -1: 
 print ('O critério foi atingido. ')