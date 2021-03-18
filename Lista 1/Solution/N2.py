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
'''2. Considere o trecho de código abaixo:
a = 10
b = a
c = 9
d = c
c = c + 1

Após a execução desse trecho de código, qual será o valor armazenado em cada variável?
'''

'''R: Após a execução deste trecho de código, o valor das variáveis serão:
a = 10 -> Não altera seu valor;
b = 10 -> "b" receberá o valor de "a";
c = 10 -> "c" é incrementado em uma unidade o seu valor inicial;
d =  9 -> "d" recebe o valor inicial de "c"; 
'''