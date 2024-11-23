import funciones_Add


Archivo_de_Clientes = "Clientes.csv"


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
    subscripcion = input("Subscripcion: ")
    pedidos = "falta encontrar funcion para la lista de pedidos"
    # Instancio el objeto con los parametros que nos pasan
    cliente = Clientes(dni, nombre, apellido, telefono, email, direccion, pedidos, subscripcion)
    # uso la funcion de Funciones add para cargar el objeto cliente al archivo de Clientes
    Funciones_Add.Cargar_objeto_al_Archivo(cliente, Archivo_de_Clientes)


def mostrar_Clientes(cliente):
    print("          ///CLIENTES////")
    for i in cliente:
        print(i)

