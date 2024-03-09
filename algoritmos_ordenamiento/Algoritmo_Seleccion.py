import os


def Seleccion(lista_numeros):
    contador_pasos = 0
    contador_ciclos = 0
    for i in range(len(lista_numeros) - 1):
        menor = lista_numeros[i]
        posicion = i
        for j in range(i + 1, len(lista_numeros)):
            if lista_numeros[j] < menor:
                menor = lista_numeros[j]
                posicion = j
                contador_pasos += 2
            contador_ciclos += 1
            contador_pasos += 3
        temp = lista_numeros[i]
        lista_numeros[i] = menor
        lista_numeros[posicion] = temp
        contador_pasos += 9
    contador_pasos += 2

    print("Ciclos Algoritmo Seleccion: " + str(contador_ciclos))
    print("Pasos Algoritmo Seleccion: " + str(contador_pasos))


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

print("Lista Desorganizada:\n")
print(lista_numeros)
print("\n")
Seleccion(lista_numeros)
print("Lista Organizada:\n")
print(lista_numeros)
