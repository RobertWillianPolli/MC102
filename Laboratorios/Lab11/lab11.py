###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 11 - Jogo da Similaridade Máxima
# Data: 31/04/2021
###################################################

matriz_maior = []
matriz_menor = []

pos                 = [0,0]
similaridade_maxima = 0

"""
Esta função recebe quatro parâmetros:
 - linha: indíce de uma linha da matriz maior
 - coluna: indice de uma coluna da matriz maior
 - menor: matriz quadrada com um padrão a ser encontrado

A função deve retornar o grau de similaridade entre a submatriz
da matriz maior que começa na posição definida pelos parâmetros
linha e coluna e a matriz menor
"""

def calcula_similaridade(linha, coluna, menor):
    igual = 0
    for linha_maior in range(linha, linha + menor):
        for coluna_maior in range(coluna, coluna + menor):
            if matriz_menor[linha_maior - linha][coluna_maior - coluna] == matriz_maior[linha_maior][coluna_maior]:
                igual += 1

    return(igual*100 / (menor * menor))

# Leitura das matrizes
linha_coluna_maior = int(input())

for times in range(linha_coluna_maior):
    matriz_maior.append(input().split(" "))

linha_coluna_menor = int(input())

for times in range(linha_coluna_menor):
    matriz_menor.append(input().split(" "))

# Cálculo da submatriz de similaridade máxima
#POSIÇÕES INICIAIS

for linha_maior in range(linha_coluna_maior - linha_coluna_menor + 1):
    for coluna_maior in range(linha_coluna_maior - linha_coluna_menor + 1):

        porcentagem = calcula_similaridade(linha_maior, coluna_maior, linha_coluna_menor)
        if porcentagem > similaridade_maxima:
            similaridade_maxima = porcentagem
            pos = [linha_maior, coluna_maior]

# similaridade
print(f"Posição: ({pos[0]},{pos[1]})")
print(f"Similaridade máxima: {similaridade_maxima:.2f}%")
