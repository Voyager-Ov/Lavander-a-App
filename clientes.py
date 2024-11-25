import funciones_Add as fa
import pickle
import os.path
Archivo_de_Clientes = "Clientes.pkl"


class Cliente:    # Creo la clase Clientes para que tenga los atributos vistos
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
    cliente = Cliente(dni, nombre, apellido, telefono, email, direccion, pedidos, subscripcion)
    # uso la funcion de Funciones add para cargar el objeto cliente al archivo de Clientes
    print("Los datos del clinete son los siguientes: ")
    print(cliente)
    print("DESEA CAMBIAR LOS DATOS DEL CLIENTE???")
    print("1. Si")
    print("2. No")
    opcion = int(input("Ingrese su opcion: "))
    if opcion == 1:
        cliente = cambiar_Datos_Cliente(cliente)
    else:
        if opcion == 2:
            print("El cliente se guardo correctamente")
        else:
            print("valor Incorrecto")
    fa.Cargar_objeto_al_Archivo(cliente, Archivo_de_Clientes)
    return cliente


def mostrar_Clientes():
    print("          ///CLIENTES////")
    if os.path.exists(Archivo_de_Clientes):
        arc = open(Archivo_de_Clientes, "rb")
        t = os.path.getsize(Archivo_de_Clientes)
        while arc.tell() < t:
            cliente = pickle.load(arc)
            print(cliente)
        arc.close()


def mostrar_Clientes_unico(valor=None, atributo=None):
    if valor is None:
        valor = input("ingrese el/la" + atributo + "del cliente: ")
    if atributo is None:
        atributo = input("Ingrese que quiere buscar(ejemplo: dni o nombre o apellido o telefono o email o direccion): ").lower()
    cliente = buscar_cliente(valor, atributo)
    if cliente is not None:
        print(cliente)
    else:
        print("El cliente no se encontro")


def buscar_Clientes_unico(valor=None, atributo=None):
    if valor is None:
        valor = input("ingrese el/la" + atributo + "del cliente: ")
    if atributo is None:
        atributo = input("Ingrese que quiere buscar(ejemplo: dni o nombre o apellido o telefono o email o direccion): ").lower()
    cliente = buscar_cliente(valor, atributo)
    if cliente is not None:
        return cliente
    else:
        print("El cliente no se encontro")


def buscar_cliente(valor, atributo):
    if os.path.exists(Archivo_de_Clientes):
        arc = open(Archivo_de_Clientes, "rb")
        t = os.path.getsize(Archivo_de_Clientes)
        cliente = []
        while arc.tell() < t:
            tick = pickle.load(arc)
            cliente.append(tick)
        for i in cliente:
            if getattr(i, atributo) == valor:
                return i
            else:
                return None


def cambiar_Datos_Cliente(cliente):
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
    cliente = Cliente(dni, nombre, apellido, telefono, email, direccion, pedidos, subscripcion)
    return cliente


def eliminar_Cliente():
    print("Para eliminar el cliente primero seleccione el metodo de busquda: ")
    print("1. Buscar por DNI")
    print("2. Buscar por nombre")
    print("3. Buscar por apellido")
    print("4. Buscar por telefono")
    print("5. Buscar por email")
    print("6. Buscar por direccion")
    opcion = int(input("Ingrese su opcion: "))
    while 1 <= opcion <=6:
        if opcion == 1:
            atributo = "dni"
            valor = input("Ingrese el DNI: ")
            break
        elif opcion == 2:
            atributo = "nombre"
            valor = input("Ingrese el nombre: ")
            break
        elif opcion == 3:
            atributo = "apellido"
            valor = input("Ingrese el apellido: ")
            break
        elif opcion == 4:
            atributo = "telefono"
            valor = input("Ingrese el telefono: ")
            break
        elif opcion == 5:
            atributo = "email"
            valor = input("Ingrese el email: ")
            break
        elif opcion == 6:
            atributo = "direccion"
            valor = input("Ingrese la direccion: ")
            break
        else:
            print("valor Incorrecto")
    if os.path.exists(Archivo_de_Clientes):
        arch_cli = open(Archivo_de_Clientes, "rb")
        t = os.path.getsize(Archivo_de_Clientes)
        cliente = []
        while arch_cli.tell() < t:
            tick = pickle.load(arch_cli)
            cliente.append(tick)
        cli_del = buscar_cliente(valor, atributo)
        print("El clienmte que quiere eliminar es: ")
        print(cli_del)
        if cli_del is not None:
            print("Esta seguro de borrar el cliente?", "\n1. Si", "\n2. No")
            eleccion = int(input("Ingrese su opcion: "))
            if eleccion == 1:
                cliente.remove(cli_del)
                fa.Cargar_objeto_al_Archivo(cliente, Archivo_de_Clientes)
                print("El cliente se elimino correctamente")
            else:
                print("El cliente no se elimino")
        else:
            print("El cliente no se encontro")


