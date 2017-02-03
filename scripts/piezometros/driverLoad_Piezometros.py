# -*- coding: utf-8 -*-
"""
@file:   driverLoad_Prisma.py
@date:   Nov,  2016
@author: Arnol
"""

import logging
import ClasePiezometros as pz
import datetime as dt


# TODO: Definir el tipo de sensor asociado y la salida de datos estandar para generalizar el nombre del driver,
def loadPiezometros_Mel(filename):

    namefile = filename.split("\\")[-1]
    logging.info("Inicia proceso de carga de prismas (Mel) desde el archivo '%s'", namefile)
    datos = pz.TablaPiezometro()
    lineasprocesadas = 0

    # Datos no incluidos en el archivo de Chuquicamata
    lect_sensor = "NULL"
    temp_sensor = "NULL"
    presion_kpa = "NULL"
    presion_mh2o = "NULL"
    field1 = "NULL"
    field2 = "NULL"
    field3 = "NULL"
    field4 = "NULL"
    field5 = "NULL"
    field6 = "NULL"
    field7 = "NULL"
    field8 = "NULL"
    field9 = "NULL"
    # Abrir archivo y guardar los registos en el objeto TablaPrismas()
    try:
        with open(filename) as infile:
            infile.seek(0)
            for line in infile:
                Line = line.split("\t")  # El separador es coma en los archivos de Mel
                if ((Line[0] != "ID_PIEZOMETRO") & (len(Line) == 10)):  # Saltarse la linea con los encabezados

                    # Obtener valores desde el archivo
                    try:
                        nombrePz = Line[0]
                        fechahora = Line[1]
                        anno = cast2floatDB(Line[2], [nombrePz, fechahora, 'anno'])
                        gw_elevation = cast2floatDB(Line[3], [nombrePz, fechahora, 'gw_elevation'])
                        utm_este = cast2floatDB(Line[4], [nombrePz, fechahora, 'utm_este'])
                        utm_norte = cast2floatDB(Line[5], [nombrePz, fechahora, 'utm_norte'])
                        mina_x = cast2floatDB(Line[6], [nombrePz, fechahora, 'mina_x'])
                        mina_y = cast2floatDB(Line[7], [nombrePz, fechahora, 'mina_y'])
                        cota_sup = cast2floatDB(Line[8], [nombrePz, fechahora, 'cota_sup'])
                        cota_sen = cast2floatDB(Line[9], [nombrePz, fechahora, 'cota_sen'])
                    except:
                        logging.exception("ERROR al convertir datos")

                    # Formatear fechas y horas
                    try:
                        fechahora = dt.datetime.strptime(fechahora, '%d-%m-%Y %H:%M')
                    except:
                        logging.exception("ERROR al convertir fecha")

                    dataInfoPz = [nombrePz, utm_este, utm_norte, cota_sup, cota_sen]
                    dataReg = [fechahora,
                               lect_sensor, temp_sensor,
                               presion_kpa, presion_mh2o, gw_elevation]

                    datos.registro(dataInfoPz=dataInfoPz, dataReg=dataReg)
                    lineasprocesadas += 1
        infile.close()
        logging.info("Carga de datos ok, lineas procesadas %d, prismas encontrados %d", lineasprocesadas, datos.elementos)
    except Exception as e:
        logging.exception("Error al cargar datos desde archivo")
    finally:
        return datos


def cast2floatDB(variable, id_registro=None):
    try:
        newVar = float(variable)
    except ValueError:
        logging.debug("No se pudo convertir el valor '%s'. Id de registro: %s", variable, id_registro)
        newVar = 'NULL'
    return newVar
