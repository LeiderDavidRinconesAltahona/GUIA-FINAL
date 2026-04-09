from productos import ver_productos
from Pedidos import hacer_pedido

def menu():
    while True:
        print("\n1. Ver productos")
        print("2. Hacer pedido")
        print("3. Salir")

        op = input("Opción: ")

        if op == "1":
            ver_productos()
        elif op == "2":
            hacer_pedido()
        elif op == "3":
            break
