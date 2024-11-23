import os.path
import pickle


def Cargar_objeto_al_Archivo(objeto, archivo):
    """
    Carga un objeto en un archivo, si el archivo existe lo abre en modo 'a'
    si el archivo no existe lo abre en modo 'w'
    :param objeto:
    :param archivo:
    """
    if os.path.exists(archivo):
        arc = open(archivo, 'a')
        pickle.dump(objeto, arc)
        arc.close()
    else:
        arch = open(archivo, 'w')
        pickle.dump(objeto, arch)
        arch.close()


def ordenar_Archivo(archivo, parametro):
    """
    ordena a los objetos del archivo por el parametro de menor a mayor
    :param archivo:
    :param parametro:
    :return: Archivo ordenado por el parametro
    """
    if os.path.exists(archivo):
        arc = open(archivo, 'r')
        clientes = pickle.load(arc)
        arc.close()
        clientes_ordenados = sorted(clientes, key=lambda persona: persona.parametro)
        


def Buscador_Coincidencias_en_Archivo(objeto, parametro, archivo):
    pass