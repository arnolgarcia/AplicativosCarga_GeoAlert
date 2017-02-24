__author__ = 'Arnol'

import scripts.createLegend.ClaseLeyenda as leyend


file = "C:\Users\Arnol\GitHub\AplicativosCarga_GeoAlert\scripts\createLegend\\template_7cl_sim_pixel.sld"
mylg = leyend.Leyenda(file)

nro_cl = 7

sat = 5
size = 3
att = "velocidad_mm_hr"
unit = "mm/hr"
tit = "Velocidad promedio [%d%s]" % (sat, unit)

rlnames = leyend.formatRulenames(nro_cl, "[%s]" % unit, -sat, sat, False)
fname = "ibis_last_vel_size%dx%d_range-%d_%d_clases7.sld" % (size, size, sat, sat)

outname = "C:\Users\Arnol\GitHub\AplicativosCarga_GeoAlert\scripts\createLegend\\" + fname


mylg.create(titulo=tit, rlNames=rlnames, sat=sat, size=size, outname=outname, atributo=att)