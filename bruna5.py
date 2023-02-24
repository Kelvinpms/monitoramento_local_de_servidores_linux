#questão 5
# Profundidade do canal (m)
profundidade = [0.0, -0.4, -1.5, -1.7, -1.3, -1.8, -0.3, 0.0]

# Distância entre os pontos (m)
dx = 0.1

# Área total inicializada com zero
area_total = 0

# Percorre os pontos
for i in range(len(profundidade)):
    # Base menor do trapézio
    b1 = dx * i
    
    # Base maior do trapézio
    b2 = dx * (i + 1)
    
    # Altura do trapézio
    h = abs(profundidade[i] - profundidade[i-1])
    
    # Área do trapézio
    area = (b1 + b2) * h / 2
    
    # Soma a área ao total
    area_total += area

# Velocidade média do fluxo (m/s)
v = 2.8 ** -1

# Vazão (m³/s)
q = area_total * v

# Imprime o resultado
print("A vazão aproximada é de", round(q, 2), "m³/s")
