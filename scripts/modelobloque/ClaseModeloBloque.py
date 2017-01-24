__author__ = 'Arnol'


import logging
import linecache
import csv
from osgeo import ogr


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
        aux = str(aux).replace("[", "{").replace("]", "}")
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
        self.fields = ['xcentre', 'ycentre', 'zcentre',
                       'xlength', 'ylength', 'zlength',
                       'litologia', 'alteracion', 'minzone',
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
        aux = str(aux).replace("[", "{").replace("]", "}")
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
            self.data.append(data[i])

    def getData(self):
        return self.data


# -----------------------------------------------------------------------------
#     Objeto ModeloBloque
# -----------------------------------------------------------------------------
class ModeloBloque(object):
    def __init__(self, name, objReg, fecha, xlength, ylength, zlength, toFile=False, tempfile=None,
                 mybatch=10000):
        self.name = name
        self.objetoRegistro = objReg
        self.sqlRegistro = objReg
        self.sqlString = ""
        self.sqlIteracion = 0
        self.sqlNroBatch = 0
        self.toFile = toFile
        self.batch = mybatch
        self.tempfile = tempfile
        self.sep = ","
        self.header = False
        self.puntos = 0  # Numero de registros que tiene el Modelo de Bloques
        self.datos = []  # Array de Objetos de clase "registro"
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
            data = []
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
        if self.toFile & len(self.datos) > 0:
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
        # si la ultima linea no termina con un enter, sumar 1 al numero de puntos
        # si el archivo tiene encabezado restar una fila
        if self.header:
            self.puntos += -1
        lastReg = self.getRegistro(self.puntos)
        if len(lastReg) <= 1:
            self.puntos += -1

    def saveToBD(self, connStr, tableName, schemaName, batchSQL=10000):
        try:
            # Testear conexion
            logging.info("Abriendo conexion a la BD")
            conn = ogr.Open(connStr)
            if conn:
                conn.Destroy()
        except Exception:
            logging.exception("Error al tratar de conectarse a la BD con los parametros '%s'", str(connStr))
        else:
            regDB = RegistroMB_DB()
            self.sqlRegistro = regDB
            logging.debug("Conexion exitosa, empieza carga de archivos...")
            # Cargar datos desde archivo
            if self.toFile:
                logging.info("Iniciando carga desde archivo '%s'", self.tempfile)
                # TODO: completar...
                try:
                    with open(self.tempfile) as infile:
                        infile.seek(0)
                        lineaNro = 0
                        for line in infile:
                            lineaNro += 1
                            if not self.header or lineaNro > 1:
                                Line = line.split(self.sep)
                                data = [float(k) for k in Line]
                                self.objetoRegistro.registro(data)
                                regDB = self.objetoRegistro.registroToDB()
                                vals = regDB.getData()
                                self.runSQL(connStr, schemaName, tableName, vals, batchSQL)
                    logging.info("Carga de datos ok, lineas procesadas %d, puntos encontrados %d",
                                 lineaNro, self.puntos)
                except Exception:
                    logging.exception("Error al cargar datos desde archivo \n")
            else:
                logging.debug("Iniciando carga desde memoria")
        finally:
            logging.info("Proceso de carga finalizado.")
            if conn:
                conn.Destroy()

    def runSQL(self, connstr, str_esquema, str_tabla, valores, batch_size=10000):
        self.sqlIteracion += 1
        valores = str(valores).replace("[", "(").replace("]", ")")  # Convertir 'valores' a Array y reemplazar [] por {}
        self.sqlString += valores
        if (self.sqlIteracion % batch_size == 0) or (self.sqlIteracion == self.puntos):
            # Cargar datos a BD y reiniciar iteracion
            self.load2db(connstr, str_esquema, str_tabla)
        else:
            self.sqlString += ", "
        # Resetear valores una vez cargado todo
        if self.sqlIteracion == self.puntos:
            self.sqlIteracion = 0
            self.sqlNroBatch = 0

    def load2db(self, connStr, toSchema, toTable):
        self.sqlNroBatch += 1
        logging.debug("cargando bacth nro: %d (%d/%d elementos cargados)...",
                      self.sqlNroBatch, self.sqlIteracion, self.puntos)
        self.sqlString = self.getSqlInsert(toSchema, toTable) + ' VALUES ' + self.sqlString + ' ' \
                         + self.getSqlConflict()
        try:
            conn = ogr.Open(connStr)
            conn.ExecuteSQL(self.sqlString)
        except Exception as e:
            logging.error("Error en batch %s al tratar de conectarse a la BD con los parametros '%s'. \n %s",
                          str(self.sqlNroBatch), str(connStr), str(e))
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

    def getSqlInsert(self, toSchema, toTable):
        campos = str(self.sqlRegistro.fields).replace("'", "\"").replace("[", "(").replace("]", ")")
        sqlInsert = 'INSERT INTO "%s"."%s" %s ' % (toSchema, toTable, campos)
        return sqlInsert

    def getSqlConflict(self):
        campos = self.sqlRegistro.fields
        mylist = []
        for i in range(len(campos)):
            mylist.append(campos[i] + " = EXCLUDED." + campos[i])
        excluded = str(mylist).replace("'", "").replace("[", "").replace("]", "")
        sqlConflict = " ON CONFLICT %s  DO UPDATE SET %s ;" % (self.objetoRegistro.llave, excluded)
        return sqlConflict




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


def getSqlInsert(tbName, scName, camposArray):
    campos = str(camposArray).replace("'", "\"").replace("[", "(").replace("]", ")")
    sqlInsert = 'INSERT INTO "%s"."%s" %s ' % (scName, tbName, campos)
    return sqlInsert


def getSqlConflict(llave, campos):
    mylist = []
    for i in range(len(campos)):
        mylist.append(campos[i] + " = EXCLUDED." + campos[i])
    excluded = str(mylist).replace("'", "").replace("[", "").replace("]", "")
    sqlConflict = " ON CONFLICT %s  DO UPDATE SET %s ;" % (llave, excluded)
    return sqlConflict


def load2PostgresDB(connStr, stringSQL):
    logging.debug("cargando bacth a la bd")
    try:
        conn = ogr.Open(connStr)
        conn.ExecuteSQL(stringSQL)
        logging.debug("... batch cargado")
        if conn:
            conn.Destroy()
    except Exception as e:
        logging.error("Error al cargar batch con los parametros '%s'", str(connStr))
        logging.error("Error:  '%s'", str(e.message))
