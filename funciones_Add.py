import os.path
import pickle
Archivo_de_Clientes = "Clientes.pkl"


def cargar_objeto_al_archivo(objeto, archivo):
    """
    Carga un objeto en un archivo, si el archivo existe lo abre en modo 'a'
    si el archivo no existe lo abre en modo 'w'
    :param objeto:
    :param archivo:
    """
    if os.path.exists(archivo):
        arc = open(archivo, 'ab')
        pickle.dump(objeto, arc)
        arc.close()
    else:
        arch = open(archivo, 'wb')
        pickle.dump(objeto, arch)
        arch.close()


def buscar_objeto_enArchivo(atributo=None, valor=None, archivo=None):
    if archivo is None:
        archivo = input("Ingrese el nombre del archivo: ")
    if atributo is None:
        atributo = input("Ingrese el atributo: ")
    if valor is None:
        valor = input("Ingrese el valor: ")
    if os.path.exists(archivo):
        arc = open(archivo, "rb")
        t = os.path.getsize(archivo)
        arc.seek(0)
        atributo_list = []
        while arc.tell() < t:
            tick = pickle.load(arc)
            atributo_list.append(tick)
        for i in atributo_list:
            if getattr(i, atributo) == valor:
                return i
        return None


def ordenar_archivo(archivo, parametro):
    """
    Ordena a los objetos del archivo por el parámetro de menor a mayor.
    
    :param archivo: Nombre del archivo que contiene los objetos.
    :param parametro: El atributo por el cual se ordenarán los objetos.
    :return: Archivo ordenado por el parámetro.
    """
    if os.path.exists(archivo):
        with open(archivo, 'rb') as arc:  # Abrir en modo lectura 
            try:
                clientes = pickle.load(arc)
            except EOFError:
                return  # Si el archivo está vacío, no hacemos nada

        # Ordenar los clientes
        clientes_ordenados = sorted(clientes, key=lambda persona: getattr(persona, parametro))

        # Guardar los clientes ordenados de nuevo en el archivo
        with open(archivo, 'wb') as arc:  # Abrir en modo escritura 
            pickle.dump(clientes_ordenados, arc)


def Buscador_Coincidencias_en_Archivo_mio(atributo, archivo, coincidencia):
    if os.path.exists(archivo):
        arc = open(archivo, "rb")
        clientes = pickle.load(arc)
        for i in clientes:
            if getattr(i, atributo) == coincidencia:
                return True  # Se encontró al menos una coincidencia
        return False  # No se encontraron coincidencias


def crear_objeto(clase):
    """
    Crea una instancia de la clase proporcionada y solicita al usuario que ingrese valores para cada
    uno de los argumentos del constructor de la clase.

    :param clase: La clase de la cual se quiere crear una instancia.
    :return: Una instancia de la clase con los atributos asignados.
    """
    # Obtener el constructor de la clase y sus argumentos
    parametros = clase.__init__.__code__.co_varnames[1:clase.__init__.__code__.co_argcount]

    # Crear un diccionario para almacenar los valores
    valores = {}

    # Pedir al usuario valores para cada parámetro
    for parametro in parametros:
        valor = input(f"Ingrese el valor para {parametro}: ")
        # Convertir a float o int si es necesario
        try:
            if '.' in valor:
                valores[parametro] = float(valor)
            else:
                valores[parametro] = int(valor)
        except ValueError:
            valores[parametro] = valor

    # Crear una instancia de la clase con los valores proporcionados
    return clase(**valores)


def mostrar_objetos(archivo, tipo_objeto='Objeto'):
    """
    Muestra todos los objetos de cualquier tipo guardados en un archivo pickle.

    :param archivo: La ruta del archivo que contiene los objetos serializados.
    :param tipo_objeto: Descripción del tipo de objeto a mostrar, para propósitos informativos.
    """
    if not os.path.exists(archivo):
        print("El archivo no existe.")
        return
    print(f"mostrando ////{tipo_objeto}///")
    arc = open(archivo, "rb")
    t = os.path.getsize(archivo)
    while arc.tell() < t:
        obj = pickle.load(arc)
        print(obj)
    arc.close()


def eliminar_objeto_del_archivo(atributo, valor, archivo):
    """
    Elimina un objeto de un archivo pickle.

    :param atributo: el atributo del objeto que se utilizará para la búsqueda
    :param valor: el valor del atributo que se buscará
    :param archivo: el nombre del archivo pickle
    """
    objeto_a_eliminar = buscar_objeto_enArchivo(atributo, valor, archivo)
    if objeto_a_eliminar is None:
        print(f"No se encontró ningún objeto con {atributo} igual a {valor} en el archivo {archivo}.")
        return

    if not os.path.exists(archivo):
        print(f"El archivo {archivo} no existe.")
        return

    arc = open(archivo, "rb")
    t = os.path.getsize(archivo)
    arc.seek(0)

    objetos = []
    while arc.tell() < t:
        objeto = pickle.load(arc)
        if objeto != objeto_a_eliminar:
            objetos.append(objeto)
    arc.close()

    # Sobreescribir el archivo con los objetos restantes
    with open(archivo, 'wb') as arc:
        pickle.dump(objetos, arc)

    print(f"Se eliminó el objeto con {atributo} igual a {valor} del archivo {archivo}.")
