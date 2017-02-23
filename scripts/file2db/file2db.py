__author__ = 'Arnol'

import logging
from osgeo import ogr
import os.path
from itertools import (takewhile, repeat)


# -----------------------------------------------------------------------------
#     Objeto PostgreSQLcon
# -----------------------------------------------------------------------------
class PostgreSQLcon(object):

    def __init__(self, connstr, tablename, schename):
        self.connstr = connstr
        self.tblname = tablename
        self.schname = schename

    def testconn(self):
        try:
            # Testear conexion
            logging.info("Testeando conexion a PostgreSQL: %s", self.connstr)
            conn = ogr.Open(self.connstr)
            logging.info("conexion exitosa..")
            if conn:
                conn.Destroy()
        except Exception:
            logging.exception("Error al tratar de conectarse a la BD")
            return -1
        try:
            # Verificar que schema.table existe
            sqlCheck = "SELECT " \
                       " COUNT(*) " \
                       "FROM " \
                       " information_schema.tables " \
                       "WHERE " \
                       " TABLE_SCHEMA = '%s' AND " \
                       "TABLE_NAME = '%s' ;" % (self.schname, self.tblname)
            conn = ogr.Open(self.connstr)
            resultSet = conn.ExecuteSQL(sqlCheck)
            row = resultSet.next()
            intExiste = row.GetField(0)
            conn.ReleaseResultSet(resultSet)
            if intExiste > 0:
                logging.info("La tabla %s.%s SI existe en la bd", self.schname, self.tblname)
                return 1
            else:
                logging.info("La tabla %s.%s NO existe en la bd", self.schname, self.tblname)
                return -1
        except Exception:
            logging.exception("Error al consultar si la tabla existe")
            return -1


# -----------------------------------------------------------------------------
#     Objeto PostgreSQLcon
# -----------------------------------------------------------------------------
class runSQL(object):

    def __init__(self, objetoCon, fields, llave, batch_size, MaxPuntos):
        self.connstr = objetoCon.connstr
        self.tblname = objetoCon.tblname
        self.schname = objetoCon.schname
        self.fields = fields
        self.llave = llave
        self.batch_size = batch_size
        self.MaxPuntos = MaxPuntos
        self.sqlNroBatch = 0
        self.sqlIteracion = 0
        self.sqlString = ""

    def loadBatch(self, valores):
        self.sqlIteracion += 1
        valores = str(valores).replace("[", "(").replace("]", ")")  # Convertir 'valores' a Array y reemplazar [] por {}
        self.sqlString += valores
        if (self.sqlIteracion % self.batch_size == 0) or (self.sqlIteracion == self.MaxPuntos):
            # Cargar datos a BD y reiniciar iteracion
            self.load()
        else:
            self.sqlString += ", "
        # Resetear valores una vez cargado to.do
        if self.sqlIteracion == self.MaxPuntos:
            self.sqlIteracion = 0
            self.sqlNroBatch = 0

    def load(self):
        self.sqlNroBatch += 1
        logging.debug("cargando bacth nro: %d (%d/%d elementos por cargar)...",
                      self.sqlNroBatch, self.sqlIteracion, self.MaxPuntos)
        # Construct SQL
        InsertPart = self.getSqlInsert()
        ValuePart = self.sqlString
        OnConflictPart = self.getSqlConflict()
        self.sqlString = InsertPart + ' VALUES ' + ValuePart + OnConflictPart

        try:
            conn = ogr.Open(self.connstr)
            conn.ExecuteSQL(self.sqlString)
        except Exception as e:
            logging.ERROR("Error en batch %s al tratar de conectarse a la BD con los parametros '%s'. \n %s",
                          str(self.sqlNroBatch), str(self.connstr), str(e))
            raise Exception
        else:
            logging.debug("... batch cargado")
        finally:
            # Cerrar conexion si esta abierta
            if conn:
                conn.Destroy()
                logging.debug("Conexion cerrada en clausula 'finally'")
            # Resetear String SQL
            self.sqlString = ""

    def getSqlInsert(self):
        campos = str(self.fields).replace("'", "\"").replace("[", "(").replace("]", ")")
        sqlInsert = 'INSERT INTO "%s"."%s" %s ' % (self.schname, self.tblname, campos)
        return sqlInsert

    def getSqlConflict(self):
        campos = self.fields
        mylist = []
        for i in range(len(campos)):
            mylist.append(campos[i] + " = EXCLUDED." + campos[i])
        excluded = str(mylist).replace("'", "").replace("[", "").replace("]", "")
        sqlConflict = " ON CONFLICT %s  DO UPDATE SET %s ;" % (self.llave, excluded)
        return sqlConflict


# -----------------------------------------------------------------------------
#     Funciones para cargar datos a a BD desde un archivo plano
# -----------------------------------------------------------------------------
def saveFile2DB(ObjConn, filename, fields, positions, llave, sep, header, batchSQL=10000):

    # Chequear validez del ObjConn
    # TODO: implementar verificacion

    # Chequear consistencia del archivo
    ckExists = checkFileExists(filename)
    ckPositions = checkFilePositions(filename)
    if not (ckExists and ckPositions):
        logging.error("El archivo entregado no es valido")
        return

    # Setear el numero de puntos
    f = open(filename, 'rb')
    bufgen = takewhile(lambda x: x, (f.read(1024*1024) for _ in repeat(None)))
    nro_puntos = sum(buf.count(b'\n') for buf in bufgen if buf)
    if header:
        nro_puntos -= 1

    # Crear Objeto para cargar datos
    loadData = runSQL(ObjConn, fields, llave, batchSQL, nro_puntos)

    try:
        with open(filename) as infile:
            infile.seek(0)
            lineaNro = 0
            for line in infile:
                lineaNro += 1
                if not header or lineaNro > 1:
                    Line = line.split(sep)
                    # data = [float(k) for k in Line]
                    data = Line
                    vals = parseData(data, positions)
                    loadData.loadBatch(valores=vals)

        logging.info("Carga de datos ok, lineas procesadas %d, puntos encontrados %d",
                     lineaNro, nro_puntos)
    except Exception:
        logging.exception("Error al cargar datos desde archivo \n")


def checkFileExists(file_name):
    return os.path.isfile(file_name)


def checkFilePositions(file_name):
    # TODO: implementar este metodo
    return os.path.isfile(file_name)


def parseData(data, positions):
    ParsedData = []
    for pos in positions:
        elemento = data[pos].replace('"', '').replace("\n", "")
        ParsedData.append(elemento)
    return ParsedData
