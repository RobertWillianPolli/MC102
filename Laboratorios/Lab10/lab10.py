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
alcance = int(input()) + 1

bau_encontrado = 0
positions = []

for i in range(num_sensores):
    linha, coluna = [int(i) for i in (input().split(" "))]

    for passo in range(alcance):
        # Check East and actual position
        if (passo+coluna) < 8:
            if (campo[linha][coluna+passo] == "x") and not([linha, coluna+passo] in positions):
                bau_encontrado += 1
                positions.append([linha, coluna+passo])

            elif campo[linha][coluna+passo] == "o":
                break

    for passo in range(1, alcance):
        # Check West
        if (coluna-passo) >= 0:
            if (campo[linha][coluna - passo] == "x") and not([linha,coluna - passo] in positions):
                bau_encontrado += 1
                positions.append([linha,coluna - passo])

            elif campo[linha][coluna - passo] == "o":
                break

    for passo in range(1, alcance):
        # Check North
        if (linha-passo) >= 0:
            if (campo[linha-passo][coluna] == "x") and not([linha-passo, coluna] in positions):
                bau_encontrado += 1
                positions.append([linha-passo,coluna])

            elif campo[linha-passo][coluna] == "o":
                break

    for passo in range(1, alcance):
        # Check South
        if (linha+passo) < 8:
            if (campo[linha + passo][coluna] == "x") and not([linha + passo, coluna] in positions):
                bau_encontrado += 1
                positions.append([linha + passo, coluna])

            elif campo[linha + passo][coluna] == "o":
                break

# Impressão da saída
if (bau_encontrado > 0):
    print(f"{bau_encontrado} bau(s) encontrado(s).")

else:
    print("Nenhum bau encontrado.")