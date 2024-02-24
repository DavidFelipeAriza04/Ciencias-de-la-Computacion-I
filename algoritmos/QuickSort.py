def QuickSort(lista, posicionIncio, posicionFin, posicionPivote):
    print("Lista:")
    # print(posicionFin)
    for i in range(posicionIncio, posicionFin):
        # print(i)
        print(lista[i])
    pivote = lista[posicionIncio]
    posicionPivote = posicionPivote
    posicionJ = posicionFin - 1
    print(
        "Posicion pivote: "
        + str(posicionPivote)
        + " Pivote: "
        + str(lista[posicionPivote])
    )
    print("Posicion fin: " + str(posicionJ))
    for i in range(posicionIncio, posicionFin):
        print(
            "Posicion pivote: "
            + str(posicionPivote)
            + " Pivote: "
            + str(lista[posicionPivote])
        )
        print("Posicion i: " + str(i) + " Numero: " + str(lista[i]))
        if i == posicionJ and lista[i] < pivote:
            print(
                "Cambiando pivote "
                + str(lista[posicionPivote])
                + " por "
                + str(lista[i])
            )
            (lista[posicionPivote], lista[i]) = (lista[i], lista[posicionPivote])
            print(lista)
            QuickSort(lista, posicionPivote, posicionJ, posicionPivote)
            QuickSort(lista, posicionJ + 1, posicionFin, posicionJ + 1)
        elif i == posicionJ:
            print("Misma Posicion")
        elif lista[i] > pivote:
            print("Guardado " + str(lista[i]))
            for j in range(posicionFin - 1, posicionIncio, -1):
                print("Posicion j: " + str(j) + " Numero: " + str(lista[j]))
                if lista[j] < pivote:
                    print("Guardado " + str(lista[j]))
                    print("Cambiando " + str(lista[i]) + " por " + str(lista[j]))
                    (lista[i], lista[j]) = (lista[j], lista[i])
                    print(lista)
                    j -= 1
                    posicionJ = j
                    print("Posicion j: " + str(j) + " Numero: " + str(lista[j]))
                    break
                elif i == j:
                    print(
                        "Cambiando pivote "
                        + str(lista[posicionPivote])
                        + " por "
                        + str(lista[i])
                    )
                    (lista[posicionPivote], lista[i]) = (
                        lista[i],
                        lista[posicionPivote],
                    )
                    print(lista)
                    QuickSort(lista, posicionPivote, posicionJ, posicionPivote)
                    QuickSort(lista, posicionJ + 1, posicionFin, posicionJ + 1)
                    break


def dividirLista(lista, ciclos):
    pivote = lista[0]
    listaMenores = []
    listaMayores = []
    for i in range(1, len(lista)):
        ciclos += 1
        print(ciclos)
        if lista[i] < pivote:
            listaMenores.append(lista[i])
        else:
            listaMayores.append(lista[i])
    print(ciclos)
    return listaMenores, pivote, listaMayores


def Quick_Sort(lista, ciclos):
    if len(lista) < 2:
        return lista
    listaMenores, pivote, listaMayores = dividirLista(lista, ciclos)
    return (
        Quick_Sort(listaMenores, ciclos) + [pivote] + Quick_Sort(listaMayores, ciclos)
    )


lista = [10, 25, 7, 3, 9, 6, 15, 5, 50]
# QuickSort(lista, 0, len(lista), 0)
ciclos = 0
lista = Quick_Sort(lista, ciclos)
print(lista)
print(ciclos)