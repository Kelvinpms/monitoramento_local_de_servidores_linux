import numpy as np
t = [0.0, 1.0, 1.8, 2.6, 3.9, 4.2, 5.8, 6.0, 7.0]
v = [0.0, 3.9, 7.8, 10.2, 14.3, 17.3, 21.2, 25.1, 27.3]
# Diferença progressiva de primeira ordem
def forward_diff(y, h):
    dy = [y[i+1] - y[i] for i in range(len(y)-1)]
    dy.append((y[-1] - y[-2])/h)
    return dy

# Diferença regressiva de primeira ordem
def backward_diff(y, h):
    dy = [(y[1] - y[0])/h]
    for i in range(1, len(y)):
        dy.append(y[i] - y[i-1])
    return dy

# Diferença centrada de primeira ordem
def centered_diff(y, h):
    dy = [(y[1] - y[0])/h]
    for i in range(1, len(y)-1):
        dy.append((y[i+1] - y[i-1])/(2*h))
    dy.append((y[-1] - y[-2])/h)
    return dy
h = 1.0  # intervalo de tempo entre as medições
dy_f = forward_diff(v, h)  # diferença progressiva
dy_b = backward_diff(v, h)  # diferença regressiva
dy_c = centered_diff(v, h)  # diferença centrada

# Estimativa da altitude após 7 segundos utilizando a diferença progressiva de primeira ordem
altitude_f = v[0] + 7*dy_f[0]
print("Altitude aproximada (diferença progressiva): {:.2f} metros".format(altitude_f))

# Estimativa da altitude após 7 segundos utilizando a diferença regressiva de primeira ordem
altitude_b = v[-1] - (7*dy_b[-1])
print("Altitude aproximada (diferença regressiva): {:.2f} metros".format(altitude_b))

# Estimativa da altitude após 7 segundos utilizando a diferença centrada de primeira ordem
altitude_c = v[3] + (7*dy_c[3])
print("Altitude aproximada (diferença centrada): {:.2f} metros".format(altitude_c))
