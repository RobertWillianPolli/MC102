# -*- coding: utf-8 -*-

# Script para testar tarefas de laboratório de MC102 em ambiente GNU/Linux.

# Uso: python3 testador.py

# O programa lab<x>.py será testado com todos os arquivos arq<i>.in
# encontrados no diretório corrente. Os testes serão iniciados com i
# igual a 01 e serão interrompidos quando arq<i>.in não for encontrado.

# As saídas serão comparadas com os arquivos arquivos arq<i>.out. 

# Durante o processamento serão criados e posteriormente removidos
# arquivos arq<i>.res e arq<i>.diff. 

import os
import sys
import re

# Imprime as saídas do programa e do gabarito
output = True

path = os.path.dirname(os.path.abspath("__file__"))
os.chdir(path)

r = re.compile(r'lab\d\d.py')
for file in os.listdir():
    if r.match(file):
        labfile = file
        break

else:
    print("Código do laboratório não encontrado.")
    exit(0)

i = 1
pasta = int(labfile.split('.')[0][-2:])
testfile = "./aux{:02d}/open/arq{:02d}.in".format(pasta, i)

while (os.path.exists(testfile)):
    resfile = "./aux{:02d}/open/arq{:02d}.out".format(pasta, i)
    if not os.path.exists(resfile):
        print("Arquivo", resfile, "não encontrado.")
        sys.exit()

    outfile = "./aux{:02d}/open/arq{:02d}.res".format(pasta, i)

    if (os.path.exists(outfile)):
        answer = input("Arquivo " + outfile + " existente. Pode ser sobrescrito (S/n)?")
        if answer == "n" or answer == "N":
            sys.exit()

    difffile = "./aux{:02d}/open/arq{:02d}.diff".format(pasta, i)
    if (os.path.exists(difffile)):
        answer = input("Arquivo " + difffile + " existente. Pode ser sobrescrito (S/n)?")
        if answer == "n" or answer == "N":
            sys.exit()

    os.system("python3 " + labfile + " < " + testfile + " > " + outfile)
    if os.system("diff " + outfile + " " + resfile + " > " + difffile) == 0:
        print("Teste ", "{:02d}".format(i), ": resultado correto")
    else:
        print("Teste ", "{:02d}".format(i), ": resultado incorreto")
        if output:
            # os.system("cat " + difffile)
            print(">>> Sua resposta:")
            os.system("cat " + outfile)
            print(">>> Resposta correta:")
            os.system("cat " + resfile)

    os.remove(outfile)
    os.remove(difffile)
    i = i + 1
    testfile = "./aux{:02d}/open/arq{:02d}.in".format(pasta, i)