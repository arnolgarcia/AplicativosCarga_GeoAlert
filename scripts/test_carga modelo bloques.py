__author__ = 'Arnol'


import scripts.modelobloque.ClaseModeloBloque as mb

from osgeo import ogr
ogr.UseExceptions()

import logging
logging.basicConfig(format='%(levelname)s-%(asctime)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.DEBUG)

"""
# Carga datos de CMDIC
aux = mb.ModeloBloque(name="cmdic", objReg=mb.RegistroMB_CMDIC(),
                      fecha='2017-01-01',
                      xlength=10, ylength=10, zlength=15)
print aux.puntos
aux.setFile("C:/Users/Arnol/Gesecology/[Demo] GeoAlert - Collahuasi/Data/ModeloBloque/rosmp_fc_15sep16_geom_v2.asc", sep=",", hasheader=True)
print aux.puntos
"""


# Carga datos de MEL
aux = mb.ModeloBloque(name="mel", objReg=mb.RegistroMB_MEL(),
                      fecha='2017-01-01',
                      xlength=25, ylength=25, zlength=15)
print aux.puntos
aux.setFile("C:/Users/Arnol/Desktop/copia Data MEL/ModeloBloque/modelo_bloques.csv", sep=",", hasheader=True)
print aux.puntos


connStr = "PG: host='%s' port='%s' dbname='%s' user='%s' password='%s'" % ("152.231.85.227",
                                                                           "5432",
                                                                           "geoalert_template",
                                                                           "postgres",
                                                                           "Admin321")
sc = "modelo_bloques"
tb = "bloques"
aux.saveToBD(connStr=connStr, tableName=tb, schemaName=sc, batchSQL=20000)



#aux.setFile("C:/Users/Arnol/Gesecology/[Demo] GeoAlert - Collahuasi/Data/ModeloBloque/mb_cmdic_to_mel.txt", sep=",", hasheader=False)
#aux.setFile("C:/Users/Arnol/Gesecology/[Demo] GeoAlert - Collahuasi/Data/ModeloBloque/test.txt", sep=",", hasheader=True)
