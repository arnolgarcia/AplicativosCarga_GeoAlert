__author__ = 'Arnol'


import seaborn as sns


# -----------------------------------------------------------------------------
#     Objeto
# -----------------------------------------------------------------------------
class Leyenda(object):

    def __init__(self, tempfile, sld):
        self.template = tempfile
        self.titulo = ""
        self.ruleNames = []
        self.saturacion = None
        self.size = None
        self.atributo = ""
        # Guardar el sld en un string
        if sld is None:
            with open(self.template) as sldfile:
                self.sldString = sldfile.read()
        else:
            self.sldString = sld

    def create(self, titulo, rlNames, sat, size, atributo, outname):
        self.titulo = titulo
        self.ruleNames = rlNames
        self.saturacion = sat
        self.size = size
        self.atributo = atributo

        self.replaceTitulo()
        self.replaceSat()
        self.replaceSize()
        self.replaceAtt()
        self.replaceRulename()

        outfile = open(outname, 'w+')
        #outfile.write(self.sldString.encode('utf-8'))  # TODO: ver en el geoserver porque se cae con utf-8
        outfile.write(self.sldString)

    def replaceTitulo(self):
        new_titulo = ">%s<" % self.titulo
        self.sldString = self.sldString.replace(">titulo<", new_titulo)

    def replaceSat(self):
        new_sat = ">%d<" % self.saturacion
        self.sldString = self.sldString.replace(">saturacion<", new_sat)

    def replaceAtt(self):
        new_att = ">%s<" % self.atributo
        self.sldString = self.sldString.replace(">param_atributo<", new_att)

    def replaceSize(self):
        new_size = ">%d<" % self.size
        self.sldString = self.sldString.replace(">param_pixelsize<", new_size)

    def replaceRulename(self):
        i = 0
        for name in self.ruleNames:
            old_name = ">rulename%d<" % (i+1)
            new_name = ">%s<" % name
            self.sldString = self.sldString.replace(old_name.decode('utf-8'), new_name.decode('utf-8'))
            i += 1


# -----------------------------------------------------------------------------
#     Funciones extras
# -----------------------------------------------------------------------------
def formatRulenames(nro_clases, unidades, min_value, max_value, interv_cerrado):
    ruleNames = []
    ruleBreaks = []

    if interv_cerrado:
        nro_cl_inside = nro_clases
    else:
        nro_cl_inside = nro_clases - 2

    step = 1.0*(max_value - min_value) / nro_cl_inside

    if not interv_cerrado:
        str_rule = "Less than %g%s" % (min_value, unidades)
        ruleNames.append(str_rule)
        ruleBreaks.append(min_value)

    for i in range(nro_cl_inside):
        str_rule = "Between %g%s and %g%s" % (min_value + step * i, unidades,
                                              min_value + step * (i+1), unidades)
        ruleNames.append(str_rule)
        ruleBreaks.append(min_value + step * i)

    ruleBreaks.append(max_value)

    if not interv_cerrado:
        str_rule = "Greatest than %g%s" % (max_value, unidades)
        ruleNames.append(str_rule)

    return [ruleNames, ruleBreaks]


def createTemplate(tipo, nro_rules, value_filter, palette):
    # Definir templates
    txt_head = "C:\Users\Arnol\GitHub\AplicativosCarga_GeoAlert\scripts\createLegend\\template_head.sld"
    txt_tail = "C:\Users\Arnol\GitHub\AplicativosCarga_GeoAlert\scripts\createLegend\\template_tail.sld"
    txt_rule_IsEqualTo = "C:\Users\Arnol\GitHub\AplicativosCarga_GeoAlert\scripts\createLegend\\template_rule_IsEqualTo.sld"
    txt_rule_Between_closedLR = "C:\Users\Arnol\GitHub\AplicativosCarga_GeoAlert\scripts\createLegend\\template_rule_Between_RcLc.sld"
    txt_rule_Between_closedR = "C:\Users\Arnol\GitHub\AplicativosCarga_GeoAlert\scripts\createLegend\\template_rule_Between_RoLc.sld"

    # Inicializar slds
    with open(txt_head) as sldfile:
            sld_head = sldfile.read()
    with open(txt_tail) as sldfile:
            sld_tail = sldfile.read()
    sld_rule = ""

    # Definir colores
    if palette is None:
        if tipo == 'clases' and nro_rules <= 10:
            palette = "Set2"
        elif tipo == 'clases' and nro_rules > 10:
            palette = "cubehelix"
        elif tipo == 'rango_cerrado':
            palette = "Blues"
    colores = sns.color_palette(palette, nro_rules).as_hex()

    # definir regla en caso de clases
    if tipo == 'clases':
        with open(txt_rule_IsEqualTo) as sldfile:
                sld_rule = sldfile.read()

    sld_Total = sld_head + "\n"
    for i in range(nro_rules):
        if tipo == 'rango_cerrado' and i == 0:
            with open(txt_rule_Between_closedLR) as sldfile:
                    sld_rule = sldfile.read()

        sld_rule_aux = sld_rule
        sld_rule_aux = sld_rule_aux.replace("param_rulename", "rulename%d" % (i+1))
        sld_rule_aux = sld_rule_aux.replace('param_valorclase', "%s" % value_filter[i])
        sld_rule_aux = sld_rule_aux.replace('param_colorhex', "%s" % colores[i])

        if tipo == 'rango_cerrado':
            sld_rule_aux = sld_rule_aux.replace('param_rangomin', "%s" % value_filter[i])
            sld_rule_aux = sld_rule_aux.replace('param_rangomax', "%s" % value_filter[i+1])

        sld_Total += sld_rule_aux + "\n"

        if tipo == 'rango_cerrado' and i == 0:
            with open(txt_rule_Between_closedR) as sldfile:
                    sld_rule = sldfile.read()

    sld_Total += sld_tail

    return sld_Total



