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
'''3) Faça um programa que leia um número ponto flutuante x e calcule o valor de:
f(x) =√x + (x/2) +x^x. (Dica:√x = x^1/2)'''

x = float(input('Determine o valor de x: '))

function_of_X = (x**0.5) + (x/2) + (x**x)

print(function_of_X)