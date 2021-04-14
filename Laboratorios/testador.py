# -*- coding: utf-8 -*-

# Script para testar tarefas de laboratório de MC102 em ambiente GNU/Linux.

# Uso: python3 testador.py NUMERO_DO_LABORATORIO

# O programa lab<x>.py será testado com todos os arquivos arq<i>.in
# encontrados no diretório corrente. Os testes serão iniciados com i
# igual a 01 e serão interrompidos quando arq<i>.in não for encontrado.

# As saídas serão comparadas com os arquivos arquivos arq<i>.out. 

# Durante o processamento serão criados e posteriormente removidos
# arquivos arq<i>.res e arq<i>.diff. 

import os
import sys
import re
import argparse

# Imprime as saídas do programa e do gabarito
output = True

parser = argparse.ArgumentParser()
parser.add_argument("num_lab")
args = parser.parse_args()

path = os.path.dirname(os.path.abspath("__file__"))
print(f'{path}/Lab{int(args.num_lab):02d}')
os.chdir(f'{path}/Lab{int(args.num_lab):02d}')

if os.path.exists(f'./lab{int(args.num_lab):02d}.py'):
    labfile = f'lab{int(args.num_lab):02d}.py'

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