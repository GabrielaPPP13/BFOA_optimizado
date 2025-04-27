from copy import copy
from multiprocessing import Manager, Pool
import time
from bacteria import bacteria
import numpy
import copy

from fastaReader import fastaReader

if __name__ == "__main__":
    numeroDeBacterias = 4
    numRandomBacteria = 1
    iteraciones = 3
    tumbo = 2                                             #numero de gaps a insertar 
    nado = 3
    secuencias = list()
    
    secuencias = fastaReader().seqs
    names = fastaReader().names
    
        
    
  
         
    
    
    #hace todas las secuencias listas de caracteres
    for i in range(len(secuencias)):
        #elimina saltos de linea
        secuencias[i] = list(secuencias[i])
        

    

    globalNFE = 0                            #numero de evaluaciones de la funcion objetivo
    
    

    dAttr= 0.001 #0.1
    wAttr= 0.00002 #0.2
    hRep=dAttr
    wRep= .00001    #10
    
   

  
    
    manager = Manager()
    numSec = len(secuencias)
    print("numSec: ", numSec)
    
    poblacion = manager.list(range(numeroDeBacterias))
    names = manager.list(names)
    NFE = manager.list(range(numeroDeBacterias))
    
    
    # print(secuencias)



    def poblacionInicial():    #lineal
        #crece la poblacion al numero de bacterias
        for i in range(numeroDeBacterias):
            bacterium = []
            for j in range(numSec):
                bacterium.append(secuencias[j])
            poblacion[i] = list(bacterium)
           
   

    operadorBacterial = bacteria(numeroDeBacterias)    
    veryBest = [None, None, None] #indice, fitness, secuencias
    
    #registra el tiempo de inicio
    start_time = time.time()
    
    print("poblacion inicial ...")
    poblacionInicial() 


    for it in range(iteraciones):
        print(f"Iteración {it+1} - Cuadrando población ...")
        operadorBacterial.cuadra(numSec, poblacion)

        print("Creando granLista de Pares ...")
        operadorBacterial.creaGranListaPares(poblacion)

        print("Evaluando Blosum ...")
        operadorBacterial.evaluaBlosum()

        print("Creando Tablas de Atracción y Repulsión ...")
        operadorBacterial.creaTablasAtractRepel(poblacion, dAttr, wAttr, hRep, wRep)

        operadorBacterial.creaTablaInteraction()
        print("Tabla de Interacción creada")

        operadorBacterial.creaTablaFitness()
        print("Tabla de Fitness creada")

        globalNFE += operadorBacterial.getNFE()
        bestIdx, bestFitness = operadorBacterial.obtieneBest(globalNFE)

        # Aplica tumbo inteligente hacia la mejor bacteria
        print("Aplicando Tumbo guiado por bestIdx ...")
        operadorBacterial.tumbo(numSec, poblacion, tumbo, bestBacteriaIdx=bestIdx)

        if veryBest[0] is None or bestFitness > veryBest[1]:
            veryBest[0] = bestIdx
            veryBest[1] = bestFitness
            veryBest[2] = copy.deepcopy(poblacion[bestIdx])

        operadorBacterial.replaceWorst(poblacion, veryBest[0])
        operadorBacterial.resetListas(numeroDeBacterias)
    
    print("--- %s seconds ---" % (time.time() - start_time))

    # print("\n--- MATRIZ FINAL DE LA POBLACIÓN ---")
    # for i in range(numeroDeBacterias):
    #     print(f"\nBacteria {i+1}:")
    #     for secuencia in poblacion[i]:
    #         print("".join(secuencia))

    print("\n--- MEJOR BACTERIA FINAL ---")
    for secuencia in veryBest[2]:
        print("".join(secuencia))




    