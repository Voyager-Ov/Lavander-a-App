import funciones_Add as fa
import pickle
import os.path
Archivo_de_Clientes = "Clientes.pkl"


class Clientes:    # Creo la clase Clientes para que tenga los atributos vistos
    def __init__(self, dni, nombre, apellido, telefono, email, direccion, pedidos, subscripcion):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.email = email
        self.direccion = direccion
        self.pedidos = pedidos
        self.subscripcion = subscripcion

    # Creo la funcion __str__ en la clase para que cuando haga un oprint me
    # muestre directamente el objeto
    def __str__(self):
        r = (
             "Nombre: " + str(self.nombre) + "\n" +
             "Apellido: " + str(self.apellido) + "\n" +
             "Telefono: " + str(self.telefono) + "\n" +
             "Email: " + str(self.email) + "\n" +
             "Direccion: " + str(self.direccion) + "\n" +
             "Pedidos: " + str(self.pedidos) + "\n" +
             "Subscripcion: " + str(self.subscripcion) + "\n")
        return r


def crear_Cliente():       # defino la funcion para crear al cliente
    print("Para crear el cliente ingrese complete los sigioentes campos: ")
    dni = input("DNI: ")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    telefono = input("Telefono: ")
    email = input("Email: ")
    direccion = input("Direccion: ")
    subscripcion = "falta encrontar lka funcion para las subscripciuones"
    pedidos = "falta encrontar lka funcion para las pedidos"
    # Instancio el objeto con los parametros que nos pasan
    cliente = Clientes(dni, nombre, apellido, telefono, email, direccion, pedidos, subscripcion)
    # uso la funcion de Funciones add para cargar el objeto cliente al archivo de Clientes
    print("Los datos del clinete son los siguientes: ")
    print(cliente)
    cliente_mod = cambiar_Datos_Cliente(cliente)
    fa.Cargar_objeto_al_Archivo(cliente_mod, Archivo_de_Clientes)
    return cliente_mod


def mostrar_Clientes():
    print("          ///CLIENTES////")
    if os.path.exists(Archivo_de_Clientes):
        arc = open(Archivo_de_Clientes, "rb")
        t = os.path.getsize(Archivo_de_Clientes)
        while arc.tell() < t:
            cliente = pickle.load(arc)
            print(cliente)
        arc.close



def buscar_cliente(dni):
    if os.path.exists(Archivo_de_Clientes):
        arc = open(Archivo_de_Clientes, "rb")
        clientes = pickle.load(arc)
        for i in clientes:
            if i.dni == dni:
                return i
            return None
        

def cambiar_Datos_Cliente(cliente):
    print("DESEA CAMBIAR LOS DATOS DEL CLIENTE???")
    print("1. Si")
    print("2. No")
    eleccion = input("Ingrese la opcion que desee: ")
    if eleccion == "1":
        print("Para cambiar los datos del cliente ingrese complete los siguientes campos: ")
        dni = input("DNI: ")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        telefono = input("Telefono: ")
        email = input("Email: ")
        direccion = input("Direccion: ")
        subscripcion = "falta encrontar lka funcion para las subscripciuones"
        pedidos = "falta encontrar funcion para la lista de pedidos"
        # Instancio el objeto con los parametros que nos pasan
        cliente = Clientes(dni, nombre, apellido, telefono, email, direccion, pedidos
                           , subscripcion)
        return cliente
    else:
        return cliente

mostrar_Clientes()
