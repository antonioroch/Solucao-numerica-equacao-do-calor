import matplotlib.pyplot as plt
import numpy as np

# parametros

L = 10        # cm
k = 0.8418    # cm^2/s

# malha

dx = 2    # incrementos
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

# matriz A

a = 1 + 2*lbd
b = -1*lbd

A = np.zeros([4, 4])
for i in range(0, 4):
    for j in range(0, 4):
        if i == j:
            A[i][j] = a
        elif i - 1 == j:
            A[i][j] = b
        elif i + 1 == j:
            A[i][j] = b
        else:
            A[i][j] = 0

# matriz B

y = 0
B = np.zeros([4, 1])
for l in range(0, 120):       # a matriz B é alterada a cada passo de tempo
    for i in range(0, 4):

        if i == 0:
            B[i] = M[1][l] + lbd*C1
        elif i == 3:
            B[i] = M[4][l] + lbd*C2
        else:
            B[i] = M[i+1][l]

    y = np.linalg.solve(A, B)  # a solução deste sistema , é a temperatura em todos nó do tempo atual
    for c in range(1, 5):
        M[c][l+1] = y[c - 1]


plt.plot(X, M[:, 30], X, M[:, 60], X, M[:, 90], X, M[:, 120])
plt.legend(('3s', '6s', '9s', '12s'))
plt.xlabel('Posição (cm)')
plt.ylabel('Temperatura (°C)')

plt.show()