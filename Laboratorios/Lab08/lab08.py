###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 8 - O Desafio da Palavra Escondida
# Data: 10/05/2021
###################################################

# DICA: use os métodos lower, replace, split e find
palavras_in = []
palavras = []
output = []

# Leitura de dados
linhas = int(input())
for i in range(linhas):
    palavras_in.append(input())

palavraProcurada = input()
#--------------------------
for swap in range(len(palavras_in)):
    for split in [".", ",", ":", ";", "!", "?", " "]:
        palavras_in[swap] = palavras_in[swap].replace(split, "@#$")
        palavras_in[swap] = palavras_in[swap].lower()

for remover in palavras_in:
    palavras += remover.split("@#$")

while("" in palavras):
    palavras.remove("")

# Verificação da palavra no texto
for i in palavraProcurada.lower():
    for index_palavra, palavra in enumerate(palavras):
        if i in palavra:
            output.append([i, index_palavra+1, palavra.find(i)+1])
            palavras[index_palavra] = " "
            break
        palavras[index_palavra] = " "

# Impressão da saída do programa
if len(output) < len(palavraProcurada):
    print("Palavra nao encontrada")

else:
    print("Palavra encontrada")
    for saida in output:
        print(f"{saida[0]}: palavra {saida[1]}, letra {saida[2]}")
