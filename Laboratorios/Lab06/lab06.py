###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 6 - Plataforma
###################################################

# Leitura de dados

plataforma = [int(i) for i in input().split()]
i = int(input()) - 1

positions = [i]
state = ''

while(True):
    new_pos = i + plataforma[i]
    if new_pos > len(plataforma):
        state = 'direita'
        break
    elif new_pos < 0:
        state = 'esquerda'
        break
    else:
        if new_pos in positions:
            state = 'loop'
            break
        else:
            positions.append(new_pos)
            i = new_pos

for posicoes in positions:
    print(posicoes+1)
print(state)
