#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
num = int(input('Informe um numero: '))
u = num // 1 % 10
d = num // 10
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))



