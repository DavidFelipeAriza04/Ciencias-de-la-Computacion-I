import os


# BURBUJA OPTIMIZADO
def BurbujaOptimizado(lista_numeros):
    contador_pasos = 0
    contador_ciclos = 0
    for i in range(len(lista_numeros) - 1):
        for j in range(len(lista_numeros) - i - 1):
            contador_ciclos += 1
            if lista_numeros[j] > lista_numeros[j + 1]:
                temp = lista_numeros[j]
                lista_numeros[j] = lista_numeros[j + 1]
                lista_numeros[j + 1] = temp
                contador_pasos += 3
            contador_pasos += 3
        contador_pasos += 4
    contador_pasos += 2

    print("\nCiclos Algoritmo Burbuja Optimizado: " + str(contador_ciclos))
    print("Pasos Algoritmo Burbuja Optimizado: " + str(contador_pasos) + "\n")


lista_numeros = []
with open(
    os.path.abspath(os.getcwd())
    + "\\algoritmos_ordenamiento\\pruebas\\"
    + input("Ingrese el nombre del archivo: ")
    + ".txt",
    "r",
) as archivo:
    for linea in archivo:
        lista_numeros.append(int(linea))

print("Lista Desorganizada:\n")
print(lista_numeros)
print("\n")
BurbujaOptimizado(lista_numeros)
print("Lista Organizada:\n")
print(lista_numeros)
