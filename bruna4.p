#questão 4

import numpy as np
import matplotlib.pyplot as plt


# Define as dimensões da placa
L = 1.0
H = 1.0

# Define as temperaturas nas bordas
T_top = 20
T_right = 15
T_bottom = 25
T_left = 22

# Define o número de pontos na placa
nx = 101
ny = 101

# Define as condições iniciais
T = np.zeros((ny, nx))
T[0, :] = T_top
T[:, -1] = T_right
T[-1, :] = T_bottom
T[:, 0] = T_left
T_prev = np.zeros((ny, nx))

# Define o erro máximo
tol = 1e-5

# Define o número máximo de iterações
maxiter = 10000

# Define o passo da malha
dx = L / (nx - 1)
dy = H / (ny - 1)

# Define os coeficientes da equação
a = 1 / dx**2
b = 1 / dy**2
c = -2 * (a + b)

# Executa o método de Gauss-Seidel
for it in range(maxiter):
    # Atualiza as temperaturas
    for i in range(1, ny-1):
        for j in range(1, nx-1):
            T[i, j] = (1/c) * (a*(T[i, j-1] + T[i, j+1]) +
                               b*(T[i-1, j] + T[i+1, j]))
    # Verifica a convergência
    if np.abs(T - T_prev).max() < tol:
        print("Convergiu após", it, "iterações.")
        break
    T_prev = T.copy()

# Plota o gráfico da solução
X, Y = np.meshgrid(np.linspace(0, L, nx), np.linspace(0, H, ny))
plt.contourf(X, Y, T, cmap='jet')
plt.colorbar()
plt.xlabel("x")
plt.ylabel("y")
plt.show()
print(T)
