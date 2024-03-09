import os


def Amontonar2(lista, len, pos, ciclos):
    ciclos += 1
    izquierda = 2 * pos + 1  # left = 2*i + 1
    derecha = 2 * pos + 2  # right = 2*i + 2
    # print("Padre "+str(lista[pos]))
    if izquierda < len:
        # print("Hijo izquierda de "+str(lista[pos])+" es "+str(lista[izquierda]))
        ciclos = Amontonar2(lista, len, izquierda, ciclos)
        if derecha < len:
            # print("Hijo derecha de "+str(lista[pos])+" es "+str(lista[derecha]))
            ciclos = Amontonar2(lista, len, derecha, ciclos)
            if lista[izquierda] > lista[pos] and lista[izquierda] > lista[derecha]:
                # print("Cambiando "+str(lista[pos])+" y "+str(lista[izquierda]))
                (lista[pos], lista[izquierda]) = (lista[izquierda], lista[pos])
                # print(lista)
            elif lista[derecha] > lista[pos] and lista[derecha] > lista[izquierda]:
                # print("Cambiando "+str(lista[pos])+" y "+str(lista[derecha]))
                (lista[pos], lista[derecha]) = (lista[derecha], lista[pos])
                # print(lista)
        else:
            # print(str(lista[pos])+" No tiene hijo derecha")
            if lista[izquierda] > lista[pos]:
                # print("Cmabiando "+str(lista[pos])+" y "+str(lista[izquierda]))
                (lista[pos], lista[izquierda]) = (lista[izquierda], lista[pos])
    else:
        # print(str(lista[pos])+" No tiene hijo izquierda")
        pass
    return ciclos


# lista_numeros = []
# with open(
#     os.path.abspath(os.getcwd())
#     + "\\algoritmos_ordenamiento\\pruebas\\"
#     + input("Ingrese el nombre del archivo: ")
#     + ".txt",
#     "r",
# ) as archivo:
#     for linea in archivo:
#         lista_numeros.append(int(linea))
lista = [4, 9, 3, 2, 5, 10, 11, 24, 12, 90]


ciclos = 0
for i in range(len(lista)):
    ciclos = Amontonar2(lista, len(lista) - i, 0, ciclos)
    print(len(lista) - i)
    (lista[0], lista[len(lista) - 1 - i]) = (lista[len(lista) - 1 - i], lista[0])
    # print(lista)

print("Ciclos algoritmo HeapSort " + str(ciclos))
print(lista)
