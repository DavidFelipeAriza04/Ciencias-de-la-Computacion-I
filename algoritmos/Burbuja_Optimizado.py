
# BURBUJA OPTIMIZADO
def BurbujaOptimizado(lista_numeros):
    contador_pasos = 0
    contador_ciclos = 0
    for i in range(len(lista_numeros)-1):
        for j in range(len(lista_numeros)-i-1):
            contador_ciclos+=1
            if lista_numeros[j]>lista_numeros[j+1]:
                temp = lista_numeros[j]
                lista_numeros[j] = lista_numeros[j+1]
                lista_numeros[j+1]=temp
                contador_pasos +=3
            contador_pasos+=3
        contador_pasos+=4
    contador_pasos+=2


    print("\nCiclos Algoritmo Burbuja Optimizado: "+str(contador_ciclos))
    print("Pasos Algoritmo Burbuja Optimizado: "+str(contador_pasos)+"\n")



lista_numeros = []
#LECTURA DEL ARCHIVO DE PRUEBA
with open("pruebas/"+input("Ingrese el nombre del archivo: ")+".txt","r") as archivo:
    for linea in archivo:
        lista_numeros.append(int(linea))

BurbujaOptimizado(lista_numeros)
print(lista_numeros)