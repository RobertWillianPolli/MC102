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

''' 4) Faça um programa que leia dois valores inteiros nas variáveis x e y e troque o conteúdo das variáveis.
Por exemplo, supondo que x = 2 e y = 10 foram os valores lidos, o seup rograma deve fazer com que x= 10 e y= 2.'''

x = int(input('Determine o valor de x: '))
y = int(input('Determine o valor de y: '))

x_1 = x
y_1 = y

x = y_1
y = x_1

print("O novo valor de x é: ", x)
print("O novo valor de y é: ", y)

# --------------------------------------------------------
'''Refaça este problema usando apenas x e y como variáveis.'''

x = int(input('Determine o valor de x: '))
y = int(input('Determine o valor de y: '))

x, y = y, x

print("O novo valor de x é: ", x)
print("O novo valor de y é: ", y)