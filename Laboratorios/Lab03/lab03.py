###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 3 - Imposto de Renda
#
#
#''''' blué, bluééééé, blu blu ImPoStO è RoUbO blué blu bluè '''''
#
###################################################

limites = {0:[0,22847.76],
           1:[22847.77,33919.80],
           2:[33919.81, 45012.60],
           3:[45012.61, 55976.16],
           4:[55976.17,]}

aliq_deduzir = {0:[0,0],
                1:[0.075,1713.58],
                2:[0.15, 4257.57],
                3:[0.225,7633.51],
                4:[0.275,10432.32]}

# Leitura de dados
rendTributavel  = float(input())
previdencia     = float(input())
educacao        = float(input())
impostoRetido   = float(input())

# Abatimento com calculo simplificado
base_simplificado = rendTributavel*0.8

# Abatimento com calculo completo
if previdencia > (rendTributavel*0.12):
    previdencia = rendTributavel*0.12

if educacao > 3561.5:
    educacao = 3561.5

base_completo = rendTributavel - previdencia - educacao

# Calculo do IR com calculo simplificado
for i in range(0,4):
    if limites[4][0] <= base_simplificado:
        ir_simplificado = base_simplificado * aliq_deduzir[4][0] - aliq_deduzir[4][1]
        break

    elif limites[i][0] <= base_simplificado <= limites[i][1]:
        ir_simplificado = base_simplificado * aliq_deduzir[i][0] - aliq_deduzir[i][1]
        break

# Calculo do IR com calculo completo
for i in range(0, 4):
    if limites[4][0] <= base_completo:
        ir_completo = base_completo * aliq_deduzir[4][0] - aliq_deduzir[4][1]
        break

    elif limites[i][0] <= base_completo <= limites[i][1]:
        ir_completo = base_completo * aliq_deduzir[i][0] - aliq_deduzir[i][1]
        break

# Calculo do IR devido com calculo simplificado
ajuste_simplificado = ir_simplificado - impostoRetido

# Calculo do IR devido com calculo completo
ajuste_completo = ir_completo - impostoRetido

# Saída
print(f"Base de calculo (Simplificado): {base_simplificado:0.2f}".replace(".", ","))
print(f"Base de calculo (Completo): {base_completo:0.2f}".replace(".", ","))
print(f"Valor do IR (Simplificado): {ir_simplificado:0.2f}".replace(".", ","))
print(f"Valor do IR (Completo): {ir_completo:0.2f}".replace(".", ","))
print(f"Valor do ajuste (Simplificado): {ajuste_simplificado:0.2f}".replace(".", ","))
print(f"Valor do ajuste (Completo): {ajuste_completo:0.2f}".replace(".", ","))
