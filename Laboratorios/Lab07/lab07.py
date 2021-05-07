###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 7 - A Viagem
# Nome: Robert Willian Polli - 03/05/21
# RA: 187848
###################################################

weight = []
value  = []
ratio  = []
choose      = [0,0]          #Soma valor, soma peso

aux_ratio   = []
aux_choose  = []

# Leitura de dados
N = int(input())
W = int(input())

for i in range(N):      #Weight
    weight.append(int(input()))

for i in range(N):      #Value
    value.append(int(input()))

for i in range(N):
    ratio.append(value[i]/weight[i])

def return_Maximums(list):
    max = []
    for i in range(0, len(list)-1):
        max.append(list[i])
        if list[i+1]<list[i]:
            break
        elif(i+1 == len(list)-1):
            max.append(list[i+1])
    return(max)

# Escolha dos itens da mochila

k = 0
while(W != 0 and k < N):
    aux_ratio = ratio[:]
    aux_ratio.sort(reverse = True)

    aux_choose = return_Maximums(aux_ratio) if len(aux_ratio) != 1 else aux_ratio

    if len(aux_choose) == 1:
        index = ratio.index(aux_choose[0])
        if weight[index] <= W:
            choose[0] += value[index]
            choose[1] += weight[index]
            W -= weight[index]

        del(ratio[index])
        del(value[index])
        del(weight[index])

    else:
        save_index_values = []
        aux_value = []

        for i in range(len(aux_choose)):
            x = ratio.index(aux_choose[0])
            save_index_values.append(x)
            ratio[x] = "DESCARTE"

        for i in save_index_values:
            aux_value.append(value[i])
            ratio[i] = aux_choose[0]

        aux_value.sort(reverse = True)
        ord_value = return_Maximums(aux_value) if len(aux_value) != 1 else aux_value

        if len(ord_value) == 1:
            index = value.index(ord_value[0])

            if weight[index] <= W:
                choose[0] += value[index]
                choose[1] += weight[index]
                W -= weight[index]

            del(ratio[index])
            del(value[index])
            del(weight[index])
    k+=1

# Saída de dados
print(choose[0])
print(choose[1])