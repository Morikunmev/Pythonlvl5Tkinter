colores = {"Canape": "blue", "Mini-pizzas": "green", "Mini-empanadas": "yellow"}
for clave in colores.keys():
    print(clave)
print("-"*20)

colores = {"Canape": "blue", "Mini-pizzas": "green", "Mini-empanadas": "yellow"}
for clave, valor in colores.items():
    print(f"Clave: {clave}, Valor: {valor}")
