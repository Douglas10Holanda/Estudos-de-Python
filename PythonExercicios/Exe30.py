# Exercicio 30 de Python - Par ou Ímpar?

# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

n = int(input('Digite um número: '))
r = n%2

if r == 0:
    print('O número {} é par!'.format(n))
else:
    print('O número {} é ímpar!'.format(n))