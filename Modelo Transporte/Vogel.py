### Bibliotecas 
import pandas as np
from pulp import *
from pandas import DataFrame


##Una empresa de transporte p´ublico llamada Transunion tiene 3 rutas diferentes R1, R2, R3
##a lo largo de la ciudad de Bogot´a. Cada una de las rutas tiene la posibilidad de subir 40,
##35, 35 pasajeros respectivamente , las cuales deben ser usadas para 4 diferentes estaciones
##donde esperan 50, 20, 30, 10 pasajeros respectivamente en cada estaci´on. Halle el costo de
##transporte minimo, usando los 3 diferentes m´etodos del modelo de transporte.


### Origenes R1, R2,R3 Que son las rutas de los buses y destinos E1, E2, E3, E4 que son las estaciones

origen = ['R1','R2','R3']
destino = ['E1','E2', 'E3', 'E4']

oferta = {'R1': 40, 'R2' : 35, 'R3': 35}
demanda = {'E1': 50, 'E2' : 20, 'E3' : 30, 'E4' :10}

costo_envio ={'R1':{'E1': 2, 'E2' : 4, 'E3' : 3, 'E4' :3},
             'R2':{'E1': 3, 'E2' : 2, 'E3' : 6, 'E4' :2},
             'R3': {'E1': 3, 'E2' : 1, 'E3' : 4, 'E4' :5}}

### Declaramos la  función objetivo... nota que buscamos minimizar el costo(LpMinimize)
prob = LpProblem('Transporte', LpMinimize)

rutas = [(i,j) for i in origen for j in destino]

cantidad = LpVariable.dicts('Cantidad de Envio',(origen,destino),0)

prob += lpSum(cantidad[i][j]*costo_envio[i][j] for (i,j) in rutas)

for j in destino:
    prob += lpSum(cantidad[i][j] for i in origen) == demanda[j]

for i in origen:
    prob += lpSum(cantidad[i][j] for j in destino) <= oferta[i]

### Resolvemos e imprimimos el Status, si es Optimo, el problema tiene solución.
prob.solve()
print("Status:", LpStatus[prob.status])

### Imprimimos la solución
for v in prob.variables():
    if v.varValue > 0:
        print(v.name, "=", v.varValue)
print('El costo mínimo es:', value(prob.objective))