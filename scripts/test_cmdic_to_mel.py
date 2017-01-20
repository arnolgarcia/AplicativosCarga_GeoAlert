__author__ = 'Arnol'


import logging
logging.basicConfig(format='%(levelname)s-%(asctime)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.DEBUG)

import modelobloque.ClaseModeloBloque as mb



inp_File = "C:/Users/Arnol/Gesecology/[Demo] GeoAlert - Collahuasi/Data/ModeloBloque/rosmp_fc_15sep16_geom_v2.asc"
inp_File = "C:/Users/Arnol/Gesecology/[Demo] GeoAlert - Collahuasi/Data/ModeloBloque/test.txt"
out_File = "C:/Users/Arnol/Gesecology/[Demo] GeoAlert - Collahuasi/Data/ModeloBloque/mb_cmdic_to_mel_test.txt"

print_batch = 3
with open(inp_File) as infile:
    infile.seek(0)  # Saltarse la primera linea con la cabecera

    # Crear objeto MB
    mybloque = mb.ModeloBloque(name='test_mb_cmdic_to_mel',
                               fecha='2017-01-19',
                               xlength=10, ylength=10, zlength=15,
                               toFile=True, tempfile=out_File,
                               mybatch=print_batch)
    # Crear objeto RegistroMB_CMDIC
    myregCMDIC = mb.RegistroMB_CMDIC()

    lineasprocesadas = 0
    for line in infile:
        Line = line.split(",")  # El separador en los archivos de CMDIC
        if Line[0].lower() != "xcentre":
            data = [float(k) for k in Line]
            myregCMDIC.registro(data)
            myregMEL = myregCMDIC.registroToMel()
            mybloque.registro(myregMEL.getData())
            lineasprocesadas += 1
    mybloque.closeRegistros()


logging.info("terminado")
