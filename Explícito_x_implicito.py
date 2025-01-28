import matplotlib.pyplot as plt
import numpy as np

# parametros

L = 10  # cm
K = 0.8418  # cm^2/s
tm = 2

# malha

dx = 0.5    # incrementos
dt = 0.5

X = np.linspace(0, L, int(L / dx) + 1)  # Dominio discreto
t = np.linspace(0, tm, int(tm / dt) + 1)

M = np.zeros([len(X), len(t)])  # - [[T_1^l],[T_2^l], ...]

Mi= np.zeros([len(X), len(t)]) 
lbd = (K * dt) / (dx ** 2)  # - constante lambda

# cond. inicial e contornos

C1 = 100
C2 = 50
M[0, :] = C1
Mi[0,:]=C1
M[-1, :] = C2
Mi[-1, :] = C2


Ci = 25
M[:, 0] = Ci
Mi[:, 0] = Ci

# método explícito

for l in range(0, int(tm / dt)):
    for i in range(1, int(L / dx)):
        M[i][l + 1] = M[i][l] + lbd * (M[i + 1][l] - 2 * M[i][l] + M[i - 1][l])
        

# método implícito

# matriz A

a = 1 + 2*lbd
b = -1*lbd

A = np.zeros([int(L/dx) -1 , int(L/dx)- 1])
for i in range(0, int(L/dx)-1):
    for j in range(0, int(L/dx)-1):
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
B = np.zeros([int(L/dx ) -1, 1])
for l in range(0, int(tm/dt)):       # a matriz B é alterada a cada passo de tempo
    for i in range(0, int(L/dx)-1):

        if i == 0:
            B[i] = Mi[1][l] + lbd*C1
        elif i == int(L/dx)-2:
            B[i] = Mi[int(L/dx)-1][l] + lbd*C2
        else:
            B[i] = Mi[i+1][l]
            
    y = np.linalg.solve(A, B)  # a solução deste sistema , é a temperatura em cada nivel de tempo
    for c in range(1, int(L/dx)):
        Mi[c][l+1] = y[c - 1]

# gráficos

plt.xlabel('Posição (cm)')
plt.ylabel('Temperatura (°C)')


tl = 0
for l in np.arange(0, tm + dt, dt):
    plt.clf()
    plt.xlabel('Posição (cm)')
    plt.ylabel('Temperatura (°C)')
    plt.plot(X, M[:, int(l / dt)], color='blue')
    plt.plot(X, Mi[:, int(l / dt)], color='red')
    plt.legend([str(f'{tl:.2f}')], title='Tempo (s)')
    tl += dt

    plt.pause(1)

plt.show()


