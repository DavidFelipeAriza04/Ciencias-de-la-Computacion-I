def amontonar(lista, n, i):
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
        amontonar(lista, n, mayor)
    else:
        print("No hay cambio")
        print(lista)
# The main function to sort an array of given size
def heapSort(lista):
    n = len(lista)
    # Build a maxheap.
    # Since last parent will be at (n//2) we can start at that location.
    print(n)
    print(n // 2)
    for i in range(n // 2 -1, -1, -1):
        print("Posicion "+str(i+1))
        amontonar(lista, n, i)
    # One by one extract elements
    for i in range(n - 1, 0, -1):
        print("Cambiando "+str(lista[i])+" y "+str(lista[0]))
        (lista[i], lista[0]) = (lista[0], lista[i])  # swap
        print(lista)
        amontonar(lista, i, 0)
# Driver code to test above

lista = []
with open(
    "pruebas/" + input("Ingrese el nombre del archivo: ") + ".txt", "r"
) as archivo:
    for linea in archivo:
        lista.append(int(linea))

heapSort(lista)
print("Sorted array is")
print(lista)
