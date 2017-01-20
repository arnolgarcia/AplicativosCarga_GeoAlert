__author__ = 'Arnol'

from osgeo import ogr
import logging


# -----------------------------------------------------------------------------
#     Objeto BatchSQL
# -----------------------------------------------------------------------------
class BatchSQL(object):

    def __init__(self, connstr, str_tabla, str_esquema, objeto, batch_size):
        """
        Clase para almacenar en un string el sql a insertar a la BD
        :param
        :return:
        """
        self.connStr = connstr
        self.toTable = str_tabla
        self.toSchema = str_esquema
        self.myObjeto = objeto
        self.batchSize = batch_size
        self.batchNro = 0
        self.iteracion = 0
        self.insertSQL = self.getSqlInsert()
        self.conflictSQL = self.getSqlConflict()
        self.stringSQL = ""

    def run(self, valores):
        self.iteracion += 1
        if self.iteracion == 1:
            self.stringSQL = self.insertSQL + ' VALUES '
        valores = str(valores).replace("[", "(").replace("]", ")")  # Convertir 'valores' a texto y reemplazar [] por ()
        self.stringSQL += valores
        if self.iteracion == self.batchSize:
            # Agrega clausula ON CONFLICT
            self.stringSQL += " " + self.conflictSQL
            # Cargar datos a BD y reiniciar iteracion
            self.load2db()
            self.iteracion = 0
        else:
            self.stringSQL += ", "

    def load2db(self):
        self.batchNro += 1
        logging.debug("cargando bacth nro: %s...", str(self.batchNro))
        try:
            conn = ogr.Open(self.connStr)
            conn.ExecuteSQL(self.stringSQL)
            logging.debug("... batch cargado")
            if conn:
                conn.Destroy()
        except Exception as e:
            logging.error("Error en batch %s al tratar de conectarse a la BD con los parametros '%s'",
                              str(self.batchNro), str(self.connStr))
            logging.error("Error:  '%s'", str(e.message))

    def getSqlInsert(self):
        campos = str(self.myObjeto.fields).replace("'", "\"").replace("[", "(").replace("]", ")")
        sqlInsert = 'INSERT INTO "%s"."%s" %s ' % (self.toSchema, self.toTable, campos)
        return  sqlInsert

    def getSqlConflict(self):
        campos = self.myObjeto.fields
        mylist = []
        for i in range(len(campos)):
            mylist.append(campos[i] + " = EXCLUDED." + campos[i])
        excluded = str(mylist).replace("'", "").replace("[", "").replace("]", "")
        sqlConflict = " ON CONFLICT %s  DO UPDATE SET %s ;" % (self.myObjeto.llave, excluded)
        return sqlConflict


# -----------------------------------------------------------------------------
#     Objeto BatchSQL
# -----------------------------------------------------------------------------
class RegistroSql(object):

    def __init__(self, connstr, str_tabla, str_esquema, objeto, batch_size):
        """
        Clase para almacenar en un string el sql a insertar a la BD
        :param
        :return:
        """
        self.connStr = connstr
        self.toTable = str_tabla
        self.toSchema = str_esquema
        self.myObjeto = objeto
        self.batchSize = batch_size
        self.batchNro = 0
        self.iteracion = 0
        self.insertSQL = self.getSqlInsert()
        self.conflictSQL = self.getSqlConflict()
        self.stringSQL = ""