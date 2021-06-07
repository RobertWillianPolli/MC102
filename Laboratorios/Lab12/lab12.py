###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 12 - Processamento de Imagens
# Nome: ROBERT WILLIAN POLLI    DATA: 07/06/2021
# RA: 187848
###################################################

def imprimir_imagem(imagem):
    print("P2")
    print(len(imagem[0]), len(imagem))
    print("255")
    for i in range(len(imagem)):
        print(" ".join(str(x) for x in imagem[i]))

def flip_horizontal(imagem_original): #(OK!)
    for horizontal in range(n):
        imagem_original[horizontal] = imagem_original[horizontal][::-1]
    return(imagem_original)

def flip_vertical(imagem_original): #(OK!)
    imagem_original = imagem_original[::-1]
    return(imagem_original)

def shift_vertical(imagem_original, x, tamanho): #(OK!)
    aux = [0]*tamanho
    for times in range(x):
        for a in range(tamanho):
            aux[a] = imagem_original[a-1]
        imagem_original = aux[:]
    return(imagem_original)

def shift_horizontal(imagem_original, x): #(OK!)
    aux = [0] * n

    for line in range(len(imagem_original)):
        aux[line] = shift_vertical(imagem_original[line], x, m)
    imagem_original = aux[:]
    return(imagem_original)

def crop(imagem_original, x1, y1, x2, y2): #(ok!)
    for linha_excluir in range(x1):
        del(imagem_original[0])

    for linha_excluir in range(x2, len(imagem_original)):
        del (imagem_original[-1])

    for coluna_excluir in range(y1):
        for col in range(len(imagem_original)):
            del(imagem_original[col][0])

    for coluna_excluir in range(y2, len(imagem_original[0])):
        for col in range(len(imagem_original)):
            del (imagem_original[col][-1])

    return(imagem_original)


#def shrink(imagem_original):


# leitura da imagem
_ = input()  # P2 - linha a ser ignorada

m, n = [int(x) for x in input().split()] # m colunas e n linhas

_ = input()  # 255 - linha a ser ignorada

imagem_original = []
for i in range(n):
    linha = [int(x) for x in input().split()]
    imagem_original.append(linha)

# leitura da operação e parâmetros
op = input()

if op == "flip":
    flip_h_v = input()

    if flip_h_v == "horizontal":
        imagem = flip_horizontal(imagem_original)
    else:
        imagem = flip_vertical(imagem_original)

elif op == "shift":
    shift_h_v = input()
    shift_num = int(input())

    if shift_h_v == "horizontal":
        imagem = shift_horizontal(imagem_original, shift_num)
    else:
        imagem = shift_vertical(imagem_original, shift_num, n)

elif op == "crop":
    crop_begin = [int(i) for i in input().split(" ")]
    crop_final = [int(i) for i in input().split(" ")]

    imagem = crop(imagem_original, crop_begin[0]-1, crop_begin[1]-1, crop_final[0]-1, crop_final[1]-1)

else:   #shrink
    imagem = shrink(imagem_original)

# impressão da imagem final
imprimir_imagem(imagem)