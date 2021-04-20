###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 5 - Super Sete
# Nome: ROBERT WILLIAN POLLI
# RA: 187848
###################################################

possibilidades = [] #Números possiveis para a aposta
combinacoes = []

numbers = [0, 0, 0, 0, 0, 0, 0]
divider = [0, 7, 13, 14, 21, 26, 28, 35, 39, 42, 49, 52, 56, 63, 65]

for i in range(7):
    possibilidades.append(list(range(10)))

# Leitura de dados
for num in [0,2,3,5]: #primeira, terceira, quarta e sexta coluna
    numbers[num] = int(input())

#Os números escolhidos para cada coluna devem seguir uma ordem não decrescente.
#Ou seja, o número de uma coluna deve ser maior ou igual aos números das colunas anteriores.
for colunm in [1,4,6]:
    for number in range(numbers[colunm-1]):
        possibilidades[colunm].remove(number)

for colunm in [1,4]:
    for number in range(numbers[colunm+1]+1, 10):
        possibilidades[colunm].remove(number)

#A soma dos 7 números da aposta não pode ser um número múltiplo de 7 ou 13
#print(possibilidades)
for segundo in possibilidades[1]:
    for quinto in possibilidades[4]:
        for setimo in possibilidades[6]:
            if not((sum(numbers) + setimo + quinto + segundo) in divider):
                combinacoes.append([segundo, quinto, setimo])

# Impressão dos quatro números das colunas fornecidos como entrada
n1, n3, n4, n6 = numbers[0], numbers[2], numbers[3], numbers[5]

print(f"Primeira: {n1}")
print(f"Terceira: {n3}")
print(f"Quarta: {n4}")
print(f"Sexta: {n6}")

# Processamento e impressão da lista de possíveis apostas

print("Lista de apostas:")
for nums in range(len(combinacoes)):
    n2, n5, n7 = combinacoes[nums][0], combinacoes[nums][1], combinacoes[nums][2]
    print(f"{n1} - {n2} - {n3} - {n4} - {n5} - {n6} - {n7}")