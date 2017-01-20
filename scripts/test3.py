__author__ = 'Arnol'


import scripts.modelobloque.ClaseModeloBloque as mb

import logging
logging.basicConfig(format='%(levelname)s-%(asctime)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.DEBUG)


aux = mb.ModeloBloque("test", '2017-01-01', 10, 10, 15)
print aux.puntos

#aux.setFile("C:/Users/Arnol/Gesecology/[Demo] GeoAlert - Collahuasi/Data/ModeloBloque/mb_cmdic_to_mel.txt", sep=",", hasheader=False)
aux.setFile("C:/Users/Arnol/Gesecology/[Demo] GeoAlert - Collahuasi/Data/ModeloBloque/rosmp_fc_15sep16_geom_v2.asc",
            sep=",", hasheader=True)

print aux.puntos

print aux.getRegistro(6572664)

# [30858.57796564, 83260.42083992, 4832.5, 10.0, 10.0, 15.0, -99.0, -99.0, -99.0, -99.0]