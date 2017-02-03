# -*- coding: utf-8 -*-
"""
@file:  uploadPrismas.py
@date:   Nov,  2016
@author: Arnol
"""

import logging
from osgeo import ogr
ogr.UseExceptions()
# import ClasePrismas as prisma


def uploadPiezometro(tblPzm, connstring, StrEsquema, StrTabla):
    try:
        logging.info("Abriendo conexion a la BD")
        conn = ogr.Open(connstring)
    except Exception:
        logging.exception("Error al tratar de conectarse a la BD con los parametros '%s'", str(connstring))
    else:
        try:

            # Iterar sobre los piezometros
            nroElementos = 1
            for curObjt in tblPzm.dataPiezometro:
                nroRegs = curObjt.elementos

                # Obtener id del objeto desde la BD, si no existe, se crea un nuevo id
                sqlGetid = "select  piezometros.get_idloadpiezometro('%s', %f, %f, %f, %f)" \
                           % (curObjt.nombre_piezometro,
                              curObjt.este, curObjt.norte,
                              curObjt.cota_superficie, curObjt.cota_sensor)
                resultSet = conn.ExecuteSQL(sqlGetid)
                row = resultSet.next()
                objId = row.GetField(0)
                conn.ReleaseResultSet(resultSet)

                # TODO: Actualizar el sql a un INSERT ... ON CONFLICT si se actualiza la BD a la v9.5
                sqlInsertPr = 'INSERT INTO "%s"."%s" ("piezometros_id","fechahora",' \
                              ' "lectura_sensor", "temperatura_sensor", ' \
                              ' "presion_kpa", "presion_mh2o", "presion_nivel_hidrostatico", ' \
                              '"field_1", "field_2", "field_3", "field_4", "field_5", "field_6", "field_7", "field_8", "field_9") ' \
                              'VALUES ' % (StrEsquema, StrTabla)
                sqlOnConflict = ' ON CONFLICT (piezometros_id, fechahora) DO UPDATE ' \
                                ' SET ' \
                                ' piezometros_id = EXCLUDED.piezometros_id,' \
                                ' fechahora = EXCLUDED.fechahora,' \
                                ' lectura_sensor = EXCLUDED.lectura_sensor,' \
                                ' temperatura_sensor = EXCLUDED.temperatura_sensor,' \
                                ' presion_kpa = EXCLUDED.presion_kpa,' \
                                ' presion_mh2o = EXCLUDED.presion_mh2o,' \
                                ' presion_nivel_hidrostatico = EXCLUDED.presion_nivel_hidrostatico,' \
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
                for i in range(nroRegs):
                    currReg = curObjt.getRegistro(i)
                    sqlAux = "(%s, '%s', %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)," \
                             % (objId,
                                currReg[0],
                                # TODO: corregir despues, porque los NULLs e en currReg stan quedando con comillas
                                currReg[1],
                                currReg[2],
                                currReg[3],
                                currReg[4],
                                currReg[5],
                                "NULL",
                                "NULL",
                                "NULL",
                                "NULL",
                                "NULL",
                                "NULL",
                                "NULL",
                                "NULL",
                                "NULL",)
                    sqlInsertPr += sqlAux
                sqlInsertPr = sqlInsertPr[0:-1]
                # Add ON CONFLICT Clause
                sqlInsertPr += sqlOnConflict
                conn.ExecuteSQL(sqlInsertPr)
                logging.info("Piezometro %s cargado exitosamente (%d / %d)",
                             curObjt.nombre_piezometro, nroElementos, tblPzm.elementos)
                nroElementos +=1
            logging.info("Carga finalizada. %d prismas cargados a la BD", nroElementos)
            if conn:
                conn.Destroy()
                logging.info("...Conexion cerrada")
        except Exception:
            logging.exception("Error al tatar de guardar los datos en la BD")
            if conn:
                conn.Destroy()
