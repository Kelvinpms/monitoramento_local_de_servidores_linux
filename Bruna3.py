#Questão 3
import numpy as np

# função que calcula a força em função da altura
def F(h):
    return (31000 - 310*h) * 9.81

# altura máxima
h_max = 20

# passo
dh = 1

# número de intervalos
ns = [2, 5, 10, 20, 50, 100, 200]

# cálculo do trabalho para cada número de intervalos
for n in ns:
    hs = np
hs = np.linspace(0, h_max, n+1)

# cálculo do trabalho utilizando o método do trapézio
W = 0
for i in range(n):
    W += (F(hs[i]) + F(hs[i+1])) / 2 * (hs[i+1] - hs[i])

print(f'n={n}: W={W}')
