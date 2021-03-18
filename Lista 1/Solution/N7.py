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

'''
7) Faça um programa que leia um caractere ‘F’ ou ‘C’, que indica se o próximo valor corresponde à temperatura em Fahrenheit ou Celsius.
Em seguida, o programa deve ler o valor da temperatura e então imprimir o valor correspondente à temperatura na outra unidadede medida.
Observação:(C= 5/9×(F−32)).
'''

Temp_Converter = input('Digite a escala de temperatura (C ou F): ')

if Temp_Converter != "C" and Temp_Converter != "F":
    print('Erro: Escala inválida')

else:
    Temp_Value = int(input('Digite a temperatura na escala o' + Temp_Converter + ': '))
    if Temp_Converter == "F":
        Temperature = 5/9 * (Temp_Value - 32)

    else:
        Temperature = (9/5) * Temp_Value + 32

    print('A temperatura convertida vale:', Temperature, sep = ' ', end = " o"+ ("C" if Temp_Converter == "F" else "F"))