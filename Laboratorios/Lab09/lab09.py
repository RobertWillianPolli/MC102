#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 9 - Magic: Trocando Cartas
# Nome: ROBERT WILLIAN POLLI
# RA: 187848
#####################################################

cartas_para_troca = {}
cartas_desejadas = {}
propostas = []

# Leitura das cartas para troca
trocas = int(input())

# Leitura das cartas desejadas

for times in range(trocas):
  x = input()
  cartas = x.split(' ')
  cartas_para_troca[cartas[0]] = int(cartas[1])

distintas = int(input())

for times in range(distintas):
  y = input()
  cartas = y.split(' ')
  cartas_desejadas[cartas[0]] = int(cartas[1])


print(cartas_para_troca)


while(True):
  data = input()
  if data == "---":
    break
  else:
    propostas.append(data.split(' '))

# Processamento das trocas
for i in range(len(propostas)):

  if propostas[i][0] in cartas_desejadas:
    if propostas[i][1] in cartas_para_troca:
      troca_feita = True

      cartas_para_troca[propostas[i][1]] -= 1
      cartas_desejadas[propostas[i][0]]  -= 1

      if cartas_para_troca[propostas[i][1]] == 0:
        del(cartas_para_troca[propostas[i][1]])

      if cartas_desejadas[propostas[i][0]] == 0:
        del(cartas_desejadas[propostas[i][0]])

    else:
      troca_feita = False

  elif propostas[i][1] in cartas_para_troca:
    troca_feita = True

    cartas_para_troca[propostas[i][0]]  = 1
    cartas_para_troca[propostas[i][1]] -= 1

    if cartas_para_troca[propostas[i][1]] == 0:
      del(cartas_para_troca[propostas[i][1]])

  else:
    troca_feita = False

  if troca_feita:
    print("TROCA REALIZADA!")

  else:
    print("TROCA NAO REALIZADA!")

# Processamento se as cartas desejadas foram obtidas

if len(cartas_desejadas) != 0:
  print("JOAO NAO CONSEGUIU AS CARTAS DESEJADAS!")

else:
  print("JOAO CONSEGUIU AS CARTAS DESEJADAS!")
