import numpy as np

#Solución a matriz tridiagonal 
def sol_tri_matriz(A, B, C, D):
  
    n = len(D)
    p = np.zeros(n - 1)
    q = np.zeros(n)

#Caso inicial 
    p[0] = C[0] / D[0]
    q[0] = B[0] / D[0]
    
    for i in range(1, n - 1):
        p[i] = C[i]/(B[i] - A[i]*p[i -1])
        q[i] = (D[i] - A[i]*q[i - 1])/(B[i] - A[i]*p[i -1])
    
#Caso final 
    q[-1] = (B[-1] - A[-2] * q[-2]) / (D[-1] + A[-2] * p[-2])
    
    x = np.zeros(n)
    x[-1] = q[-1]
    
#Último paso
    for i in range(n - 2, -1, -1):
        x[i] = p[i] * x[i + 1] + q[i]

    return x
   

A = np.array([2, 1, 1], dtype=float)
D = np.array([2, 4, 4, 5], dtype=float)
C = np.array([3, 1, 2], dtype=float)
B = np.array([5, 6, 7, 8], dtype=float)

x = sol_tri_matriz(A,B,C,D)

print("Las composiciones del componente 1 en las N etapas es:", x)
