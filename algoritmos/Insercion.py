def Insercion(lista_numeros):
    contador_ciclos = 0
    contador_pasos = 0
    ciclo = False
    for i in range(len(lista_numeros)):
        aux = lista_numeros[i]
        while lista_numeros[i] < lista_numeros[i - 1] and i != 0:
            lista_numeros[i] = lista_numeros[i - 1]
            lista_numeros[i - 1] = aux
            i -= 1
            contador_pasos += 3
            contador_ciclos += 1
            ciclo = True
        contador_pasos += 3
        if ciclo == False:
            contador_ciclos += 1
    contador_pasos += 2
    print("Ciclos Algoritmo Seleccion: " + str(contador_ciclos))
    print("Pasos Algoritmo Seleccion: " + str(contador_pasos))


lista_numeros = []
lista_numeros2 = []
with open(
    "pruebas/" + input("Ingrese el nombre del archivo: ") + ".txt", "r"
) as archivo:
    for linea in archivo:
        lista_numeros.append(int(linea))
        lista_numeros2.append(int(linea))


Insercion(lista_numeros2)
# print(lista_numeros)

ciclos = 0
pasos = 0
ciclo = False
for i in range(1, len(lista_numeros)):
    aux = lista_numeros[i]
    j = i - 1
    while j >= 0 and lista_numeros[j] > aux:
        lista_numeros[j + 1] = lista_numeros[j]
        j -= 1
        ciclos += 1
        pasos += 2
        ciclo = True
    if ciclo == False:
        ciclos += 1
    lista_numeros[j + 1] = aux
    pasos += 5
pasos += 2

print(ciclos)
print(pasos)
print(lista_numeros)
