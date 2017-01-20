# -*- coding: utf-8 -*-
"""
@file:  uploadPrismas.py
@date:   Nov,  2016
@author: Arnol
"""

# TODO: actualiza a mbloque, aun esta como prismas
import ClaseModeloBloque as mb
import scripts.DB_connection.ClaseBatchSQL as btch
import logging
from osgeo import ogr
ogr.UseExceptions()


# Driver para cargar los datos de Collahuasi directo desde el archivo
def uploadMbFromFile_CMDIC(fullFileName, connString, strEsquema, strTabla, batch=1):

    logging.info("Inicia proceso de carga del modelo de bloque (CMDIC) desde el archivo '%s'", fullFileName)
    lineasprocesadas = 0

    # Inicialización del boque y del batch si batch es distinto de 0 TODO
    mybloque = mb.RegistroMB_DB()
    mybatch = btch.BatchSQL(connString, strTabla, strEsquema, mybloque, batch)

    try:
        # Testear conexion
        logging.info("Abriendo conexion a la BD")
        conn = ogr.Open(connString)
        if conn:
            conn.Destroy()
    except Exception:
        logging.exception("Error al tratar de conectarse a la BD con los parametros '%s'", str(connString))
    else:
        logging.debug("Conexion exitosa, empieza carga de archivos...")
        try:
            with open(fullFileName) as infile:
                infile.seek(0)

                for line in infile:
                    Line = line.split(",")  # El separador en los archivos de CMDIC
                    # TODO: ver si hay otra forma mas general de hacer lo siguiente
                    if str(Line[0]).lower() != "xcentre":  # Saltarse la linea con los encabezados
                        data = [float(k) for k in Line]
                        # Asignar datos al objeto RegistroMB
                        mybloqueCMDIC = mb.RegistroMB_CMDIC()
                        mybloqueCMDIC.registro(data)
                        mybloque = mybloqueCMDIC.registroToDB()
                        lineasprocesadas += 1
                        mybatch.run(mybloque.getData())
            logging.info("Carga de datos ok, lineas procesadas %d, puntos encontrados %d", lineasprocesadas, mybloque.puntos)
        except Exception:
            logging.exception("Error al cargar datos desde archivo \n")
        finally:
            return mybloque


def uploadMBloque(mbloque, connstring, StrEsquema, StrTabla, batch = 0):
    try:
        logging.info("Abriendo conexion a la BD")
        conn = ogr.Open(connstring)
    except Exception:
        logging.exception("Error al tratar de conectarse a la BD con los parametros '%s'", str(connstring))
    else:
        try:
            nroPuntos = mbloque.puntos

            sqlInsert = 'INSERT INTO "%s"."%s" ("load_prismas_id","fechahora","fecha","hora",' \
                        ' "norte", "este", "altura", "distancia", "hz", "v", "hor_distancia",' \
                        ' "field_1", "field_2", "field_3", "field_4", "field_5", "field_6", "field_7", "field_8", "field_9") ' \
                        ' VALUES ' % (StrEsquema, StrTabla)
            sqlOnConflict = ' ON CONFLICT (load_prismas_id, fechahora) DO UPDATE ' \
                            ' SET ' \
                            ' load_prismas_id = EXCLUDED.load_prismas_id,' \
                            ' fechahora = EXCLUDED.fechahora,' \
                            ' fecha = EXCLUDED.fecha,' \
                            ' hora = EXCLUDED.hora,' \
                            ' norte = EXCLUDED.norte,' \
                            ' este = EXCLUDED.este,' \
                            ' altura = EXCLUDED.altura,' \
                            ' distancia = EXCLUDED.distancia,' \
                            ' hz = EXCLUDED.hz,' \
                            ' v = EXCLUDED.v,' \
                            ' hor_distancia = EXCLUDED.hor_distancia,' \
                            ' field_1 = EXCLUDED.field_1,' \
                            ' field_2 = EXCLUDED.field_2,' \
                            ' field_3 = EXCLUDED.field_3,' \
                            ' field_4 = EXCLUDED.field_4,' \
                            ' field_5 = EXCLUDED.field_5,' \
                            ' field_6 = EXCLUDED.field_6,' \
                            ' field_7 = EXCLUDED.field_7,' \
                            ' field_8 = EXCLUDED.field_8,' \
                            ' field_9 = EXCLUDED.field_9' \
                            ';'

            for i in range(nroPuntos):
                mybloque = mbloque.getRegistro(i)

                # TODO hacer for para insertar en batch
                if batch == 0:
                    batch = mbloque.puntos


                for i in range(prismaN):
                    registroPrisma = myprisma.getRegistro(i)
                    sqlAux = "(%s, '%s', '%s', '%s', %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)," \
                             % (prismaId,
                                registroPrisma[0],
                                registroPrisma[1],
                                registroPrisma[2],
                                registroPrisma[3],
                                registroPrisma[4],
                                registroPrisma[5],
                                registroPrisma[6],
                                registroPrisma[7],
                                registroPrisma[8],
                                registroPrisma[9],
                                registroPrisma[10],
                                registroPrisma[11],
                                registroPrisma[12],
                                registroPrisma[13],
                                registroPrisma[14],
                                registroPrisma[15],
                                registroPrisma[16],
                                registroPrisma[17],
                                registroPrisma[18])
                    sqlInsertPr += sqlAux
                sqlInsertPr = sqlInsertPr[0:-1]
                # Add ON CONFLICT Clause
                sqlInsertPr += sqlOnConflict
                conn.ExecuteSQL(sqlInsertPr)
                logging.info("Prisma %s cargado exitosamente (%d / %d)", str(prismaName), prism+1, nroPrismas)
            logging.info("Carga finalizada. %d prismas cargados a la BD", nroPrismas)
            if conn:
                conn.Destroy()
                logging.info("...Conexion cerrada")
        except Exception:
            logging.exception("Error al tatar de guardar los datos en la BD")




