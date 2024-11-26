import clientes as cli
import funciones_Add as fa
import pickle
import os.path

Archivo_de_Clientes = "Clientes.pkl"
Archivo_de_pedidos = "Pedidos.pkl"


class Pedido:
    def __init__(self, estado, cliente, tiporopa, descripcion, colortela, categoria, fechaentrega, total):
        self.estado = estado
        self.cliente = cliente
        self.tiporopa = tiporopa
        self.descripcion = descripcion
        self.colortela = colortela
        self.categoria = categoria
        self.fechaentrega = fechaentrega
        self.total = total

    def __str__(self):
        r = (
                "Estado: " + str(self.estado) + "\n" +
                "Cliente: " + str(self.cliente) + "\n" +
                "Tipo de Ropa: " + str(self.tiporopa) + "\n" +
                "Descripcion: " + str(self.descripcion) + "\n" +
                "Color de la Tela: " + str(self.colortela) + "\n" +
                "Categoria: " + str(self.categoria) + "\n" +
                "Fecha de Entrega: " + str(self.fechaentrega) + "\n" +
                "Total: " + str(self.total) + "\n"
        )
        return r


def mostrar_pedidos():
    print("          ///PEDIDOS////")
    if os.path.exists(Archivo_de_pedidos):
        arc = open(Archivo_de_pedidos, "rb")
        t = os.path.getsize(Archivo_de_pedidos)
        while arc.tell() < t:
            pedido = pickle.load(arc)
            print(pedido)
        arc.close()


def crear_Pedido():
    print("Cliente Nuevo?? \n 1. Si \n 2. No")
    opcion = int(input("Ingrese su opcion: "))
    if opcion == 1:
        cliente = cli.crear_Cliente()
    else:
        cliente = cli.buscar_Clientes_unico()
    print("Para crear el pedido complete los siguientes campos: ")
    estado = input("Estado: ")
    tiporopa = input("Tipo de Ropa: ")
    descripcion = input("Descripcion: ")
    colortela = input("Color de la Tela: ")
    categoria = input("Categoria: ")
    fechaentrega = input("Fecha de Entrega: ")
    total = input("Total: ")
    pedido = Pedido(estado, cliente, tiporopa, descripcion, colortela, categoria, fechaentrega, total)
    print("los datos del pedido son los siguientes: ")
    print(pedido)
    print("Desea cambiar los datos del Pedido??? \n 1. Si \n 2. No")
    opcion = int(input("Ingrese su opcion: "))
    if opcion == 1:
        pedido = cambiar_Datos_Pedido(pedido)
    else:
        print("valor Incorrecto")
    fa.Cargar_objeto_al_Archivo(pedido, Archivo_de_pedidos)
    print("El pedido se guardo correctamente")
    return pedido


def actualizar_atributo(nombre_atributo, valor_actual):
    """ Solicita al usuario un nuevo valor para el atributo y lo actualiza si es necesario. """
    nuevo_valor = input(f"{nombre_atributo} ({valor_actual}): ")
    if nuevo_valor:
        return nuevo_valor
    else:
        return valor_actual


def cambiar_Datos_Pedido(pedido):
    """
    Cambia los datos del pedido que se le pasa como parámetro.
    :param pedido: Objeto Pedido a modificar.
    :return: Objeto Pedido modificado.
    """
    print("Para cambiar los datos del pedido complete los siguientes campos (deje vacío para no cambiar): ")

    pedido.estado = actualizar_atributo("Estado", pedido.estado)
    pedido.tiporopa = actualizar_atributo("Tipo de Ropa", pedido.tiporopa)
    pedido.descripcion = actualizar_atributo("Descripcion", pedido.descripcion)
    pedido.colortela = actualizar_atributo("Color de la Tela", pedido.colortela)
    pedido.categoria = actualizar_atributo("Categoria", pedido.categoria)
    pedido.fechaentrega = actualizar_atributo("Fecha de Entrega", pedido.fechaentrega)
    pedido.total = actualizar_atributo("Total", pedido.total)

    print("Los datos del pedido han sido actualizados.")
    return pedido



