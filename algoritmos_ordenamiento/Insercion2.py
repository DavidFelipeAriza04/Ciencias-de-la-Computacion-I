import os


def Insercion(lista_numeros):
    contador_ciclos = 0
    contador_pasos = 0
    for i in range(1, len(lista_numeros)):
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
    print("Lista Organizada")
    print(lista_numeros)
    print("Ciclos Algoritmo Insercion: " + str(contador_ciclos))
    print("Pasos Algoritmo Insercion: " + str(contador_pasos))


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


Insercion(lista_numeros)
