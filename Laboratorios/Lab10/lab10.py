###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 10 - Caça ao Tesouro
# Nome: ROBERT WILLIAN POLLI    DATA: 26/05/21
# RA: 187848
###################################################

# Leitura da matriz

campo = []
for i in range(8):
    campo.append(input().split(" "))

# Leitura e processamento dos sensores
num_sensores = int(input())
alcance = int(input())

bau_encontrado = 0

for i in range(num_sensores):
    coluna, linha = [int(i) for i in (input().split(" "))]

    coluna -= 1
    linha  -= 1

    for passo in range(alcance+1):
        # Check Leste and actual position
        if (passo+coluna) < 8:
            if campo[linha][coluna+passo] == "x":
                bau_encontrado += 1

            elif campo[linha][coluna+passo] == "o":
                break

    for passo in range(1, alcance+1):
        # Check Oeste
        if (passo-coluna) >= 0:
            if campo[linha][coluna - passo] == "x":
                bau_encontrado += 1

            elif campo[linha][coluna - passo] == "o":
                break

    for passo in range(1, alcance+1):
        # Check Norte
        if (passo+linha) < 8:
            if campo[linha+passo][coluna] == "x":
                bau_encontrado += 1

            elif campo[linha+passo][coluna] == "o":
                break

    for passo in range(1, alcance+1):
        # Check Sul
        if (passo-coluna) >= 0:
            if campo[linha][coluna - passo] == "x":
                bau_encontrado += 1

            elif campo[linha][coluna - passo] == "o":
                break

# Impressão da saída
if (bau_encontrado > 0):
    print(f"{bau_encontrado} bau(s) encontrado(s).")

else:
    print("Nenhum bau encontrado.")