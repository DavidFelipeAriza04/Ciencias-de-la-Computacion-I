
# BURBUJA OPTIMIZADO
def Burbuja (lista_numeros):
    contador_pasos = 0
    contador_ciclos = 0
    for i in range(len(lista_numeros)):
        for j in range(i+1,len(lista_numeros)):
            contador_ciclos+=1
            if lista_numeros[i]>lista_numeros[j]:
                temp = lista_numeros[i]
                lista_numeros[i] = lista_numeros[j]
                lista_numeros[j]=temp
                contador_pasos +=3
            contador_pasos+=3
        contador_pasos+=4
    contador_pasos+=4


    print("Ciclos Algoritmo Burbuja: "+str(contador_ciclos))
    print("Pasos Algoritmo Burbuja: "+str(contador_pasos)+"\n")

# BURBUJA TRADICIONAL
def Burbuja2 (lista_numeros):
    contador_pasos = 0
    contador_ciclos = 0
    for i in range(len(lista_numeros)-1):
        for j in range(len(lista_numeros)-1):
            contador_ciclos+=1
            if lista_numeros[j]>lista_numeros[j+1]:
                temp = lista_numeros[j]
                lista_numeros[j] = lista_numeros[j+1]
                lista_numeros[j+1]=temp
                contador_pasos +=3
            contador_pasos+=3
        contador_pasos+=4
    contador_pasos+=2


    print("Ciclos Algoritmo Burbuja Tradicional: "+str(contador_ciclos))
    print("Pasos Algoritmo Burbuja Tradicional: "+str(contador_pasos)+"\n")

# SELECCION
def Seleccion (lista_numeros):
    contador_pasos = 0
    contador_ciclos = 0
    for i in range(len(lista_numeros)-1):
        menor = lista_numeros[i]
        posicion = i
        for j in range(i+1, len(lista_numeros)):
            if lista_numeros[j]<menor:
                menor = lista_numeros[j]
                posicion = j
                contador_pasos+=2
            contador_ciclos = contador_ciclos+1
            contador_pasos+=3
        temp = lista_numeros[i]
        lista_numeros[i]=menor
        lista_numeros[posicion]=temp
        contador_pasos +=3
    contador_pasos+=2

    print("Ciclos Algoritmo Seleccion: "+str(contador_ciclos))
    print("Pasos Algoritmo Seleccion: "+str(contador_pasos))

lista_numeros = []
with open("pruebas/"+input("Ingrese el nombre del archivo pls: ")+".txt","r") as archivo:
    for linea in archivo:
        lista_numeros.append(int(linea))


Burbuja(lista_numeros)
Burbuja2(lista_numeros)
Seleccion(lista_numeros)