import __init__ as test

print("""
Que prueba va a realizar:
-----
1) Suma => suma
2) Multiplicacion de matrices => MxM
3) Multiplicacion de matriz por vector => MxV
4) Producto Cruz    =>  ProCruz
-----
      
""")


while True: #Bucle para realizar varias prubas con control
    
    usuario = str(input("Prueba: "))

    if usuario == "suma": #Simple de suma
        resultado = test.suma(2,3)
        print(resultado)
         
    elif usuario == "MxM": #Multiplicacion de matrices
        a = [[-1, 0, 1], [7, 3, -(13/2)], [3, (1/2), -(5/2)]]
        b = [[2, 4, 5], [2, 3, 4], [3, 4, 6]]

        multiplicacion = test.multMat(a, b)
        print(multiplicacion)

    elif usuario == "MxV": #Matriz por vector
        a = [[-1, 0, 3, 4], [7, 3, 5, 6], [3, 2, 4, 3]]
        b = 2
        resultado = test.multVector(a,b)
        print(resultado)

    elif usuario == "ProCruz": #Matriz por vector
        a = [3, -1, 1]
        b = [1, 2, -1]
        resultado = test.ProCruz(a, b)
        print(resultado)
        print(f"{resultado[0]}i {resultado[1]}j {resultado[2]}k")
        
        
    else:
        print("Comando Equivocado. Intenta de nuevo.")