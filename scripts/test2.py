__author__ = 'Arnol'


import modelobloque.ClaseModeloBloque as mb
import modelobloque.uploadMBloque as dr


myFile = "C:/Users/Arnol/Gesecology/[Demo] GeoAlert - Collahuasi/Data/ModeloBloque/rosmp_fc_15sep16_geom_v2.asc"
myFile = "C:/Users/Arnol/Gesecology/[Demo] GeoAlert - Collahuasi/Data/ModeloBloque/test.txt"
connStr = "PG: host='%s' port='%s' dbname='%s' user='%s' password='%s'" % ("152.231.85.227",
                                                                           "5432",
                                                                           "geoalert_template",
                                                                           "postgres",
                                                                           "Admin321")
schemName = "test"
tableName = "test"

dr.uploadMbFromFile_CMDIC(myFile, connStr, schemName, tableName, batch=0)