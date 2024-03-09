import os


def Quick(lista, inicioLista, finLista, ciclos, pasos):
    i = inicioLista
    j = finLista
    pasos += 2
    if len(lista[inicioLista : finLista + 1]) <= 1:
        pasos += 1
        ciclos += 1
        return ciclos, pasos
    pivote = lista[inicioLista]
    pasos += 1

    while j > i:
        pasos += 1
        if pivote >= lista[j]:
            if i == j:
                pasos += 1
                break
            for n in range(i, len(lista)):
                pasos += 2
                ciclos += 1
                if n == j:
                    i = n
                    pasos += 2
                    break
                if pivote < lista[n]:
                    aux = lista[n]
                    lista[n] = lista[j]
                    lista[j] = aux
                    i = n
                    pasos += 5
                    break
        else:
            ciclos += 1
            j -= 1
            pasos += 1
    pasos += 1
    if pivote >= lista[j]:
        lista[inicioLista] = lista[j]
        lista[j] = pivote
        pasos += 5
    pasos += 1
    ciclos, pasos = Quick(lista, inicioLista, j - 1, ciclos, pasos)
    ciclos, pasos = Quick(lista, j + 1, finLista, ciclos, pasos)
    pasos += 2
    return ciclos, pasos


lista = []
with open(
    os.path.abspath(os.getcwd())
    + "\\algoritmos_ordenamiento\\pruebas\\"
    + input("Ingrese el nombre del archivo: ")
    + ".txt",
    "r",
) as archivo:
    for linea in archivo:
        lista.append(int(linea))

ciclos = 0
pasos = 0
ciclos, pasos = Quick(lista, 0, len(lista) - 1, ciclos, pasos)
print("Lista Ordenada: ")
print(lista)
print(f"Ciclos algortimo QuickSort: {ciclos}")
print(f"Pasos algortimo QuickSort: {pasos}")
