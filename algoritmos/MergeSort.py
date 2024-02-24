def mergeSort(lista, ciclos):
    if len(lista) > 1:
        # print("Lista Completa: " + str(lista))
        listaIzq = lista[: len(lista) // 2]
        # print("Lista izq: " + str(listaIzq))
        listaDer = lista[len(lista) // 2 :]
        # print("Lista der: " + str(listaDer))

        # Recursion
        ciclos = mergeSort(listaIzq, ciclos)
        ciclos = mergeSort(listaDer, ciclos)

        # Combinar
        i = 0  # Indice lista izq
        j = 0  # Indice lista der
        k = 0  # Indice lista organizada
        while i < len(listaIzq) and j < len(listaDer):
            # print(f'Comparando {listaIzq[i]} y {listaDer[j]}')
            if listaIzq[i] < listaDer[j]:
                # print(f'{listaIzq[i]} es menor que {listaDer[j]}')
                # print(f'Agregando Izq {listaIzq[i]}')
                lista[k] = listaIzq[i]
                i += 1
                # print(f'La lista es {lista}')
            else:
                # print(f'{listaIzq[i]} es mayor que {listaDer[j]}')
                # (f'Agregando Der {listaDer[j]}')
                lista[k] = listaDer[j]
                j += 1
                # print(f'La lista es {lista}')
            k += 1
            ciclos += 1
        while i < len(listaIzq):
            # print(f'Agregando {listaIzq[i]}')
            lista[k] = listaIzq[i]
            i += 1
            k += 1
            # print(f'La lista es {lista}')
            ciclos += 1

        while j < len(listaDer):
            lista[k] = listaDer[j]
            f"Agregando {listaDer[j]}"
            j += 1
            k += 1
            # print(f'La lista es {lista}')
            ciclos += 1
    return ciclos


lista = []
with open("pruebas/" + input("Ingrese el nombre del archivo: ") + ".txt", "r") as archivo:
    for linea in archivo:
        lista.append(int(linea))

ciclos = 0
ciclos = mergeSort(lista, ciclos)
print("Lista Ordenada: ")
print(lista)
print(f'Ciclos algortimo MergerSort: {ciclos}')
