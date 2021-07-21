###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 15 - De salto em salto
# Data: 29/06/2021
# Fora Bolsonaro!
###################################################

'''
Dada uma matriz e a posição (x,y) de uma possível pessoa infectada,
atualiza a matriz para que cada caractere correspondente a uma pessoa
infectada seja substituído por 'X'.
'''
def propagacao_de_fake_news(matriz, x, y, alcance_value=0):
    alcance = alcance_value

    if alcance_value == 0 and matriz[x][y].isdigit():
        alcance = int(matriz[x][y])

    def percorrer(inicio_x, fim_x, inicio_y, fim_y, passo_x, passo_y):

        for coordenada_y in range(inicio_y, fim_y, passo_y):
            for coordenada_x in range(inicio_x, fim_x, passo_x):

                if not(coordenada_x in range(m_linhas)) or not(coordenada_y in range(m_colunas)) or matriz[coordenada_x][coordenada_y] == "#":
                    return()

                elif matriz[coordenada_x][coordenada_y].isdigit():
                    novo_alcance = int(matriz[coordenada_x][coordenada_y])
                    matriz[coordenada_x][coordenada_y] = "X"
                    propagacao_de_fake_news(matriz=matriz, x=coordenada_x, y=coordenada_y, alcance_value=novo_alcance)

    percorrer(x, x + 1, y, y - alcance - 1,  1, -1)  # Norte
    percorrer(x, x + 1, y, y + alcance + 1,  1,  1)  # Sul
    percorrer(x, x + alcance + 1, y, y + 1,  1,  1)  # Leste
    percorrer(x, x - alcance - 1, y, y + 1, -1,  1)  # Oeste

# Leitura de dados
n = int(input())
matriz = []

for _ in range(n):
    matriz.append(list(input()))

m_linhas  = len(matriz)
m_colunas = len(matriz[0])
x, y = [int(i) for i in input().split()]

# Atualiza a matriz com a propagação da noticia falsa.

propagacao_de_fake_news(matriz, x, y)

# Impressão do resultado
for line in matriz:
    print("".join(line))
