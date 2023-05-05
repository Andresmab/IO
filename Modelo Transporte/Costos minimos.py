# Importamos la libreria NumPy
import numpy as np

# Definimos la matriz de entrada de costo
A = np.array([[2, 4, 3, 4], [3, 2, 6, 2], [3, 1, 4, 5]])

# Suministro dado para la matriz de oferta
supply = np.array([40, 35, 35])

# Suministro dado para la matriz de demanda
demand = np.array([50, 20, 30, 10])

# Se inicializa el costo
y = 0

# Se comprueba donde la oferta y la demanda es cero o no
while supply.size > 0 and demand.size > 0:
    # Se encuentra el costo mínimo
    i, j = np.unravel_index(A.argmin(), A.shape)
    # Se encuentra el mínimo de la oferta y la demanda
    X = min(supply[i], demand[j])
    # Se actualiza el costo
    y += X * A[i, j]
    # Se comprueba que X es igual a la oferta o a la demanda y se elimina o se resta
    if X == supply[i]:
        A = np.delete(A, i, 0)
        supply = np.delete(supply, i)
        demand[j] -= X
    else:
        A = np.delete(A, j, 1)
        demand = np.delete(demand, j)
        supply[i] -= X

# Imprime el resultado
print('El costo mínimo de la matriz de entrada dada es:')
print(y)