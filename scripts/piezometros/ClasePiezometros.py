# -*- coding: utf-8 -*-
"""
@file:      ClasePiezometros.py
@version:   1
@date:      Ene,  2017
@author:    Arnol (version 2)
"""

import logging

import linecache
import csv
from osgeo import ogr
from itertools import (takewhile, repeat)


# -----------------------------------------------------------------------------
#     Objetos Registro
# -----------------------------------------------------------------------------
class RegistroPz(object):

    def __init__(self):
        self.fields = ['fechahora',
                       'lectura_sensor', 'temperatura_sensor',
                       'presion_kpa', 'presion_mh2o', 'presion_nivel_hidrostatico']
        self.data = []
        for i in range(len(self.fields)):
            setattr(self, self.fields[i], None)

    def registro(self, data):
        self.data = []
        for i in range(len(self.fields)):
            valor = data[i]
            if i == 0:
                valor = valor.strftime('%Y-%m-%d %H:%M:%S')
            #else:
            #    valor = float(valor)
            setattr(self, self.fields[i], valor)
            self.data.append(valor)

    def getData(self):
        return self.data


# -----------------------------------------------------------------------------
#     Objeto Piezometro
# -----------------------------------------------------------------------------
class Piezometro(object):
    def __init__(self, name, este, norte, cota_sup, cota_sen):
        self.nombre_piezometro = name
        self.este = este
        self.norte = norte
        self.cota_superficie = cota_sup
        self.cota_sensor = cota_sen
        self.elementos = 0  # Numero de registros que tiene el Prisma
        self.datos = []  # Objetos de clase "registro"
        self.fechasSet = set()
        self.fechasList = []

    def registro(self, data):  # Fn para agregar un nuevo registro a Prisma
        reg = RegistroPz()
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
#     Objeto TablaPiezometro
# -----------------------------------------------------------------------------
class TablaPiezometro(object):
    def __init__(self):
        self.elementos = 0
        self.namePiezometro = []
        self.dataPiezometro = []  # Arreglo con objetos de clase Piezometro

    def registro(self, dataInfoPz, dataReg):  # Fn para annadir un nuevo registro a un prisma, si no existe, lo crea
        name = dataInfoPz[0]
        # Crea objeto Piezometro si no existe y lo annade
        if not (name in self.namePiezometro):
            # Crea el objeto
            este = dataInfoPz[1]
            norte = dataInfoPz[2]
            cota_sup = dataInfoPz[3]
            cota_sen = dataInfoPz[4]
            pz = Piezometro(name=name, este=este, norte=norte, cota_sup=cota_sup, cota_sen=cota_sen)
            # Annade el objeto
            self.namePiezometro.append(name)
            self.dataPiezometro.append(pz)
            # Actualiza valores y genera log
            indice = -1
            self.elementos += 1
            logging.debug("Nuevo prisma encontrado '%s' (%d)", str(name), self.elementos)
        else:
            indice = self.namePiezometro.index(name)
        # Annade / Actualiza el registro al objeto Piezometro correspondiente
        newfecha = dataReg[0].strftime('%Y-%m-%d %H:%M:%S')
        myfechasSet = self.dataPiezometro[indice].fechasSet
        myfechasList = self.dataPiezometro[indice].fechasList
        if newfecha in myfechasSet:
            k = myfechasList.index(newfecha)
            self.dataPiezometro[indice].updateRegistro(k, dataReg)
            logging.warning("Fecha repetida '%s', para el prisma '%s', se hace un update del registro.",
                            str(newfecha), str(name))
        else:
            (self.dataPiezometro[indice]).registro(dataReg)

    def getRow(self, p, k):
        return (self.dataPiezometro[p]).getRegistro(k)

    def getColumn(self, p, k):
        return (self.dataPiezometro[p]).getColumn(k)