# Ingrese una lista de compras: manzanas, plátanos, leche, pan
# Los productos en la lista de compras son: ['manzanas', 'plátanos', 'leche', 'pan']

# compras = input("Ingrese una lista de compras: ")
# productos = compras.split(", ")
# print(f"Los productos en la lista de compras son: {productos}")

# # Convertir la lista de compras en una tupla
# def convertir_lista_a_tupla(lista):
#     return tuple(lista)# Utiliza una función para convertir 

# if __name__ == "__main__":
#     productos_tupla = convertir_lista_a_tupla(productos)  # Convierte la lista a tupla
#     print(f"Los productos en la lista de compras como tupla son: {productos_tupla}")
def convertir_lista_a_tupla(lista):
    return tuple(lista)

if __name__ == "__main__":
    compras = input("Ingrese una lista de compras (separada por comas): ")
    productos = compras.split(", ")
    print(f"Los productos en la lista de compras son: {productos}")
    
    productos_tupla = convertir_lista_a_tupla(productos)
    print(f"Los productos en la lista de compras como tupla son: {productos_tupla}")