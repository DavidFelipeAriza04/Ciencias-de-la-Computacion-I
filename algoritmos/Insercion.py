def Insercion(lista_numeros):
    contador_ciclos = 0
    contador_pasos = 0
    for i in range(1,len(lista_numeros)):
        aux = lista_numeros[i]
        while lista_numeros[i] < lista_numeros[i - 1] and i != 0:
            lista_numeros[i] = lista_numeros[i - 1]
            lista_numeros[i - 1] = aux
            i -= 1
            contador_pasos += 3
            contador_ciclos += 1
        contador_pasos += 3
        contador_ciclos += 1
    contador_pasos += 2
    print("Ciclos Algoritmo Seleccion: " + str(contador_ciclos))
    print("Pasos Algoritmo Seleccion: " + str(contador_pasos))


lista_numeros = []
with open(
    "pruebas/" + input("Ingrese el nombre del archivo: ") + ".txt", "r") as archivo:
    for linea in archivo:
        lista_numeros.append(int(linea))


# Insercion(lista_numeros2)
# print(lista_numeros)

def insercion(lista):
    ciclos=0
    pasos=0
    for i in range(1,len(lista)):
        for j in range(i,0,-1):
            if(lista[j-1] > lista[j]):
                aux=lista[j];
                lista[j]=lista[j-1];
                lista[j-1]=aux;
                pasos+=3
            ciclos+=1
            pasos+=1
        pasos+=2
    pasos+=2
    print(lista)
    print(ciclos)
    print(pasos)

#Programa Principal
insercion(lista_numeros);