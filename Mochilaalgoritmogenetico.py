import random
import matplotlib.pyplot as plt
import numpy as np
from random import randint

# Entrada de datos
capacidad = int(input('Ingresar capacidad de la mochila: '))
poblacion = int(input('Ingrese numero de individuos: '))
elementos = int(input('Ingrese numero de elementos: '))

# Matriz para representar la población de individuos
P1 = [[0 for x in range(0, elementos)] for y in range(0, poblacion)]

# Variables adicionales
pesotoa = 0
PV = []  # Lista para almacenar los pesos de los elementos
VV = []  # Lista para almacenar los valores de los elementos
P = []   # Lista para almacenar los pesos seleccionados por individuo
Pesotoa = []  # Lista para almacenar los pesos totales de los individuos
Valortoa = []  # Lista para almacenar los valores totales de los individuos
Fitness = []  # Lista para almacenar los valores de fitness de los elementos
Competencia = []  # Lista para almacenar los valores de Valortoa
Piscina = []  # Lista para almacenar los valores de Valortoa
Posiciones = []  # Lista para almacenar las posiciones de los elementos seleccionados
V = []  # Lista para almacenar valores de elementos
Ratio = []  # Lista para almacenar los valores de Ratio
Mejor = []  # Lista para almacenar los valores de Mejor
Pasar = []  # Lista para almacenar los valores de Pasar

# Función para generar la población inicial
def poblacioninicial():
    for x in range(0, elementos, 1):
        PV.append(random.randint(1, 100))
        VV.append(random.randint(1, 100))
        
    for z in range(0, poblacion, 1):
        for z1 in range(0, elementos, 1):
            P1[z][z1] = randint(0, 1)
            
    for xi in range(0, poblacion, 1):
        s = ' '
        for yi in range(0, elementos, 1):
            s = s + str(P1[xi][yi])
        print(s)
    print(PV, VV)

# Función para decodificar la población
def decodificadora():
    for xd in range(0, elementos, 1):
        r = VV[xd] / PV[xd]
        Fitness.append(r)
        
    Ratio = Fitness[:]
    for xcom in range(0, len(Ratio), 1):
        b = 0
        for ycom in range(0, len(Ratio), 1):
            if ycom != len(Ratio) - 1:
                if Ratio[ycom] > Ratio[ycom + 1]:
                    b = Ratio[ycom]
                    Ratio[ycom] = Ratio[ycom + 1]
                    Ratio[ycom + 1] = b
    print('antes', Fitness)
    print('ordenado por fitness', Ratio)
    
    for xor in range(0, elementos, 1):
        a = Fitness.index(Ratio[xor])  
        P.append(PV[a])
        V.append(VV[a])
    print(P)
    print(V)
    op = 0

# Función para realizar la selección de individuos
def seleccion():
    for xe in range(0, poblacion, 1):
        e = elementos
        pesotoa = 0
        valortoa = 0
        for ye in range(0, elementos, 1):
            if P[ye] > capacidad:
                P[ye] = 0
                V[ye] = 0
            if P1[xe][ye] == 1:
                pesotoa = pesotoa + P[ye]
                valortoa = valortoa + V[ye]
                
        Pesotoa.append(pesotoa)
        Valortoa.append(valortoa)
    
    for xi in range(0, poblacion, 1):
        s = ' '
        for yi in range(0, elementos, 1):
            s = s + str(P1[xi][yi])
        print(s)
          
    print('pesototal', Pesotoa)
    print('valortotal', Valortoa)
    
    Mejor = []
    Mejor = Valortoa[:]
    for xcom2 in range(0, len(Valortoa), 1):
        b = 0
        for ycom2 in range(0, len(Valortoa), 1):
            if ycom2 != len(Valortoa) - 1:
                if Mejor[ycom2] > Mejor[ycom2 + 1]:
                    b = Mejor[ycom2]
                    Mejor[ycom2] = Mejor[ycom2 + 1]
                    Mejor[ycom2 + 1] = b
                
    li = 0
    while li == 0:
        hu = Valortoa.index(Mejor[-1])
        
        if Pesotoa[hu] < capacidad:
            op = Mejor[-1]
            li = li + 1
        else:
            Mejor = Mejor[0:len(Mejor) - 1]
        print('mejor de la generacion', Mejor)
    rem = Valortoa.index(op)
    for xex in range(0, poblacion, 1):
        for yex in range(0, elementos, 1):
            if xex == rem:
                Pasar.append(P1[xex][yex])
    i = 0
    while (i < poblacion):
        k = 2
        Competencia = []
        for xt in range(0, k, 1):
            k1 = random.randint(0, poblacion - 1)
            re = Valortoa[k1]
            Competencia.append(re)
         
        al = 0
        for xc in range (0, len(Competencia), 1):
            if (Competencia[xc] > al):
                al = Competencia[xc]
        jj = Valortoa.index(al)
        
        if Pesotoa[jj] < capacidad:
            Piscina.append(al)
            i = i + 1
    print('esta es la piscina', Piscina)
    
    return Pasar

