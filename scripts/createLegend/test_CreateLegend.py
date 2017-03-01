# -*- coding: utf-8 -*-
#
# __author__ = 'Arnol'

import scripts.createLegend.ClaseLeyenda as leyend

"""
file = "C:\Users\Arnol\GitHub\AplicativosCarga_GeoAlert\scripts\createLegend\\template_7cl_sim_pixel.sld"
mylg = leyend.Leyenda(file)

nro_cl = 7

sat = 5
size = 3
att = "velocidad_mm_hr"
unit = "mm/hr"
tit = "Velocidad promedio [%d%s]" % (sat, unit)
"""

"""
rlnames = leyend.formatRulenames(nro_cl, "[%s]" % unit, -sat, sat, False)
fname = "ibis_last_vel_size%dx%d_range-%d_%d_clases7.sld" % (size, size, sat, sat)

outname = "C:\Users\Arnol\GitHub\AplicativosCarga_GeoAlert\scripts\createLegend\\" + fname


mylg.create(titulo=tit, rlNames=rlnames, sat=sat, size=size, outname=outname, atributo=att)
"""

tipo = "clases"
size = 25
sat = 0

"""
fname_layer = "mbloque_lito"
tit = "Litologia"
nro_rules = 5
value_rules = ["1", "2", "3", "4", "6"]
rlnames = ["Porfido Feldespatico (Diorita, Granodiorita)",
           "Porfido Riolitico",
           "Andesita",
           "Brechas",
           "Gravas"]
att = "lito"
"""


"""
fname_layer = "mbloque_mine"
tit = "Mineralizacion"
nro_rules = 7
value_rules = ["1", "4", "5", "6", "7", "8", "0"]
rlnames = ["Mixto",
           "Mixto",
           "Oxido",
           "Primario + Bornita",
           "Primario",
           "Esteril",
           "Lixiviado"]
att = "mine"
"""


"""
fname_layer = "mbloque_alte"
tit = "Alteracion"
nro_rules = 3
value_rules = ["1", "2", "3"]
rlnames = ["Cuarzo - Sericita",
           "Clorita - Sericita",
           "Biotizacion"]
att = "alte"
"""


fname_layer = "mbloque_ucs"
tit = "Indice UCS"
nro_rules = 14
value_rules = [0, 20, 30, 40, 50, 60, 70, 80, 100, 120, 140, 160, 180, 200, 230]
rlnames = ["0 - 20",
           "20 -30",
           "30 -40",
           "40 -50",
           "50 -60",
           "60 -70",
           "70 -80",
           "80 -100",
           "100 -120",
           "120 -140",
           "140 -160",
           "160 -180",
           "180 -200",
           "200 -230"]
att = "ucs"
tipo = "rango_cerrado"





aux_temp = leyend.createTemplate(tipo, nro_rules, value_rules)


fname_tipo = "class"  # "clases7"
fname = "%s_size%dx%d_range-%d_%d_%s.sld" % (fname_layer, size, size, 0, 230, fname_tipo)

outname = "C:\Users\Arnol\GitHub\AplicativosCarga_GeoAlert\scripts\createLegend\\" + fname


mylg = leyend.Leyenda(tempfile=None, sld=aux_temp)
mylg.create(titulo=tit, rlNames=rlnames, sat=sat, size=size, outname=outname, atributo=att)