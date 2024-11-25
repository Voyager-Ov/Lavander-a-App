import os.path
import pickle
Archivo_de_Clientes = "Clientes.pkl"

def Cargar_objeto_al_Archivo(objeto, archivo):
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


def ordenar_archivo(archivo, parametro):
    """
    Ordena a los objetos del archivo por el parámetro de menor a mayor.
    
    :param archivo: nombre del archivo que contiene los objetos.
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




def Buscador_Coincidencias_en_Archivo_mio(parametro, archivo, coincidencia):
    if os.path.exists(archivo):
        arc = open(archivo, "rb")
        clientes = pickle.load(arc)
        for i in clientes:
            if getattr(i, parametro) == coincidencia:
                return True  # Se encontró al menos una coincidencia
        return False  # No se encontraron coincidencias
    

def Buscador_Coincidencias_en_Archivo_blackbox(parametro, archivo, coincidencia):
    """
    Busca coincidencias en el archivo para el parámetro dado y la coincidencia especificada.
    Retorna True si se encuentra al menos un objeto, False si no se encuentran coincidencias.
    :param parametro: El atributo del objeto en el que se va a buscar la coincidencia.
    :param archivo: El archivo donde se almacenan los objetos.
    :param coincidencia: El valor que se está buscando.
    :return: True si se encuentra al menos un objeto, False si no se encuentran coincidencias.
    """
    if os.path.exists(archivo):
        with open(archivo, "rb") as arc:  # Abrir en modo lectura binaria
            try:
                clientes = pickle.load(arc)
                for i in clientes:
                    if getattr(i, parametro) == coincidencia:
                        return True  # Se encontró al menos una coincidencia
            except EOFError:
                return False  # El archivo está vacío o tiene un formato incorrecto
    return False  # No se encontraron coincidencias o el archivo no existe