def test(mbloque, connstring, StrEsquema, StrTabla, batch = 0):
    try:
        logging.info("Abriendo conexion a la BD")
        conn = ogr.Open(connstring)
    except Exception:
        logging.exception("Error al tratar de conectarse a la BD con los parametros '%s'", str(connstring))
    else:
        try:
            nroPuntos = mbloque.puntos
            for i in range(nroPuntos):
                mybloque = mbloque.getRegistro(i)

                # TODO hacer for para insertar en batch
                if batch == 0:
                    batch = mbloque.puntos

                # TODO: aca voy...

                # TODO: Actualizar el sql a un INSERT ... ON CONFLICT si se actualiza la BD a la v9.5
                sqlInsertPr = 'INSERT INTO "%s"."%s" ("load_prismas_id","fechahora","fecha","hora",' \
                              ' "norte", "este", "altura", "distancia", "hz", "v", "hor_distancia",' \
                              '"field_1", "field_2", "field_3", "field_4", "field_5", "field_6", "field_7", "field_8", "field_9") ' \
                              'VALUES ' % (StrEsquema, StrTabla)
                sqlOnConflict = ' ON CONFLICT (load_prismas_id, fechahora) DO UPDATE ' \
                                ' SET ' \
                                ' load_prismas_id = EXCLUDED.load_prismas_id,' \
                                ' fechahora = EXCLUDED.fechahora,' \
                                ' fecha = EXCLUDED.fecha,' \
                                ' hora = EXCLUDED.hora,' \
                                ' norte = EXCLUDED.norte,' \
                                ' este = EXCLUDED.este,' \
                                ' altura = EXCLUDED.altura,' \
                                ' distancia = EXCLUDED.distancia,' \
                                ' hz = EXCLUDED.hz,' \
                                ' v = EXCLUDED.v,' \
                                ' hor_distancia = EXCLUDED.hor_distancia,' \
                                ' field_1 = EXCLUDED.field_1,' \
                                ' field_2 = EXCLUDED.field_2,' \
                                ' field_3 = EXCLUDED.field_3,' \
                                ' field_4 = EXCLUDED.field_4,' \
                                ' field_5 = EXCLUDED.field_5,' \
                                ' field_6 = EXCLUDED.field_6,' \
                                ' field_7 = EXCLUDED.field_7,' \
                                ' field_8 = EXCLUDED.field_8,' \
                                ' field_9 = EXCLUDED.field_9' \
                                ';'
                for i in range(prismaN):
                    registroPrisma = myprisma.getRegistro(i)
                    sqlAux = "(%s, '%s', '%s', '%s', %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)," \
                             % (prismaId,
                                registroPrisma[0],
                                registroPrisma[1],
                                registroPrisma[2],
                                registroPrisma[3],
                                registroPrisma[4],
                                registroPrisma[5],
                                registroPrisma[6],
                                registroPrisma[7],
                                registroPrisma[8],
                                registroPrisma[9],
                                registroPrisma[10],
                                registroPrisma[11],
                                registroPrisma[12],
                                registroPrisma[13],
                                registroPrisma[14],
                                registroPrisma[15],
                                registroPrisma[16],
                                registroPrisma[17],
                                registroPrisma[18])
                    sqlInsertPr += sqlAux
                sqlInsertPr = sqlInsertPr[0:-1]
                # Add ON CONFLICT Clause
                sqlInsertPr += sqlOnConflict
                conn.ExecuteSQL(sqlInsertPr)
                logging.info("Prisma %s cargado exitosamente (%d / %d)", str(prismaName), prism+1, nroPrismas)
            logging.info("Carga finalizada. %d prismas cargados a la BD", nroPrismas)
            if conn:
                conn.Destroy()
                logging.info("...Conexion cerrada")
        except Exception:
            logging.exception("Error al tatar de guardar los datos en la BD")