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
def busca_padrao(linha_inicio, linha_fim, coluna_inicio, coluna_fim, padrao, passo_l = 1, passo_c = 1):
    status = []

    for i in range(linha_inicio, linha_fim, passo_l):
        for j in range(coluna_inicio, coluna_fim, passo_c):
            for p in padrao:
                if int(matriz[i][j]) in padroes[p]:
                    status.append(1)

# Leitura da matriz

matriz = []
pattern = ""
received = "Null"

while(True):
    received = input()
    if received[0] in commands:
        matriz.append(received.split(" "))
    else:
        pattern = received
        break

# DICA: use o método isdigit para verficar se a linha lida corresponde
# a uma linha da matriz ou ao padrão procurado

# Processamento da busca na matriz
m_linhas = len(matriz)
m_colunas = len(matriz[0])

posicoes = []

for linha in range(m_linhas):
    for coluna in range(m_colunas):
        # Horizontal - Direita
            if (coluna + len(pattern)) <= m_colunas:
                busca_padrao(linha, linha, coluna, coluna+len(pattern))

        # Horizontal - Esquerda
            if (coluna - len(pattern)) >= 0:
                busca_padrao(linha, linha, coluna, coluna+len(pattern), passo_c = -1)




# Impressão das posições iniciais (linha e coluna)

if 1==1:
  print("Nenhum padrao encontrado!")

else:
  print(("Posicoes: " + " ".join([str((linha, coluna)) for linha, coluna in posicoes])).strip())
