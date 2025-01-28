import matplotlib.pyplot as plt
import numpy as np

# parametros

L = 10  # cm
K = 0.8418  # cm^2/s
tm = 50

# malha

dx =  0.5 # incrementos
dt = 0.1
X = np.linspace(0, L, int(L / dx) + 1)  # Dominio discreto
t = np.linspace(0, tm, int(tm / dt) + 1)

M = np.zeros([len(X), len(t)])  # - [[T_1^l],[T_2^l], ...]

lbd = (K * dt) / (dx ** 2)  # - constante lambda

# cond. inicial e contornos

C1 = 100
C2 = 50
M[0, :] = C1
M[-1, :] = C2

Ci = 25
M[:, 0] = Ci

# método explícito

for l in range(0, int(tm / dt)):
    for i in range(1, int(L / dx)):
        M[i][l + 1] = M[i][l] + lbd * (M[i + 1][l] - 2 * M[i][l] + M[i - 1][l])

# gráficos

plt.xlabel('Posição (cm)')
plt.ylabel('Temperatura (°C)')
plt.title('Distribuição de temperatura pelo método explícito')

tl = 0
for l in np.arange(0, tm + dt, 10*dt):
    
    
    plt.plot(X, M[:, int(l / dt)], color='blue')
    plt.legend([str(f'{tl:.2f}')], title='Tempo (s)')
    tl += 10*dt

    plt.pause(0.1)

plt.show()
