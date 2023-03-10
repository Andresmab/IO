import numpy as np
from scipy.optimize import linprog
#Andres Mauricio Ariza Bustos 20202020113


# Definimos la matriz de coeficientes de las restricciones
A = np.array([[2, 4], [8, 2]])

# Definimos los vectores de coeficientes de las variables y de los términos independientes de las restricciones
b = np.array([15, 20])

# Definimos el vector de coeficientes de la función objetivo
c = np.array([-2, -3])

# Resolvemos el problema de maximización con el método simplex
resultado = linprog(c, A_ub=A, b_ub=b, method='simplex')

# Imprimimos los resultados
print("Estado:", resultado.message)
print("Número óptimo de unidades de A:", round(resultado.x[0]))
print("Número óptimo de unidades de B:", round(resultado.x[1]))
print("Beneficio máximo:", round(-resultado.fun))