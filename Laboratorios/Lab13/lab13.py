###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 13 - Super Trunfo
# Nome: ROBERT WILLIAN POLLI - Data: 14/06/2021
# RA: 187848
###################################################

indices = []
initialPosition = []

cartas = []
contador_de_insercoes = 0

def ordenar():
    for coluna in indices:
        initialLine = 0

        while(initialLine < qtde_cartas):
            for line in range(initialLine+1, qtde_cartas):
                if (int(cartas[initialLine][coluna]) < int(cartas[line][coluna])):
                    #print(initialLine, line)
                    global contador_de_insercoes
                    contador_de_insercoes += 1
                    cartas[line], cartas[initialLine] = cartas[initialLine], cartas[line]
            initialLine += 1

    for coluna in [indices[-1]]:
        initialLine = 0
        while (initialLine < qtde_cartas):
             for line in range(initialLine + 1, qtde_cartas):
                if cartas[line][coluna] == cartas[line-1][coluna]:
                    if initialPosition.index(cartas[line][0]) < initialPosition.index(cartas[line-1][0]):
                        cartas[line], cartas[line-1] = cartas[line-1], cartas[line]
             initialLine += 1

# Leitura das cartas

qtde_cartas = int(input())
campos = input().split(" ")

for loop in range(qtde_cartas):
    cartas.append(input().split(" "))

for init in cartas:
    initialPosition += [init[0]]

prioridades = input().split(" ")
prioridades.reverse()

for priority in prioridades:
    indices.append(campos.index(priority))

# Ordenação das cartas
ordenar()

# Impressão dos dados

print('{:15s}'.format(campos[0]), ''.join('{:>10}'.format(campo) for campo in campos[1:]))

for carta in cartas:
    print('{:15s}'.format(carta[0]), ''.join('{:>10}'.format(atributo) for atributo in carta[1:]))
print('Insercoes realizadas:', contador_de_insercoes)