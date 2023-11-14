#Suma sencilla
def suma(x,y):
    resultado = x + y
    return resultado

#Multiplicacion de matrices
def multMat(a,b):
    resultados = []

    c = 0
    i = 0
    j = 0
    n = 0
    p = 0
    print(f"Se realiza una multiplicación de las matices {a} y {b}: ")
    for i in range(len(a)):  # Iterar sobre las filas de a
        fila_resultante = []  # Inicializar una lista para la fila resultante actual
        for j in range(len(b[p])):  # Iterar sobre las columnas de b
            c = 0
            for k in range(len(a[n])):
                posicionA = a[i][k]
                posicionB = b[k][j]
                c += posicionA * posicionB
            fila_resultante.append(c)  # Agregar el resultado a la fila resultante actual
        resultados.append(fila_resultante)  # Agregar la fila resultante a resultados
    for row in resultados: #Itera para mostrar la matriz
        for element in row:
            print(f"({element}", end=")" ) 
        print()
    return resultados
    

#Multiplicacion de matris por vector

def multVector (a, b):
    c = 0
    iterar = a[0] #Declaro en una varaiable la cantidad de columbas que tiens
    resultados = []
    for i in a: #Itero por las filas
        j = 0
        
        for i in iterar:#Itero por las columnas
            lista = a[c][j]
            lista = lista * b
            print(f"({lista}", end=")")
            resultados.append(lista)
            j = j + 1 #Incrementeo para cambiar de columna
        print()    
        c = c + 1 #Incremento para cambiar de fila
    
    return resultados

#Prductocruz
def ProCruz (a, b):
    resultado = []
    P_1 = (a[1] * b[2]) - (a[2] * b[1])
    resultado.append(P_1)
    P_2 = (a[2] * b[0]) - (a[0] * b[2])
    resultado.append(P_2)
    P_3 = (a[0] * b[1]) - (a[1] * b[0])
    resultado.append(P_3)
    return resultado