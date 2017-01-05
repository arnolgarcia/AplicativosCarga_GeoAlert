__author__ = 'Arnol'


import logging
import ClaseModeloBloque as mb
import datetime as dt


# TODO: Definir el tipo de sensor asociado y la salida de datos estandar para generalizar el nombre del driver,
# ahora dice Mel, pero puede ser un sensor mas general.
def loadMBloque_Mel(filename, nombre, fecha, xl, yl, zl):
    """Carga datos del modelo de bloques de Mel.
    Metodo para extraer los datos del modelo de bloque desde un archivo .csv y guardarlos como objeto *ModeloBloque*.
    :param filename: ruta y nombre del archivo a cargar (datos de mel solamente)
    :type filename: str
    :return: objeto con los datos del modelo de bloque
    :rtype: ModeloBloque
    """

    namefile = filename.split("\\")[-1]
    logging.info("Inicia proceso de carga del modelo de bloque (Mel) desde el archivo '%s'", namefile)
    datos = mb.ModeloBloque(nombre, fecha, xl, yl, zl)
    lineasprocesadas = 0
    # Inicializar todos los valores como NULL, en caso que alguno no venga en el archivo
    xcentre = "NULL"
    ycentre = "NULL"
    zcentre = "NULL"
    xlength = "NULL"
    ylength = "NULL"
    zlength = "NULL"
    litologia = "NULL"
    alteracion = "NULL"
    mineralizacion = "NULL"
    ucs = "NULL"
    rmr = "NULL"
    field1 = "NULL"
    field2 = "NULL"
    field3 = "NULL"
    field4 = "NULL"
    field5 = "NULL"
    field6 = "NULL"
    field7 = "NULL"
    field8 = "NULL"
    field9 = "NULL"
    # Abrir archivo y guardar los registos en el objeto ModeloBloque()
    try:
        with open(filename) as infile:
            infile.seek(0)
            for line in infile:
                Line = line.split("\t")  # El separador es tab en los archivos de Mel
                if Line[0] != "xcentre":  # Saltarse la linea con los encabezados # TODO: ver si hay otra forma mas general de hacerlo

                    # Obtener valores desde el archivo
                    xcentre = Line[0]
                    ycentre = Line[1]
                    zcentre = float(Line[2])
                    xlength = float(Line[3])
                    ylength = float(Line[4])
                    zlength = float(Line[5])
                    litologia = float(Line[6])
                    alteracion = float(Line[7])
                    mineralizacion = float(Line[8])
                    ucs = float(Line[9])
                    rmr = float(Line[10])

                    data = [xcentre, ycentre, zcentre, xlength, ylength, zlength,
                            litologia, alteracion, mineralizacion,
                            ucs,rmr,
                            field1, field2, field3, field4, field5, field6, field7, field8, field9]
                    datos.registro(data)
                    lineasprocesadas += 1
        infile.close()
        logging.info("Carga de datos ok, lineas procesadas %d, puntos encontrados %d", lineasprocesadas, datos.elementos)
    except Exception:
        logging.exception("Error al cargar datos desde archivo \n")
    finally:
        return datos