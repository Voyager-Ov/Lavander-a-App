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


def Buscador_objeto_en_Archivo(objeto, archivo):
    pass