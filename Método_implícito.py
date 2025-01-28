import matplotlib.pyplot as plt
import numpy as np

# parâmetros

L = 10    # cm
K = 0.8418 # cm^2/s
tm = 160

# malha

dx = 0.1 # incrementos
dt = 0.5

X = np.linspace(0, L, int(L/dx)+1)   #Dominio discreto
t = np.linspace(0, tm, int(tm/dt)+1)

M = np.zeros([len(X), len(t)])       # - [[T00,T01...],[T10,T11..],...]

lbd = (K * dt) / (dx ** 2)    # - número de Fourier

# temperaturas impostas nas laterais

C1 = 100
C2 = 50
M[0, :] = C1
M[-1, :] = C2


# temperatura inicial

Ci = 25
M[:, 0] = Ci

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
for l in range(0, int(tm/dt)):
    for i in range(0, int(L/dx)-1):

        if i == 0:
            B[i] = M[1][l] + lbd*C1
        elif i == int(L/dx)-2:
            B[i] = M[int(L/dx)-1][l] + lbd*C2
        else:
            B[i] = M[i+1][l]
            
    y = np.linalg.solve(A, B)
    for c in range(1, int(L/dx)):
        M[c][l+1] = y[c - 1]
          
# graficos

plt.xlabel('Posição (cm)')
plt.ylabel('Temperatura (°C)')
plt.title('Distribuição de temperatura pelo método implicito')

tl = 0

for l in np.arange(0, tm + dt, 2*dt):

    
    plt.plot(X, M[:, int(l/dt)], color = 'red')
    plt.legend([tl], title = 'Tempo (s)')
    tl += 2*dt
   
    plt.pause(0.1)

plt.show()
