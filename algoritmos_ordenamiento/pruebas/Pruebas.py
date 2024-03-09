import random
archivo = open("pruebas\prueba1.txt","w")
for i in range (100):
    numero = random.randint(0,1000)
    archivo.write(str(numero)+"\n")


with open("pruebas\prueba1.txt","r") as archivo:
    numero=archivo.readline()
    print(numero)


