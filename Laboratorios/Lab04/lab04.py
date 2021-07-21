###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 4 - Magic: The Gathering
###################################################

#Variaveis
cartas_total = []
cartas_conseguidas = 0
boosters_comprados = 0

# Leitura do orçamento, do valor do booster e da quantidade de cartas desejadas

X = float(input())
B = float(input())
D = int(input())

quantidade_boosters_max = X//B

# Leitura da sequência de cartas
while(True):
    try:
        cartas_total.append(input())
    except:
        break

while(boosters_comprados + 1 <= quantidade_boosters_max):

    if cartas_total[boosters_comprados] in ['3', '5']:
        cartas_conseguidas += 1

    boosters_comprados += 1

    if cartas_conseguidas == D:
        break

total_gasto = B * boosters_comprados
total_restante = X - total_gasto

quantidade_cartas = cartas_conseguidas

# Impressão das informações de saída

print(f"ORCAMENTO: {X:.2f} REAIS")
print(f"VALOR DO BOOSTER: {B:.2f} REAIS")
print(f"TOTAL GASTO: {total_gasto:.2f} REAIS")
print(f"TOTAL RESTANTE: {total_restante:.2f} REAIS")
print(f"QUANTIDADE DE BOOSTERS COMPRADOS: {int(boosters_comprados)}")
print(f"QUANTIDADE DESEJADA DE CARTAS DA COR VERDE OU DA COR PRETA: {D}")
print(f"QUANTIDADE OBTIDA DE CARTAS DA COR VERDE OU DA COR PRETA: {quantidade_cartas}")

if cartas_conseguidas == D:
    print("JOAO CONSEGUIU MONTAR SEU NOVO DECK!")
else:
    print("JOAO NAO CONSEGUIU MONTAR SEU NOVO DECK!")
