import clientes


class Pedido:
    def __init__(self, cliente, numDePedido, tipoDePedido, ColorDeLaTela,
                 PrecioTotal, FechaDeEntrega):
        self.cliente = cliente
        self.numDePedido = numDePedido
        self.tipoDePedido = tipoDePedido
        self.ColorDeLaTela = ColorDeLaTela
        self.PrecioTotal = PrecioTotal
        self.FechaDeEntrega = FechaDeEntrega

    def __str__(self):
        r = (
            "Numero de Pedido: " + str(self.numDePedido) + "\n" +
            "Tipo de Pedido: " + str(self.tipoDePedido) + "\n" +
            "Color de la tela: " + str(self.ColorDeLaTela) + "\n" +
            "Precio total: " + str(self.PrecioTotal) + "\n" +
            "Fecha de Entrega: " + str(self.FechaDeEntrega) + 2*"\n" +
            "//Cliente//" + "\n" + str(self.cliente) + 2*"\n"
        )


def Crear_Pedido():
    print("//Para crear un pedido porfavor rellene los campos requeridos//", "\n")
    dni = input("Ingresa el DNI del cliente, (si el cliente ya existe no van a tomar los datos): ")

