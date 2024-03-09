import os


def amontonar(lista, n, i, ciclos, pasos):
    ciclos += 1
    mayor = i
    izquierda = 2 * i + 1
    derecha = 2 * i + 2
    pasos += 3
    if izquierda < n and lista[i] < lista[izquierda]:
        mayor = izquierda
        pasos += 1
    pasos += 2
    if derecha < n and lista[mayor] < lista[derecha]:
        mayor = derecha
        pasos += 1
    pasos += 2
    if mayor != i:
        (lista[i], lista[mayor]) = (lista[mayor], lista[i])
        ciclos = amontonar(lista, n, mayor, ciclos, pasos)
        pasos += 3
    pasos += 1
    return ciclos


def OredenarHeap(lista, ciclos, pasos):

    n = len(lista)
    for i in range(n // 2 - 1, -1, -1):
        ciclos = amontonar(lista, n, i, ciclos, pasos)
        pasos += 3
    pasos += 2
    for i in range(n - 1, 0, -1):
        (lista[i], lista[0]) = (lista[0], lista[i])
        ciclos = amontonar(lista, i, 0, ciclos, pasos)
        pasos += 5
    pasos += 2
    pasos += 1
    print("Ciclos algoritmo HeapSort " + str(ciclos))
    print("Pasos algoritmo HeapSort " + str(pasos))


ciclos = 0
pasos = 0
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

OredenarHeap(lista_numeros, ciclos, pasos)
print("Lista Ordenada:")
print(lista_numeros)