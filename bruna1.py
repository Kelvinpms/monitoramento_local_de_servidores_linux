#questão 1
import numpy as np

# Dados fornecidos
t = np.array([0, 1, 1.8, 2.6, 3.9, 4.2, 5.8, 6.0, 7.0])
v = np.array([0, 3.9, 7.8, 10.2, 14.3, 17.3, 21.2, 25.1, 27.3])

# Função para calcular o polinômio interpolador de Lagrange
def lagrange_interp(x, xp, yp):
    n = len(xp)
    p = np.zeros(n)
    for j in range(n):
        # Calcula o polinômio de Lagrange para cada ponto de dados
        indicies = np.arange(n) != j
        p[j] = np.prod(x - xp[indicies]) / np.prod(xp[j] - xp[indicies])
    # Retorna o valor do polinômio interpolador em x
    return np.sum(yp * p)

# Calcula a altitude aproximada após 7 segundos
altitude = lagrange_interp(7, t[:3], v[:3])
print("Altitude aproximada após 7 segundos:", altitude, "metros")
