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
def busca_padrao(linha, coluna, padrao):
    p = []
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if not((linha + i < 0) or (coluna + j < 0) or (linha + i > (m_linhas-1)) or (coluna + j > (m_colunas-1)) or (i == j == 0)):
                if int(matriz[linha + i][coluna + j]) in padroes[padrao]:
                    p.append([linha + i, coluna + j])
    return(p)

def check(p):
    global ordem
    ordem += 1

    for positions in p:
        possibilidades = busca_padrao(positions[0], positions[1], pattern[ordem])

        if ordem == (len(pattern) - 1):
            if possibilidades != []:
                return(True)
            else:
                return(False)
        else:
            return(check(possibilidades))

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

possibilidades          = []
posicoes_iniciais       = []
possibilidades_iniciais = []

global ordem

for linha in range(m_linhas):
    for coluna in range(m_colunas):
        ordem = 1
        if int(matriz[linha][coluna]) in padroes[pattern[0]]:
            possibilidades_iniciais = busca_padrao(linha, coluna, pattern[1])
            if possibilidades_iniciais != []:
                if check(possibilidades_iniciais):
                    posicoes_iniciais.append([linha+1, coluna+1])


#print(posicoes_iniciais)

# Impressão das posições iniciais (linha e coluna)
if posicoes_iniciais == []:
  print("Nenhum padrao encontrado!")

else:
    print(("Posicoes: " + " ".join([str((linha, coluna)) for linha, coluna in posicoes_iniciais])).strip())