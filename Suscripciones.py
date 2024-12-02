import funciones_Add as fa
archivo_sub = "Suscripcion.pkl"


class Suscripcion:
    def __init__(self, plan, precio, lavados):
        self.plan = plan
        self.precio = precio
        self.lavados = lavados

    def __str__(self):
        r = (
                "Plan: " + str(self.plan) + "\n" +
                "Precio: " + str(self.precio) + "\n" +
                "Lavados: " + str(self.lavados) + "\n"
        )
        return r


def crear_suscripcion():
    print("Crear Suscripcion")
    sub = fa.crear_objeto(Suscripcion)
    fa.cargar_objeto_al_archivo(sub, archivo_sub)


def mostrar_suscripciones():
    if not fa.os.path.exists(archivo_sub):
        print(f"El archivo {archivo_sub} no existe. No hay suscripciones para mostrar.")
        return
    fa.mostrar_objetos(archivo_sub, "Suscripcion")


def eliminar_suscripcion():
    subElim = fa.buscar_objeto_enArchivo("plan", input("Ingrese el plan a eliminar: "), archivo_sub)
    if subElim is not None:
        print(f"El plan que quiere eliminar es: \n {subElim}")
        print("Esta seguro de borrar el plan?", "\n1. Si", "\n2. No")
        eleccion = int(input("Ingrese su opcion: "))
        if eleccion == 1:
            fa.cargar_objeto_al_archivo(subElim, archivo_sub)
            print("El plan se elimino correctamente")
        else:
            print("El plan no se elimino")
    else:
        print("El plan no se encontro")
        