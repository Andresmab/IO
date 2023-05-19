matriz = []
matriz2 =[]
result = 0

filas = int (input("DIGITE NUMERO DE FILAS")) + 1
columnas = int (input("DIGITE NUMERO DE COLUMNAS")) + 1

for i in range(filas):
    matriz.append([0]*columnas)
    matriz2.append([0]*columnas)

print("INGRESE OFERTAS Y DEMANDAS")
sumaF, sumaC =0, 0
while(True):
    sumaF, sumaC = 0,0
    for f in range(filas-1):
        matriz[f][columnas-1] = int(input("INGRESE OFERTA [%d]: " %(f+1)))
        matriz2[f][columnas-1] = matriz[f][columnas-1]
        sumaF += matriz[f][columnas-1]
    for c in range(columnas-1):
        matriz[filas-1][c] = int(input("INGRESE DEMANDA [%d]: " %(c+1)))
        matriz2[filas-1][c] = matriz[filas-1][c]
        sumaC += matriz[filas-1][c]
    if(sumaF == sumaC):
        break
    else:
        print("INGRESA NUEVAMENTE LOS VALORES. NOTA: RECUERDA LA SUMA DE OFERTA DEBE SER IGUAL A LA DE LAS DEMANDAS")
        
print("INGRESE INVENTARIO/STOCK/ALMACEN. ")
for f in range(filas-1):
    for c in range(columnas-1):
        matriz[f][c] = int(input("INGRESE EL ELEMENTO [%d,%d]: " %(f,c)))

print("CALCULAR MOVIMIENTOS -> Matriz2")
posF, posC = 0, 0
vo, vi = 0, 0
menor, igual  = 0, 0

while(True):
    sumaF, sumaC = 0, 0
    for f in range(filas-1):
        sumaF += matriz2[f][posC]
    for c in range(columnas-1):
        sumaC += matriz2[posF][c]
    
    vo = matriz[filas-1][posC] - sumaF
    vi = matriz[posF][columnas-1] - sumaC

    if(vo < vi):
        menor = vo
        matriz2[posF][posC] = menor
        posC += 1
    
    elif(vi < vo):
        menor = vi
        matriz2[posF][posC] = menor
        posF += 1

    elif(vo == vi):
        igual = (vo+vi)//2
        matriz2[posF][posC] = igual
        posF += 1
        posC += 1
    
    if(posF == filas-1 or posC == columnas-1):
        break

print("Matriz1 -> Inventario")
for p in range(filas):
    print(matriz[p])

print("Matri<z -> Movimientos")
for p in range(filas):
    print(matriz2[p])

for fila in matriz2:
    for casilla in fila:
        result += casilla
        
print("Resultado usando método esquina noroeste: ", result)