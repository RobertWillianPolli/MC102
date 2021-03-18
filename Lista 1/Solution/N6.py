#!/usr/bin/env python3
# ------------------------------------------------------
#       Universidade Estadual de Campinas - UNICAMP
#
#     MC102 - Algoritmos e Programação de Computadores
# ------------------------------------------------------
#               Aluno: Robert Willian Polli
#                       RA:187848
#                Data: 17 de março de 2021
#-------------------------------------------------------

#Lista: 01

'''6) Considere um programa que deve classificar um número como par ou ímpar e, além disso,
classificar ele como menor do que 100 ou maior ou igual a 100.
A solução abaixo faz essa classificação de maneira correta?'''

'''
print("Digite um número:")
a = int(input())
if a % 2 == 0 and a < 100:
    print("O número é par e menor do que 100")
else:
    if a  >= 100:
        print("O número é par e maior ou igual que 100")
    
if a % 2 != 0 and a < 100:
    print("O número é ímpar e menor do que 100")
else:
    if a  >= 100:
        print("O número é ímpar e maior ou igual que 100")
'''

'''
R: O programa não faz de maneira correta, uma vez que não há filtragem sobre as condições "if" para
se determinar qual delas é falsa. 
'''