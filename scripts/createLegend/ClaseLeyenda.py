__author__ = 'Arnol'


# -----------------------------------------------------------------------------
#     Objeto
# -----------------------------------------------------------------------------
class Leyenda(object):

    def __init__(self, tempfile):
        self.template = tempfile
        self.titulo = ""
        self.ruleNames = []
        self.saturacion = None
        self.size = None
        self.sldString = ""
        self.atributo = ""

    def create(self, titulo, rlNames, sat, size, atributo, outname):
        self.titulo = titulo
        self.ruleNames = rlNames
        self.saturacion = sat
        self.size = size
        self.atributo = atributo

        with open(self.template) as sldfile:
            self.sldString = sldfile.read()
        self.replaceTitulo()
        self.replaceSat()
        self.replaceSize()
        self.replaceAtt()
        self.replaceRulename()

        outfile = open(outname, 'w+')
        outfile.write(self.sldString)

    def replaceTitulo(self):
        new_titulo = ">%s<" % self.titulo
        self.sldString = self.sldString.replace(">titulo<", new_titulo)

    def replaceSat(self):
        new_sat = ">%d<" % self.saturacion
        self.sldString = self.sldString.replace(">saturacion<", new_sat)

    def replaceAtt(self):
        new_att = ">%s<" % self.atributo
        self.sldString = self.sldString.replace(">atributo<", new_att)

    def replaceSize(self):
        new_size = ">%d<" % self.size
        self.sldString = self.sldString.replace(">pixelsize<", new_size)

    def replaceRulename(self):
        i = 0
        for name in self.ruleNames:
            old_name = ">rulename%d<" % (i+1)
            new_name = ">%s<" % name
            self.sldString = self.sldString.replace(old_name, new_name)
            i += 1


def formatRulenames(nro_clases, unidades, min_value, max_value, interv_cerrado):
    ruleNames = []

    if interv_cerrado:
        nro_cl_inside = nro_clases
    else:
        nro_cl_inside = nro_clases - 2

    step = 1.0*(max_value - min_value) / nro_cl_inside

    if not interv_cerrado:
        str_rule = "Less than %g%s" % (min_value, unidades)
        ruleNames.append(str_rule)

    for i in range(nro_cl_inside):
        str_rule = "Between %g%s and %g%s" % (min_value + step * i, unidades,
                                              min_value + step * (i+1), unidades)
        ruleNames.append(str_rule)

    if not interv_cerrado:
        str_rule = "Greatest than %g%s" % (max_value, unidades)
        ruleNames.append(str_rule)

    return  ruleNames


