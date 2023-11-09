def suma(x,y):
    resultado = x + y
    return resultado

#Matriz



def multmat(a,b):
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



    for row in resultados:
        for element in row:
            print(f"({element}", end=")" )
        print()