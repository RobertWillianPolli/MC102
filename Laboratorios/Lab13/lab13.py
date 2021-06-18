###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 13 - Super Trunfo
# Nome: ROBERT WILLIAN POLLI - Data: 14/06/2021
# RA: 187848
###################################################

indices = []
cartas = []

contador_de_insercoes = 0

def ordenar():
    for coluna in indices:
        matrizColuna = []
        initialLine = 0

        matrizColuna += (int(x[coluna]) for x in cartas)
        while(initialLine < qtde_cartas):
            change = matrizColuna[initialLine:].index(max(matrizColuna[initialLine:]))

            if change != 0:
                global contador_de_insercoes
                contador_de_insercoes += 1
                cartas.insert(initialLine, cartas[initialLine+change])
                del(cartas[initialLine+change+1])

                matrizColuna.insert(initialLine, initialLine+change)
                del(matrizColuna[initialLine+change+1])
            initialLine += 1

# Leitura das cartas

qtde_cartas = int(input())
campos = input().split(" ")

for loop in range(qtde_cartas):
    cartas.append(input().split(" "))

prioridades = input().split(" ")
prioridades.reverse()

for priority in prioridades:
    indices.append(campos.index(priority))

# Ordenação das cartas
ordenar()

# Impressão dos dados

print(f'{campos[0]:15s}', ''.join(f'{campo:>10}' for campo in campos[1:]))

for carta in cartas:
    print(f'{carta[0]:15s}', ''.join(f'{atributo:>10}' for atributo in carta[1:]))
print(f'Insercoes realizadas: {contador_de_insercoes}')