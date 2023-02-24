import math
import matplotlib.pyplot as plt

# Define a função da equação diferencial dC/dx = -kx
def dCdx(C, x, k):
    return -k * x * C

# Define as constantes k e C0
k_veg = 0.00034
k_noveg = 0.00017
C0 = 35.17

# Define a distância máxima e o passo h
xmax = 2000
h = 0.001

# Define as listas de valores de x e C para o gráfico
x = [0]
C = [C0]

# Calcula os valores de C para cada valor de x utilizando o método de Euler
while x[-1] < xmax:
    # Verifica se a distância é menor que 500 metros, para determinar o valor de k
    if x[-1] < 500:
        k = k_veg
    else:
        k = k_noveg
    # Calcula o próximo valor de C utilizando o método de Euler
    C_next = C[-1] + h * dCdx(C[-1], x[-1], k)
    # Adiciona os valores de x e C às listas
    x.append(x[-1] + h)
    C.append(C_next)

# Plota o gráfico
plt.plot(x, C)
plt.xlabel('Distância ao longo do córrego (m)')
plt.ylabel('Concentração do poluente (mg/m^3)')
plt.title('Concentração do poluente ao longo do córrego')
plt.show()
