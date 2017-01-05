# -*- coding: utf-8 -*-
"""
@file:   driverLoad_Prisma.py
@date:   Nov,  2016
@author: Arnol
"""

import logging
import ClasePrismas as pr
import datetime as dt


# TODO: Definir el tipo de sensor asociado y la salida de datos estandar para generalizar el nombre del driver,
# ahora dice Chuqui, pero puede ser un sensor mas general.
def loadPrisma_Chuqui(filename):
    """Carga datos de prismas de Chuqicamata.
    Metodo para extraer los datos de prisma desde un archivo .csv y guardarlos como objeto *TablaPrismas*.
    :param filename: ruta y nombre del archivo a cargar (datos de chuquicamata solamente)
    :type filename: str
    :return: objeto con los datos de prismas
    :rtype: TablaPrismas
    """

    namefile = filename.split("\\")[-1]
    logging.info("Inicia proceso de carga de prismas (Chuquicamata) desde el archivo '%s'", namefile)
    datos = pr.TablaPrismas("mitabla")
    lineasprocesadas = 0
    # Datos no incluidos en el archivo de Chuquicamata
    hz = "NULL"
    v = "NULL"
    hor_distancia = "NULL"
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
                Line = line.split(",")  # El separador es coma en los archivos de Chuqui
                if Line[0] != "NAME":  # Saltarse la linea con los encabezados

                    # Obtener valores desde el archivo
                    nombrePrisma = Line[0]
                    fecha = Line[1]
                    hora = Line[2]
                    este = float(Line[3])
                    norte = float(Line[4])
                    altura = float(Line[5])
                    distancia = float(Line[6])
                    fechahora = fecha + " " + hora

                    # Formatear fechas y horas
                    fechahora = dt.datetime.strptime(fechahora, '%d-%m-%Y %H:%M:%S')
                    fecha = fechahora.date()
                    hora = fechahora.time()


                    data = [fechahora, fecha, hora, norte, este, altura, distancia, hz, v, hor_distancia,
                            field1, field2, field3, field4, field5, field6, field7, field8, field9]
                    datos.registro(nombrePrisma, data)
                    lineasprocesadas += 1
        infile.close()
        logging.info("Carga de datos ok, lineas procesadas %d, prismas encontrados %d", lineasprocesadas, datos.elementos)
    except Exception:
        logging.exception("Error al cargar datos desde archivo \n")
    finally:
        return datos


def loadPrisma_Mel(filename):
    """Carga datos de prismas de Mel.
    Metodo para extraer los datos de prisma desde un archivo .csv y guardarlos como objeto *TablaPrismas*.
    :param filename: ruta y nombre del archivo a cargar (datos de mel solamente)
    :type filename: str
    :return: objeto con los datos de prismas
    :rtype: TablaPrismas
    """

    namefile = filename.split("\\")[-1]
    logging.info("Inicia proceso de carga de prismas (Mel) desde el archivo '%s'", namefile)
    datos = pr.TablaPrismas("mitabla")
    lineasprocesadas = 0
    # Inicializar todos los valores como NULL, en caso que alguno no venga en el archivo
    nombrePrisma = "NULL"
    fechahora = "NULL"
    fecha = "NULL"
    hora = "NULL"
    norte = "NULL"
    este = "NULL"
    altura = "NULL"
    distancia = "NULL"
    hz = "NULL"
    v = "NULL"
    hor_distancia = "NULL"
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
                Line = line.split("\t")  # El separador es tab en los archivos de Mel
                if Line[0] != "Point ID":  # Saltarse la linea con los encabezados

                    # Obtener valores desde el archivo
                    nombrePrisma = Line[0]
                    fechahora = Line[1]
                    este = float(Line[2])
                    norte = float(Line[3])
                    altura = float(Line[4])
                    distancia = float(Line[5])
                    hz = float(Line[6])
                    v = float(Line[7])
                    hor_distancia = float(Line[8])

                    # Formatear fechas y horas
                    fechahora = dt.datetime.strptime(fechahora, '%d/%m/%Y %H:%M:%S')
                    fecha = fechahora.date()
                    hora = fechahora.time()

                    data = [fechahora, fecha, hora, norte, este, altura, distancia, hz, v, hor_distancia,
                            field1, field2, field3, field4, field5, field6, field7, field8, field9]
                    datos.registro(nombrePrisma, data)
                    lineasprocesadas += 1
        infile.close()
        logging.info("Carga de datos ok, lineas procesadas %d, prismas encontrados %d", lineasprocesadas, datos.elementos)
    except Exception:
        logging.exception("Error al cargar datos desde archivo \n")
    finally:
        return datos
