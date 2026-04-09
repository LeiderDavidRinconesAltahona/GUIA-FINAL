from productos import productos

def hacer_pedido():
    opcion = input("Seleccione producto: ")
    cantidad = int(input("Cantidad: "))

    nombre, precio = productos[opcion]
    total = precio * cantidad

    print("Producto:", nombre)
    print("Total:", total)

    with open("historial.txt", "a") as f:
        f.write(f"{nombre} - {cantidad} - {total}\n")
