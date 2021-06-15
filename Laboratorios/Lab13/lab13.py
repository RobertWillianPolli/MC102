###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 13 - Super Trunfo
# Nome: ROBERT WILLIAN POLLI - Data: 14/06/2021
# RA: 187848
###################################################

atributos_value = {}
indices = {}

cartas = []
contador_de_insercoes = 0

def ordenar():
    for p in indices:
        peso = indices[p]
        initialLine = 0
        while(initialLine < len(cartas)):
            for line in range(initialLine+1, len(cartas)):
                if (cartas[line][peso] > cartas[initialLine][peso]):
                    global contador_de_insercoes
                    contador_de_insercoes += 1
                    cartas[line], cartas[initialLine] = cartas[initialLine], cartas[line]
            initialLine += 1
# Leitura das cartas

qtde_cartas = int(input())
campos = input().split(" ")

for loop in range(qtde_cartas):
    cartas.append(input().split(" "))
    atributos_value[cartas[-1][0]] = cartas[-1][1:]

prioridades = input().split(" ")

for index, priority in enumerate(prioridades):
    indices[priority] = len(prioridades) - index


# Ordenação das cartas
ordenar()

# Impressão dos dados

print('{:15s}'.format(campos[0]), ''.join('{:>10}'.format(campo) for campo in campos[1:]))

for carta in cartas:
    print('{:15s}'.format(carta[0]), ''.join('{:>10}'.format(atributo) for atributo in carta[1:]))
print('Insercoes realizadas:', contador_de_insercoes)