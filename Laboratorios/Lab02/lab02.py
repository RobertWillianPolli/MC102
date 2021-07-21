###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 2 - O Grande Show
###################################################

# Leitura de dados
dist_a_b = int(input())
vel_t1 = float(input())
t_b_c = int(input()) #Tempo que o segundo trem sairá da estação B

dist_b_c = int(input())
vel_t2 = float(input())
t_show = int(input())

# Cálculo do tempo de chegada na cidade B e de chegada na cidade C

t_AB = (dist_a_b/vel_t1)*60
t_BC = (dist_b_c/vel_t2)*60
t_saidaTrem = t_b_c - t_AB

# Impressão da resposta

print(not((t_saidaTrem < 0) or ((t_AB + t_BC + t_saidaTrem) > t_show)))
