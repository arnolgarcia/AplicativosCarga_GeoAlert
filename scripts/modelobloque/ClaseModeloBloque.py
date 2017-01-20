__author__ = 'Arnol'


import logging
import linecache
import csv

from itertools import (takewhile,repeat)


# -----------------------------------------------------------------------------
#     Objeto RegistroMB_CMDIC
# -----------------------------------------------------------------------------
class RegistroMB_CMDIC(object):

    def __init__(self):
        # TODO: comprobar que nombres sean los originales y en el orden correcto
        self.fields = ['xcentre', 'ycentre', 'zcentre',
                       'xlength', 'ylength', 'zlength',
                       'alter_det', 'alter_mp',
                       'banco',
                       'bsu', 'bsu_rat', 'densidad_mp',
                       'ff', 'ff_lp', 'ff_rat',
                       'gsi_rat',
                       'hsag', 'hsaga',
                       'int_alt', 'jc', 'jc_rat',
                       'lito_det', 'lito_mp',
                       'mi', 'mnzn_det', 'mnzn_mp',
                       'modelo',
                       'mot', 'mot_mp', 'ppv_crit', 'rfc_op',
                       'rmom', 'rmu_rat',
                       'rqd', 'rqd_porc', 'rqd_rat',
                       'rst_op', 'rsu_rat',
                       'st_com',
                       'topo', 'topo_mp',
                       'ucs', 'ugcut', 'ugg', 'ugg_rat',
                       'ugm', 'ugm_mp', 'ugt']
        self.data = []
        self.nrofields = len(self.fields)  # 49 campos
        self.llave = "(xcentre, ycentre, zcentre)"
        for i in range(self.nrofields):
            setattr(self, self.fields[i], None)

    def registro(self, data):
        self.data = []
        for i in range(self.nrofields):
            setattr(self, self.fields[i], float(data[i]))
            self.data.append(float(data[i]))

    def getData(self):
        return self.data

    def registroToDB(self):
        aux = []
        for i in range(3, self.nrofields):
            aux.append(getattr(self, self.fields[i]))
        datos = [self.xcentre, self.ycentre, self.zcentre, aux]
        # Retornar salida
        newReg = RegistroMB_DB()
        newReg.registro(datos)
        return newReg

    def registroToMel(self):
        # TODO: confirmar las variables lito, alter, mnzn y rmr o ver que se puede poner en su lugar
        datos = [self.xcentre, self.ycentre, self.zcentre,
                 self.xlength, self.ylength, self.zlength,
                 self.lito_det, self.alter_det, self.mnzn_det,
                 self.ucs, self.rmu_rat]
        # Retornar salida
        newReg = RegistroMB_MEL()
        newReg.registro(datos)
        return newReg


# -----------------------------------------------------------------------------
#     Objeto RegistroMB_MEL
# -----------------------------------------------------------------------------
class RegistroMB_MEL(object):

    def __init__(self):
        # TODO: comprobar que nombres sean los originales y en el orden correcto
        self.fields = ['xcentre', 'ycentre', 'zcentre',
                       'xlength', 'ylength', 'zlength',
                       'litologia', 'alteracion', 'minzone'
                       'ucs', 'rmr_adic']
        self.data = []
        self.nrofields = len(self.fields)  # 11 campos
        self.llave = "(xcentre, ycentre, zcentre)"
        for i in range(self.nrofields):
            setattr(self, self.fields[i], None)

    def registro(self, data):
        self.data = []
        for i in range(self.nrofields):
            setattr(self, self.fields[i], float(data[i]))
            self.data.append(float(data[i]))

    def getData(self):
        return self.data

    def registroToDB(self):
        aux = []
        for i in range(3, self.nrofields):
            aux.append(getattr(self, self.fields[i]))
        datos = [self.xcentre, self.ycentre, self.zcentre, aux]
        # Retornar salida
        newReg = RegistroMB_DB()
        newReg.registro(datos)
        return newReg


# -----------------------------------------------------------------------------
#     Objeto RegistroMB_DB
# -----------------------------------------------------------------------------
class RegistroMB_DB(object):

    def __init__(self):
        self.fields = ['xcentre', 'ycentre', 'zcentre', 'valores']
        self.data = []
        self.nrofields = len(self.fields)
        self.llave = "(xcentre, ycentre, zcentre)"
        #self.fields_valores = None  # TODO: ver si agregarlo o no
        for i in range(self.nrofields):
            setattr(self, self.fields[i], None)

    def registro(self, data):
        self.data = []
        for i in range(self.nrofields):
            setattr(self, self.fields[i], data[i])
            self.data.append(float(data[i]))

    def getData(self):
        return self.data


# -----------------------------------------------------------------------------
#     Objeto ModeloBloque
# -----------------------------------------------------------------------------
class ModeloBloque(object):
    def __init__(self, name, fecha, xlength, ylength, zlength, toFile=False, tempfile=None, mybatch=1):
        self.name = name
        self.toFile = toFile
        self.batch = mybatch
        self.tempfile = tempfile
        self.sep = ","
        self.header = False
        self.puntos = 0  # Numero de registros que tiene el Modelo de Bloques
        self.datos = []  # Objetos de clase "registro"
        self.fecha = fecha
        self.xlength = xlength
        self.ylength = ylength
        self.zlength = zlength

    def registro(self, dataReg):  # Fn para agregar un nuevo registro a ModeloBloques
        # Guardar registro
        self.datos.append(dataReg)
        self.puntos += 1

        # Si se guarda en disco crear nuevo archivo y borrar si existe uno previo
        if self.puntos == 1 & self.toFile:
            temp = open(self.tempfile, 'w+')
            temp.close()

        # Guardar si se llega al batch o se "cierra"
        if self.toFile and (self.puntos % self.batch == 0):
            self.saveToFile()

    def getRegistro(self, k):  # # Obtiene todos los datos del registro "k" como una lista, con k= 1, 2,...
        if k > self.puntos or k < 1:
            logging.error("El valor %d esta fuera de rango, el modelo tiene %d puntos", k, self.puntos)
            return -1
        if self.header:
            k += 1
        if self.toFile:
            with open(self.tempfile) as fp:
                for i, line in enumerate(fp):
                    if i == k-1:
                        data = line
                        break
            data = [float(k) for k in data.split(self.sep)]
            return data
        else:
            return [float(k) for k in (self.datos[k-1])]

    def saveToFile(self):
        if self.toFile:
            with open(self.tempfile, 'ab+') as tempfile:
                wr = csv.writer(tempfile, quoting=csv.QUOTE_NONNUMERIC)
                wr.writerows(self.datos)
            self.datos = []
            logging.debug("Lineas pocesadas y guardadas en archivo: %d", self.puntos)

    def closeRegistros(self):
        if self.toFile & len(self.datos)>0:
            self.saveToFile()

    def setFile(self, fileName, sep, hasheader):
        self.toFile = True
        self.tempfile = fileName
        self.sep = sep
        self.header = hasheader
        # Setear el numero de puntos
        f = open(fileName, 'rb')
        bufgen = takewhile(lambda x: x, (f.read(1024*1024) for _ in repeat(None)))
        self.puntos = sum( buf.count(b'\n') for buf in bufgen if buf)
        # si el archivo tiene encabezado restar una fila
        if self.header:
            self.puntos += -1





"""
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
"""


# -----------------------------------------------------------------------------
#     Funciones generales
# -----------------------------------------------------------------------------

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False