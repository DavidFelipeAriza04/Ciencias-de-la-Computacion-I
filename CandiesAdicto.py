def MayorCantidadDulces(lista):
    ListaSumas = [lista[0], lista[1]]
    n1 = 0
    n2 = 0
    if len(lista) <= 2:
        n1 = lista[0]
        n2 = lista[1]
        return n1 if n1 > n2 else n2
    else:
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


def DividirMatriz(x, y, matriz):
    ListaSumas=[]
    for i in range(x):
        # print(matriz[i])
        ListaSumas.append(MayorCantidadDulces(matriz[i]))
    return MayorCantidadDulces(ListaSumas)


lista = [10, 2, 30, 21, 17, 4]
matriz = [
    [1, 8, 2, 1, 9],
    [1, 7, 3, 5, 2],
    [1, 2, 10, 3, 10],
    [8, 4, 7, 9, 1],
    [7, 1, 3, 1, 6],
]
# print(MayorCantidadDulces(lista))
print(f"La mayor cantidad de dulces que se pueden obtener de la matriz: {matriz} es {DividirMatriz(5, 5, matriz)}")