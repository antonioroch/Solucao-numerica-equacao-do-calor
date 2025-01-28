import matplotlib.pyplot as plt
import numpy as np

# parametros

L = 10        # cm
k = 0.8418    # cm^2/s

# malha

dx = 2        # incrementos
dt = 0.1

X = np.linspace(0, 10, 6)    #Dominio discreto
t = np.linspace(0, 12, 121)

M = np.zeros([len(X), len(t)])       # - [[T00,T01...],[T10,T11..],...]

lbd = (k * dt) / (dx ** 2)    # - constante lambda

# contorno e cond. iniciais

C1 = 100
C2 = 50
M[0, :] = C1
M[-1, :] = C2

Ci = 25
M[:, 0] = Ci

# método explícito

for l in range(0, 120):
    for i in range(1, 5):
       M[i][l+1] = M[i][l] + lbd*(M[i+1][l] - 2*M[i][l] + M[i-1][l])


# gráficos

plt.plot(X, M[:, 30], X, M[:, 60],X, M[:, 90], X, M[:, 120])
plt.legend(('3s', '6s', '9s', '12s'))
plt.xlabel('Posição (cm)')
plt.ylabel('Temperatura (°C)')
plt.show()