# Función para realizar la recombinación de individuos
def recombinacion():
    for xen in range(0, poblacion, 1):
        di = Valortoa.index(Piscina[xen])
        Posiciones.append(di)
    u = 0
    
    while u < poblacion:
        antespadre = []
        antesmadre = []
        despuespadre = []
        despuesmadre = []
        hijo = []
        hija = []
        puntodequiebre = random.randint(1, elementos - 1)
        
        ptq = 0
        for xt1 in range(0, poblacion, 1):
            for yt1 in range(0, elementos, 1):
                if xt1 == Posiciones[ptq]:
                    if yt1 < puntodequiebre:
                        antespadre.append(P1[xt1][yt1])
                    else:
                        despuespadre.append(P1[xt1][yt1])
        ptq2 = 1
        for xt2 in range(0, poblacion, 1):
            for yt2 in range(0, elementos, 1):
                if xt2 == Posiciones[ptq]:
                    if yt2 < puntodequiebre:
                        antesmadre.append(P1[xt2][yt2])
                    else:
                        despuesmadre.append(P1[xt2][yt2])
        p = 0.7
        k3 = random.random()
        if k3 < p:
            hijo = hijo + antespadre
            hijo = hijo + despuesmadre
            hija = hija + antesmadre
            hija = hija + despuespadre
            
            for xt3 in range(0, poblacion, 1):
                for yt3 in range(0, elementos, 1):
                    if xt3 == ptq:
                        P1[xt3][yt3] = hijo[yt3]
                
            for xt4 in range(0, poblacion, 1):
                for yt4 in range(0, elementos, 1):
                    if xt4 == ptq2:
                        P1[xt4][yt4] = hija[yt4]
        ptq = ptq + 2
        ptq2 = ptq2 + 2
        u = u + 2

# Función para realizar la mutación de individuos
def mutacion(Pasar):
    JJ = 1 / elementos
    for xz in range(0, poblacion, 1):
        for yz in range(0, elementos, 1):
            JJJ = random.random()
            if JJJ < JJ:
                if P1[xz][yz] == 0:
                    P1[xz][yz] = 1
                else:
                    P1[xz][yz] = 0
    print('nueva generacion', P1)
    Pesotoa = []
    Valortoa = []
    for xe in range(0, poblacion, 1):
        e = elementos
        pesotoa = 0
        valortoa = 0
        for ye in range(0, elementos, 1):
            if P[ye] > capacidad:
                P[ye] = 0
                V[ye] = 0
            if P1[xe][ye] == 1:
                pesotoa = pesotoa + P[ye]
                valortoa = valortoa + V[ye]
                
        Pesotoa.append(pesotoa)
        Valortoa.append(valortoa)            
                            
    Peor = []
    Peor = Valortoa[:]
    for xcom2 in range(0, len(Valortoa), 1):
        b = 0
        for ycom2 in range(0, len(Valortoa), 1):
            if ycom2 != len(Valortoa) - 1:
                if Peor[ycom2] > Peor[ycom2 + 1]:
                    b = Peor[ycom2]
                    Peor[ycom2] = Peor[ycom2 + 1]
                    Peor[ycom2 + 1] = b
    el = Valortoa.index(Peor[0])
    
    print('ANTESPOBLACION', P1)    
    for xel in range(0, poblacion, 1):
        for yel in range(0, elementos, 1):
            if xel == el:
                P1[xel][yel] = Pasar[yel]
    print('Mejor individuo', Pasar)
    print('DESPUESPOBLACION', P1)
    salir = 0
    pesofinal = 0
    for yf in range(0, elementos, 1):
        if P[yf] > capacidad:
            P[ye] = 0
            V[ye] = 0
        if Pasar[yf] == 1:
            pesofinal = pesofinal + P[yf]
            salir = salir + V[yf]
    print('peso final', pesofinal)
    print('valor final', salir)
    return salir

# Llamada a las funciones y generación de gráficas
poblacioninicial()
op = decodificadora()

con = 0
b = 0
graficas = []
equis = []
for xhol in range(0, 25, 1):
    Valortoa = []
    Pesotoa = []
    Posiciones = []
    Piscina = []
    Pasar = []
    Pasar = seleccion()
    recombinacion()
    f = mutacion(Pasar)
    graficas.append(f)
    equis.append(xhol)
    con = con + 1

plt.plot(equis, graficas)
plt.show()
