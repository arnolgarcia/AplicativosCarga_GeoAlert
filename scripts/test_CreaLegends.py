__author__ = 'Arnol'


import scripts.createLegend.ClaseLeyenda as leyend


file = "C:\Users\Arnol\GitHub\AplicativosCarga_GeoAlert\scripts\createLegend\\template_7cl_sim_pixel.sld"


nro_cl = 7
sat_min = 0
sat_max = 1
sat = sat_max
size = 30
att = "indice_riesgo"
unit = ""
tit = "Indice de riesgo"



[rlnames, rlbreaks] = leyend.formatRulenames(nro_cl, "", sat_min, sat_max, True)


aux_temp = leyend.createTemplate('rango_cerrado', nro_cl, rlbreaks, palette = "RdYlGn_r")


fname_layer = "mlp"
fname_tipo = "clases7"  # "clases7"
fname = "%s_size%dx%d_range%d_%d_%s.sld" % (fname_layer, size, size, sat_min, sat_max, fname_tipo)

outname = "C:\Users\Arnol\GitHub\AplicativosCarga_GeoAlert\scripts\createLegend\\" + fname


mylg = leyend.Leyenda(tempfile=None, sld=aux_temp)
mylg.create(titulo=tit, rlNames=rlnames, sat=sat, size=size, outname=outname, atributo=att)