# -*- coding: utf-8 -*-
"""
@file:      ClasePrismas.py
@version:   2
@date:      Nov,  2016
@author:    Rodrigo (version 1)
            Arnol (version 2)
"""

import logging


# -----------------------------------------------------------------------------
#     Objeto Registro
# -----------------------------------------------------------------------------
class Registro(object):

    def __init__(self):
        """
        Clase para almacenar un registro de prismas
        :param
        :return:
        """
        self.fechahora = None
        self.fecha = None
        self.hora = None
        self.norte = None
        self.este = None
        self.altura = None
        self.distancia = None
        self.hz = None
        self.v = None
        self.hor_distancia = None
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
        self.fechahora = data[0]
        self.fecha = data[1]
        self.hora = data[2]
        self.norte = data[3]
        self.este = data[4]
        self.altura = data[5]
        self.distancia = data[6]
        self.hz = data[7]
        self.v = data[8]
        self.hor_distancia = data[9]
        self.field_1 = data[10]
        self.field_2 = data[11]
        self.field_3 = data[12]
        self.field_4 = data[13]
        self.field_5 = data[14]
        self.field_6 = data[15]
        self.field_7 = data[16]
        self.field_8 = data[17]
        self.field_9 = data[18]

    def getData(self):
        """
        Metodo para obtener los datos almacenados en un objeto de clase Registro()
        :param
        :return: [] -> Datos en formato de vector
        """
        return [self.fechahora.strftime('%Y-%m-%d %H:%M:%S'),
                self.fecha,
                self.hora,
                self.norte,
                self.este,
                self.altura,
                self.distancia,
                self.hz,
                self.v,
                self.hor_distancia,
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
#     Objeto Prisma
# -----------------------------------------------------------------------------
class Prisma(object):
    def __init__(self, name):
        self.name = name
        self.elementos = 0  # Numero de registros que tiene el Prisma
        self.datos = []  # Objetos de clase "registro"
        self.fechasSet = set()
        self.fechasList = []

    def registro(self, data):  # Fn para agregar un nuevo registro a Prisma
        reg = Registro()
        reg.registro(data)
        self.datos.append(reg)
        self.fechasSet.add(data[0].strftime('%Y-%m-%d %H:%M:%S'))
        self.fechasList.append(data[0].strftime('%Y-%m-%d %H:%M:%S'))
        self.elementos += 1

    def getRegistro(self, k):
        return (self.datos[k]).getData()

    def getColumn(self, columna):  # Obtiene todos los datos del campo "columna" como una lista
        xx = []
        for i in xrange(self.elementos):
            xx.append((self.datos[i]).getData()[columna])
        return xx

    def deleteRegistro(self, k):
        del self.datos[k]
        fechaK = self.fechasList[k]
        del self.fechasList[k]
        self.fechasSet.remove(fechaK)
        self.elementos -= 1

    def updateRegistro(self, k, newdata):
        self.deleteRegistro(k)
        self.registro(newdata)


# -----------------------------------------------------------------------------
#     Objeto TablaPrisma
# -----------------------------------------------------------------------------
class TablaPrismas(object):
    def __init__(self, name):
        self.name = name
        self.elementos = 0
        self.namePrismas = []
        self.dataPrismas = []  # Arreglo con objetos de clase Prisma

    def registro(self, namePrisma, data):  # Fn para annadir un nuevo registro a un prisma, si no existe, lo crea
        if not (namePrisma in self.namePrismas):
            self.namePrismas.append(namePrisma)
            self.dataPrismas.append(Prisma(namePrisma))  # Crea un nuevo objeto Prisma (vacio) y lo annade
            indice = -1
            self.elementos += 1
            logging.debug("Nuevo prisma encontrado '%s' (%d)", str(namePrisma), self.elementos)
        else:
            indice = self.namePrismas.index(namePrisma)
        newfecha = data[0].strftime('%Y-%m-%d %H:%M:%S')
        myfechasSet = self.dataPrismas[indice].fechasSet
        myfechasList = self.dataPrismas[indice].fechasList
        if newfecha in myfechasSet:
            k = myfechasList.index(newfecha)
            self.dataPrismas[indice].updateRegistro(k, data)
            logging.warning("Fecha repetida '%s', para el prisma '%s', se hace un update del registro.", str(newfecha), str(namePrisma))
        else:
            (self.dataPrismas[indice]).registro(data)

    def getRow(self, p, k):
        return (self.dataPrismas[p]).getRegistro(k)

    def getColumn(self, p, k):
        return (self.dataPrismas[p]).getColumn(k)
