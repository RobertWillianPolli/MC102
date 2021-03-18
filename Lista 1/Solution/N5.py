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

''' 5) Faça um programa que leia os valores correspondentes aos três lados "a","b" e "c" de um triângulo.
 O programa então deve determinar se o triângulo é isósceles, escaleno ou equilátero,informando isto para o usuário,
 e em seguida o programa deve imprimir a área 'A' do triângulo utilizando a fórmula de Heron:

 A=√[s(s−a)(s−b)(s−c)]
 onde: s=(a+b+c)/2.
 '''

a = int(input('Determine o valor do lado "a" do triângulo: '))
b = int(input('Determine o valor do lado "b" do triângulo: '))
c = int(input('Determine o valor do lado "c" do triângulo: '))

# 1) Checando o tipo de triângulo:

if a == b == c:
    type_Triangulo = "Equilátero"

elif a == b or b == c or a == c:
    type_Triangulo = "Isósceles"

else:
    type_Triangulo = "Escaleno"

print("O triângulo informado é ", type_Triangulo)

# 2) Determinando a área do triângulo:

s = (a + b + c)/2

value_square = s*(s-a)*(s-b)*(s-c)

if value_square >= 0:
    area_triangulo = value_square ** (1/2)

    print("A área do triângulo vale", area_triangulo, "unidades", sep = " ")

else:
    print("Valores inválidos")