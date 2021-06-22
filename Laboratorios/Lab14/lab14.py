###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 14 - Caça-Números
# Nome: Robert Willian Polli    Data: 21/06/2021
# RA: 187848
###################################################

commands = ["A", "E", "O", "C", "P", "S", "T"]
padroes = {"A":range(10),
           "E":range(0, 10, 2),
           "O":range(1, 10, 2),
           "C":[4, 6, 8, 9],
           "P":[2, 3, 5, 7],
           "S":[1],
           "T":[3, 6, 9]
           }
"""
Esta função recebe como parâmetro uma matriz, uma posição inicial na
matriz determinada pelos parâmetros linha e coluna e um padrão que
deve ser buscado em todas as direções (norte, sul, leste, oeste,
nordeste, sudeste, noroeste e sudoeste) a partir da posição inicial.
Caso o padrão seja encontrado a partir da posição inicial a função
deve retornar o valor True. Caso contrário, a função de retornar o
valor False.
"""
def busca_padrao(linha_inicio, linha_fim, coluna_inicio, coluna_fim, passo_l = 1, passo_c = 1):
    status = []
    p = 0
    for i in range(linha_inicio, linha_fim, passo_l):
        for j in range(coluna_inicio, coluna_fim, passo_c):
            if int(matriz[i][j]) in padroes[pattern[p]]:
                status.append(1)
                p += 1

    if len(status) == len(pattern):
        return([True, [linha_inicio+1, coluna_inicio+1]])

    else:
        return([False, [None, None]])
# Leitura da matriz

matriz = []
pattern = ""
received = "Null"

while(True):
    received = input()
    if not(received[0] in commands):
        matriz.append(received.split(" "))
    else:
        pattern = received
        break

# Processamento da busca na matriz
m_linhas = len(matriz)
m_colunas = len(matriz[0])

found         = []
found_pattern = []

for linha in range(m_linhas):
    for coluna in range(m_colunas):
        # Horizontal - Leste

        if (coluna + len(pattern)) <= m_colunas:
            found = busca_padrao(linha, linha+1, coluna, coluna + len(pattern))
            if found[0]:
                found_pattern.append(found[1])
        # Horizontal - Oeste
        if (coluna - len(pattern)) >= 0:
            found_pattern = busca_padrao(linha, linha+1, coluna, coluna - len(pattern), passo_c = -1)
            if found[0]:
                found_pattern.append(found[1])

        # Vertical - Norte
        if (linha - len(pattern)) >= 0:
            found_pattern = busca_padrao(linha, linha - len(pattern), coluna, coluna+1, passo_l = -1)
            if found[0]:
                found_pattern.append(found[1])

        # Vertical - Sul
        if (linha + len(pattern)) <= m_linhas:
            found_pattern = busca_padrao(linha, linha + len(pattern), coluna, coluna+1)
            if found[0]:
                found_pattern.append(found[1])

        # Diagonal - Nordeste
        if ((linha - len(pattern)) >= 0) and ((linha + len(pattern)) < m_colunas):
            found_pattern = busca_padrao(linha, linha - len(pattern), coluna, coluna + len(pattern), passo_l = -1)
            if found[0]:
                found_pattern.append(found[1])

        # Diagonal - Noroeste
        if ((linha - len(pattern)) >= 0) and ((coluna - len(pattern)) >= 0):
            found_pattern = busca_padrao(linha, linha - len(pattern), coluna, coluna - len(pattern), passo_l = -1, passo_c = -1)
            if found[0]:
                found_pattern.append(found[1])

        # Diagonal - Sudeste
        if ((linha + len(pattern)) <= m_linhas) and ((coluna + len(pattern)) <= m_colunas):
            found_pattern = busca_padrao(linha, linha + len(pattern), coluna, coluna + len(pattern))
            if found[0]:
                found_pattern.append(found[1])

        # Diagonal - Sudoeste
        if ((linha + len(pattern)) <= m_linhas) and ((coluna - len(pattern)) >= 0):
            found_pattern = busca_padrao(linha, linha + len(pattern), coluna, coluna - len(pattern), passo_c = -1)
            if found[0]:
                found_pattern.append(found[1])
print(found_pattern)
''' 

# Impressão das posições iniciais (linha e coluna)
if not(found_pattern[0]):
  print("Nenhum padrao encontrado!")

else:
#  print(("Posicoes: " + " ".join([str((linha, coluna)) for linha, coluna in found_pattern[1]])).strip())
    print(found_pattern[1])
'''

