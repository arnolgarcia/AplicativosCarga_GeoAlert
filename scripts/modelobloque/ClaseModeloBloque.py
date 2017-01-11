__author__ = 'Arnol'


import logging
import linecache
import csv


# -----------------------------------------------------------------------------
#     Objeto Registro
# -----------------------------------------------------------------------------
class Registro(object):

    def __init__(self):
        """
        Clase para almacenar un registro del modelo de bloques
        :param
        :return:
        """
        # TODO: ver si hay que incluir mas campos con los datos de Collaahuasi
        self.xcentre = None
        self.ycentre = None
        self.zcentre = None
        self.xlength = None
        self.ylength = None
        self.zlength = None
        self.litologia = None
        self.alteracion = None
        self.mineralizacion = None
        self.ucs = None
        self.rmr = None
        self.field_1 = ""
        self.field_2 = ""
        self.field_3 = ""
        self.field_4 = ""
        self.field_5 = ""
        self.field_6 = ""
        self.field_7 = ""
        self.field_8 = ""
        self.field_9 = ""

    def registro(self, data):
        """
        Metodo para almacenar datos en un objeto de clase Registro()
        :param data : vector con los datos de prismas
        :return:
        """
        self.xcentre = float(data[0])
        self.ycentre = float(data[1])
        self.zcentre = float(data[2])
        self.xlength = float(data[3])
        self.ylength = float(data[4])
        self.zlength = float(data[5])
        self.litologia = float(data[6])
        self.alteracion = float(data[7])
        self.mineralizacion = float(data[8])
        self.ucs = float(data[9])
        self.rmr = float(data[10])
        self.field_1 = data[11]
        self.field_2 = data[12]
        self.field_3 = data[13]
        self.field_4 = data[14]
        self.field_5 = data[15]
        self.field_6 = data[16]
        self.field_7 = data[17]
        self.field_8 = data[18]
        self.field_9 = data[19]

    def getData(self):
        """
        Metodo para obtener los datos almacenados en un objeto de clase Registro()
        :param
        :return: [] -> Datos en formato de vector
        """
        return [self.xcentre,
                self.ycentre,
                self.zcentre,
                self.xlength,
                self.ylength,
                self.zlength,
                self.litologia,
                self.alteracion,
                self.mineralizacion,
                self.ucs,
                self.rmr,
                self.field_1,
                self.field_2,
                self.field_3,
                self.field_4,
                self.field_5,
                self.field_6,
                self.field_7,
                self.field_8,
                self.field_9]


# -----------------------------------------------------------------------------
#     Objeto ModeloBloque
# -----------------------------------------------------------------------------
class ModeloBloque(object):
    def __init__(self, name, fecha, xlength, ylength, zlength, toFile=False, tempfile=None):
        self.name = name
        self.toFile = toFile
        self.tempfile = tempfile
        self.puntos = 0  # Numero de registros que tiene el Modelo de Bloques
        self.datos = []  # Objetos de clase "registro"
        self.fecha = fecha
        self.xlength = xlength
        self.ylength = ylength
        self.zlength = zlength

    def registro(self, data):  # Fn para agregar un nuevo registro a ModeloBloques
        # Crear nuevo archivo y borrar si existe uno previo
        if self.puntos == 0 & self.toFile:
            temp = open(self.tempfile, 'w+')
            temp.close()
        if self.toFile:
            with open(self.tempfile, 'ab+') as tempfile:
                wr = csv.writer(tempfile, quoting=csv.QUOTE_NONNUMERIC)
                wr.writerow(data)
        else:
            reg = Registro()
            reg.registro(data)
            self.datos.append(reg)
        self.puntos += 1

    def getRegistro(self, k):  # # Obtiene todos los datos del registro "k" como una lista
        if k >= self.puntos:
            return -1
        if self.toFile:
            with open(self.tempfile, 'r') as tempfile:
                data = linecache.getline(self.tempfile, k+1).strip('\n')
                data = data.split(",")
                reg = Registro()
                reg.registro(data)
            return reg.getData()
        else:
            return (self.datos[k]).getData()

    # TODO: modificar para la implementacion desde archivo
    def getColumn(self, columna):  # Obtiene todos los datos del campo "columna" como una lista
        xx = []
        for i in xrange(self.puntos):
            xx.append((self.datos[i]).getData()[columna])
        return xx

    # TODO: modificar para la implementacion desde archivo
    def deleteRegistro(self, k):
        del self.datos[k]
        self.puntos -= 1

    # TODO: modificar para la implementacion desde archivo
    def updateRegistro(self, k, newdata):
        self.deleteRegistro(k)
        self.registro(newdata)

