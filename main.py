import clientes as cli
import pedidos as ped


def main():
    while True:
        print("Menu de Opciones:")
        print("1. cretar cliente")
        print("2. crear pedido ")
        print("3. mostrar clientes")
        print("4. mostrar pedidos")
        print("5. salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            print("Has seleccionado crear cliente")
            cli.crear_Cliente()
        elif opcion == '2':
            print("Has seleccionado crear pedido")
            ped.crear_Pedido()
        elif opcion == '3':
            print("Has seleccionado mostrar cleintes")
            cli.mostrar_Clientes()
        elif opcion == '4':
            print("Has seleccionado mostrar pedidos")
            ped.mostrar_pedidos()
        else:
            print("Opción no válida, por favor seleccione una opción válida.")
