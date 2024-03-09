def MayorCantidadDulces(lista):
    if len(lista) ==2:
        n1 = lista[0]
        n2 = lista[1]
        return n1 if n1 > n2 else n2
    if len(lista) == 1:
        return lista[0]
    if len(lista) == 0:
        return 0
    else:
        ListaSumas = [lista[0], lista[1]]
        n1 = 0
        n2 = 0
        for i in range(2, len(lista)):
            if i - 3 >= 0:
                n1 = lista[i] + ListaSumas[i - 3]
            if i - 2 >= 0:
                n2 = lista[i] + ListaSumas[i - 2]
            ListaSumas.append(n1 if n1 > n2 else n2)
            # print(ListaSumas)
    return (
        ListaSumas[len(ListaSumas) - 1]
        if ListaSumas[len(ListaSumas) - 1] > ListaSumas[len(ListaSumas) - 2]
        else ListaSumas[len(ListaSumas) - 2]
    )


def DividirMatriz(x, matriz):
    ListaSumas = []
    for i in range(x):
        ListaSumas.append(MayorCantidadDulces(matriz[i]))
    return MayorCantidadDulces(ListaSumas)

# x, y = 5, 5
matriz = [
    [1, 8, 2, 1, 9],
    [1, 7, 3, 5, 2],
    [1, 2, 10, 3, 10],
    [8, 4, 7, 9, 1],
    [7, 1, 3, 1, 6],
]


matriz2 = [
    [10, 1, 1, 10],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [10, 1, 1, 10]
]
# x, y = 4, 4

matriz3 = [
    [9, 10, 2, 7],
    [5, 1, 1, 5]
]
x, y = 2, 4

matriz4 = []
# x, y = 0, 0


def MostrarMatriz(matriz):
    for fila in matriz:
        for valor in fila:
            print("\t", valor, end="")
        print()


print(f"Para la matriz:")
MostrarMatriz(matriz3)
print(
    f"La mayor cantidad de dulces que se pueden obtener es {DividirMatriz(x, matriz3)}"
)
