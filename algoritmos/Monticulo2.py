def amontonar(lista, n, i, ciclos):
    ciclos+=1
    mayor = i  # Initialize largest as root
    izquierda = 2 * i + 1  # left = 2*i + 1
    derecha = 2 * i + 2  # right = 2*i + 2
    print("Mayor Antes " + str(lista[mayor]))
    if izquierda < n:
        print("Izq " + str(lista[izquierda]))
    else:
        print("Izq No hay hijo")
    if derecha < n:
        print("Der " + str(lista[derecha]))
    else:
        print("Der No hay hijo")
    # See if left child of root exists and is greater than root
    if izquierda < n and lista[i] < lista[izquierda]:
        mayor = izquierda
    # See if right child of root exists and is greater than root
    if derecha < n and lista[mayor] < lista[derecha]:
        mayor = derecha
    # Change root, if needed
    print("Mayor Despues " + str(lista[mayor]))
    if mayor != i:
        print("Cambiando " + str(lista[i])+ " y "+str(lista[mayor]))
        (lista[i], lista[mayor]) = (lista[mayor], lista[i])  # swap
        # Heapify the root.
        print(lista)
        amontonar(lista, n, mayor,ciclos)
    else:
        print("No hay cambio")
        print(lista)
# The main function to sort an array of given size
def heapSort(lista,ciclos):
    n = len(lista)
    # Build a maxheap.
    # Since last parent will be at (n//2) we can start at that location.
    print(n)
    print(n // 2)
    for i in range(n-1, -1, -1):
        print("Posicion "+str(i))
        amontonar(lista, n, i, ciclos)
    # One by one extract elements
    for i in range(n - 1, 0, -1):
        print("Posicion "+str(i))
        print(lista)
        amontonar(lista, i, 0,ciclos)
        print("Cambiando "+str(lista[i])+" y "+str(lista[0]))
        (lista[i], lista[0]) = (lista[0], lista[i])  # swap
    print(ciclos)
# lista = []
# with open(
#     "pruebas/" + input("Ingrese el nombre del archivo: ") + ".txt", "r"
# ) as archivo:
#     for linea in archivo:
#         lista.append(int(linea))

lista=[4,9,3,2]
# ciclos=0
# heapSort(lista,ciclos)
# print("Sorted array is")
# print(lista)

def Amontonar2(lista, len, pos, ciclos):
    ciclos+=1
    print("Ciclos "+str(ciclos))
    izquierda = 2 * pos + 1  # left = 2*i + 1
    derecha = 2 * pos + 2  # right = 2*i + 2
    # print("Padre "+str(lista[pos]))
    if(izquierda<len):
        # print("Hijo izquierda de "+str(lista[pos])+" es "+str(lista[izquierda]))
        ciclos = Amontonar2(lista,len,izquierda,ciclos)
        if(derecha<len):
            # print("Hijo derecha de "+str(lista[pos])+" es "+str(lista[derecha]))
            ciclos = Amontonar2(lista,len,derecha,ciclos)
            if(lista[izquierda]>lista[pos] and lista[izquierda]>lista[derecha]):
                # print("Cambiando "+str(lista[pos])+" y "+str(lista[izquierda]))
                (lista[pos],lista[izquierda])=(lista[izquierda],lista[pos])
                # print(lista)
            elif (lista[derecha]>lista[pos] and lista[derecha]>lista[izquierda]):
                # print("Cambiando "+str(lista[pos])+" y "+str(lista[derecha]))
                (lista[pos],lista[derecha])=(lista[derecha],lista[pos])
                # print(lista)
        else:
            # print(str(lista[pos])+" No tiene hijo derecha")
            if(lista[izquierda]>lista[pos]):
                # print("Cmabiando "+str(lista[pos])+" y "+str(lista[izquierda]))
                (lista[pos],lista[izquierda])=(lista[izquierda],lista[pos])
    else:
        # print(str(lista[pos])+" No tiene hijo izquierda")
        pass
    return ciclos

ciclos=0
# for i in range(len(lista)):
#     ciclos = Amontonar2(lista,len(lista)-i,0,ciclos)
#     # print("Cambiando "+str(lista[0])+" y "+str(lista[len(lista)-1-i]))
#     (lista[0],lista[len(lista)-1-i])=(lista[len(lista)-1-i],lista[0])
    # print(lista)
# Amontonar2(lista,len(lista)-1,0)
# (lista[0],lista[len(lista)-1])=(lista[len(lista)-1],lista[0])
ciclos = Amontonar2(lista,len(lista),0,ciclos)
print(ciclos)