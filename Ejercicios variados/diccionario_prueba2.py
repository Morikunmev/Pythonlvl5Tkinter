# Supongamos que tienes un diccionario de colores y una lista de grados asociados a cada color
colores = {"rojo": "FF0000", "verde": "00FF00", "azul": "0000FF"}
grados = [20, 40, 60]

# Iterar sobre los elementos del diccionario utilizando enumerate y acceder a los grados por índice
for i, color in enumerate(colores.keys()):
    grado = grados[i]
    print(f"El color {color} tiene un grado de {grado}.")

print("Iteracion sobre las llaves")
for i, color in enumerate(colores.keys()):
    print(i,color)
print("Iteracion sobre los items")
for i, color in enumerate(colores.items()):
    print(i,color)
