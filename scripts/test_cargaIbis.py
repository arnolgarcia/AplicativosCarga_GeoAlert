__author__ = 'Arnol'

import logging
logging.basicConfig(format='%(levelname)s-%(asctime)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.DEBUG)

import scripts.file2db.file2db as f2db



# Crear objeto de conexion
conStr = "PG: host='%s' port='%s' dbname='%s' user='%s' password='%s'" % ("152.231.85.227",
                                                                          "5432",
                                                                          "geoalert_template",
                                                                          "postgres",
                                                                          "Admin321")

"""
tblName = "radar_puntos"
schName = "radar_ibis"

myObj = f2db.PostgreSQLcon(conStr, tblName, schName)
myObj.testconn()


# Cargar datos a la bd (ibis_puntos)
filename = "C:\Users\Arnol\Desktop\copia Data MEL\Radar Ibis\\test_mel\ibis_puntos_mel.txt"
fields = ["id", "radar_proyectos_id", "x", "y", "geom"]
positions = [1, 2, 3, 4, 5]
types = ["int", "int", "float", "float", "geometry"]
llave = "(id)"
sep = "\t"
header = True
batchSQL = 10000

f2db.saveFile2DB(myObj, filename, fields, positions, llave, sep, header, batchSQL)


"""


schName = "radar_ibis"
tblName = "radar_consolidado"

myObj = f2db.PostgreSQLcon(conStr, tblName, schName)
myObj.testconn()

# Cargar datos a la bd (ibis_consolidado_dia_test_mel)
filename = "C:\Users\Arnol\Desktop\copia Data MEL\Radar Ibis\\test_mel\ibis_consolidado_dia_test_mel.txt"
fields = ["radar_puntos_id", "x", "y", "geom", "fechahora", "deformacion_instantanea", "deformacion_acumulada"]
positions = [7, 3, 4, 6, 1, 5, 8]
# types = ["int", "float", "float", "geometry", "timestamp", "float"]
llave = "(x, y, fechahora)"
sep = "\t"
header = True
batchSQL = 15000

f2db.saveFile2DB(myObj, filename, fields, positions, llave, sep, header, batchSQL)
