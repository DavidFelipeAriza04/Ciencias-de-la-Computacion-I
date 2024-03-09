import os


def mergeSort(lista, ciclos, pasos):
    if len(lista) > 1:
        listaIzq = lista[: len(lista) // 2]
        listaDer = lista[len(lista) // 2 :]
        pasos += 2

        # Recursion
        ciclos, pasos = mergeSort(listaIzq, ciclos, pasos)
        ciclos, pasos = mergeSort(listaDer, ciclos, pasos)

        # Combinar
        i = 0  # Indice lista izq
        j = 0  # Indice lista der
        k = 0  # Indice lista organizada
        pasos += 3
        while i < len(listaIzq) and j < len(listaDer):
            pasos += 2
            if listaIzq[i] < listaDer[j]:
                lista[k] = listaIzq[i]
                i += 1
                pasos += 3
            else:
                lista[k] = listaDer[j]
                j += 1
                pasos += 2
            k += 1
            pasos += 1
            ciclos += 1
        pasos += 2
        while i < len(listaIzq):
            lista[k] = listaIzq[i]
            i += 1
            k += 1
            pasos += 4
            ciclos += 1
        pasos += 1
        while j < len(listaDer):
            lista[k] = listaDer[j]
            j += 1
            k += 1
            pasos += 3
            ciclos += 1
        pasos += 1
    pasos += 1
    return ciclos, pasos


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

ciclos = 0
pasos = 0
ciclos, pasos = mergeSort(lista_numeros, ciclos, pasos)
print("Lista Ordenada: ")
print(lista_numeros)
print(f"Ciclos algortimo MergerSort: {ciclos}")
print(f"Pasos algortimo MergerSort: {pasos}")
