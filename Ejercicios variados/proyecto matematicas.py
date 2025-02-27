import random

# declaracion de variables y variables con lista

fila_a = []
fila_b = []
fila_c = []
juego = True
contador = 0

# creacion de barajas de cartas  y mezcla con funcion shuffle
mazo_cartas = list(range(1, 22))
random.shuffle(mazo_cartas)
print("Bienvenido al juego de las 21 cartas de Richard")
print("-" * 50)
print(mazo_cartas)
input("por favor, elija un numero y presione Enter: ")


# creacion de funcion de los tres mazos
def mazo_tres_cartas():
    global mazo_cartas

    for i in range(0, 21, 3):
        fila_a.append(mazo_cartas[i])
    for j in range(1, 21, 3):
        fila_b.append(mazo_cartas[j])
    for k in range(2, 21, 3):
        fila_c.append(mazo_cartas[k])
    mazo_cartas = []

    print("-" * 30)
    print("A: {}".format(fila_a))
    print("B: {}".format(fila_b))
    print("C: {}".format(fila_c))
    print("En que mazo esta su numero: A, B o C?")


# funcion de definicion del algoritmo de los 3 mazos segun la eleccion del usuario, sea a, b o c


def revolver_cartas(eleccion):
    global fila_a, fila_b, fila_c

    if eleccion == "A":
        for i in fila_b:
            mazo_cartas.append(i)
        for j in fila_a:
            mazo_cartas.append(j)
        for k in fila_c:
            mazo_cartas.append(k)

    if eleccion == "B":
        for i in fila_a:
            mazo_cartas.append(i)

        for j in fila_b:
            mazo_cartas.append(j)
        for k in fila_c:
            mazo_cartas.append(k)

    if eleccion == "C":
        for i in fila_b:
            mazo_cartas.append(i)
        for j in fila_c:
            mazo_cartas.append(j)
        for k in fila_a:
            mazo_cartas.append(k)

    fila_a, fila_b, fila_c = [], [], []


# funcion donde el usuario ingresa una letra "a" "b" o "c",
# se le agrega una condicion si el valor ingresado es que corresponde
# sino se vuelve a preguntar que ingrese la letra

def en_juego():
    eleccion_valida = ("A", "B", "C")
    eleccion = input("Ingrese la letra del mazo: ").upper()
    if eleccion in eleccion_valida:
        revolver_cartas(eleccion)
    else:
        print(f"{eleccion}: no es una letra de mazo valido")
        en_juego()


while juego:
    mazo_tres_cartas()
    en_juego()
    contador += 1
    if contador > 2:
        juego = False
        print("-" * 30)
        print("{} es tu numero!!!".format(mazo_cartas[10]))