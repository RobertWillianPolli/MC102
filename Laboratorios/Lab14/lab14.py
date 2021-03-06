###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 14 - Caça-Números
# Data: 21/06/2021
###################################################

padroes = {"A":range(10),
           "E":range(2, 10, 2),
           "O":range(1, 10, 2),
           "C":[4, 6, 8, 9],
           "P":[2, 3, 5, 7],
           "S":[1],
           "T":[3, 6, 9]
           }

matriz = []
pattern = ""
received = "Null"

possibilidades          = []
posicoes_iniciais       = []
possibilidades_iniciais = []

def busca_padrao(linha, coluna, padrao):
    pp = []
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if not((linha + i < 0) or (coluna + j < 0) or (linha + i > (m_linhas-1)) or (coluna + j > (m_colunas-1)) or (i == j == 0)) \
                    and (int(matriz[linha + i][coluna + j]) in padroes[padrao]):
                pp.append([linha + i, coluna + j])
    return(pp)

def check(p, my_ordem):
    my_ordem += 1

    for positions in p:
        possibilidades = busca_padrao(positions[0], positions[1], pattern[my_ordem])

        if ((my_ordem == (len(pattern)-1)) and possibilidades != []) or check(p = possibilidades, my_ordem = my_ordem):
            return(True)

# Leitura da matriz
while(True):
    received = input()
    if not(received[0] in padroes):
        matriz.append(received.split(" "))
    else:
        pattern = received
        break

# Processamento da busca na matriz
m_linhas = len(matriz)
m_colunas = len(matriz[0])

for linha in range(m_linhas):
    for coluna in range(m_colunas):
        if (int(matriz[linha][coluna]) in padroes[pattern[0]]) and \
            check(p = busca_padrao(linha, coluna, pattern[1]), my_ordem=1) and not([linha+1, coluna+1] in posicoes_iniciais):
                    posicoes_iniciais.append([linha+1, coluna+1])

# Impressão das posições iniciais (linha e coluna)
if posicoes_iniciais == []:
    print("Nenhum padrao encontrado!")

else:
    print(("Posicoes: " + " ".join([str((linha, coluna)) for linha, coluna in posicoes_iniciais])).strip())
