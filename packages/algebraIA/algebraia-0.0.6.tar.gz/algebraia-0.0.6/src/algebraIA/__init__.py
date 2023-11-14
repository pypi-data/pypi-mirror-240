import numpy as np

# fernando codigos-----------------------------------------------------------------------
def matriz(cA, rA, cB, rB):
    
    import random
    
    def numeroMatriz():
        numero = random.randint(-10,10)
        return numero

    while True:
        # Matríz a
        columnasA =  cA
        renglonesA =  rA
        # Matríz b
        columnasB = cB
        renglonesB = rB
        if columnasA == renglonesB:
            break

    matrizA = [[numeroMatriz() for _ in range(columnasA)] for _ in range(renglonesA)]

    matrizB = [[numeroMatriz() for _ in range(columnasB)] for _ in range(renglonesB)]

    lista = [[] ]

    # Tamaño de la matríz c
    matrizC = [[0 for _ in range(len(matrizB[0]))] for _ in range(len(matrizA))]

    for i in range(len(matrizA)):
        for j in range(len(matrizB[0])):
            for k in range(len(matrizA[0])):
                posicionA = matrizA[i][k]
                posisionB = matrizB[k][j]
                matrizC[i][j] += posicionA * posisionB

    
    return matrizA, matrizB, matrizC


def vectorRestultante(*vectores):
    vectorResultante = [ sum(valores) for valores in zip(*vectores)]
    return vectorResultante


# gael codigos-----------------------------------------------------------------------
def producto_escalar():
    # Importación de libreria
    import numpy as np
    # Definición de vectores
    v1 = np.array([20,30,40,50],float)
    v2 = np.array([100,200,300,400],float)
    # Calculo de PE
    r=np.dot(v1,v2)
    # Calculo de norma de vectores
    n1=np.linalg.norm(v1)
    n2=np.linalg.norm(v2)

    print("el producto escalar es: ", r)
    print("la norma de v1 es: ", n1)
    print("la norma de v2 es: ", n2)

def Gauss_Jordan_pri():
    matriz = []
    res=[]
    # ... rest of your code ...

def ecl(n):
    import numpy as np
    import matplotlib.pyplot as plt

    x = np.arange(-6,6)

    y_2 = -x+3
    y_3 = 2*x+1
    plt.figure()
    plt.plot(x, y_2)
    plt.plot(x, y_3)

    plt.xlim(-8,8)
    plt.ylim(-8,8)

    plt.axvline(x=0, color='grey')
    plt.axhline(y=0, color='grey')

    plt.show()


# maria codigos-----------------------------------------------------------------------


# Definir el sistema de ecuaciones
# 2x + y - z = 8
# -3x - y + 2z = -11
# -2x + y + 2z = -3

coeficientes = np.array([[2, 1, -1],
                        [-3, -1, 2],
                        [-2, 1, 2]])

constantes = np.array([8, -11, -3])

# Resolver el sistema de ecuaciones lineales
solucion = np.linalg.solve(coeficientes, constantes)

# Mostrar la solución
print("Solución del sistema de ecuaciones:")
print("x =", solucion[0])
print("y =", solucion[1])
print("z =", solucion[2])