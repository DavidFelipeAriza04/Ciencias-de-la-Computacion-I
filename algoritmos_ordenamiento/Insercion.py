import os


def insercion(lista):
    ciclos = 0
    pasos = 0
    for i in range(1, len(lista)):
        for j in range(i, 0, -1):
            if lista[j - 1] > lista[j]:
                aux = lista[j]
                lista[j] = lista[j - 1]
                lista[j - 1] = aux
                pasos += 3
            ciclos += 1
            pasos += 1
        pasos += 2
    pasos += 2
    print("Lista Organizada")
    print(lista_numeros)
    print("Ciclos Algoritmo Insercion: " + str(ciclos))
    print("Pasos Algoritmo Insercion: " + str(pasos))


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

# Programa Principal
insercion(lista_numeros)
