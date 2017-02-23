__author__ = 'Arnol'


import logging


# -----------------------------------------------------------------------------
#     Objeto RegistroMB_CMDIC
# -----------------------------------------------------------------------------
class Leyenda(object):

    def __init__(self):
        # TODO: comprobar que nombres sean los originales y en el orden correcto
        self.fields = ['xcentre', 'ycentre', 'zcentre',
                       'xlength', 'ylength', 'zlength',
                       'alter_det', 'alter_mp',
                       'banco',
                       'bsu', 'bsu_rat', 'densidad_mp',
                       'ff', 'ff_lp', 'ff_rat',
                       'gsi_rat',
                       'hsag', 'hsaga',
                       'int_alt', 'jc', 'jc_rat',
                       'lito_det', 'lito_mp',
                       'mi', 'mnzn_det', 'mnzn_mp',
                       'modelo',
                       'mot', 'mot_mp', 'ppv_crit', 'rfc_op',
                       'rmom', 'rmu_rat',
                       'rqd', 'rqd_porc', 'rqd_rat',
                       'rst_op', 'rsu_rat',
                       'st_com',
                       'topo', 'topo_mp',
                       'ucs', 'ugcut', 'ugg', 'ugg_rat',
                       'ugm', 'ugm_mp', 'ugt']
        self.data = []
        self.nrofields = len(self.fields)  # 49 campos
        self.llave = "(xcentre, ycentre, zcentre)"
        for i in range(self.nrofields):
            setattr(self, self.fields[i], None)

    def registro(self, data):
        self.data = []
        for i in range(self.nrofields):
            setattr(self, self.fields[i], float(data[i]))
            self.data.append(float(data[i]))

    def getData(self):
        return self.data

    def registroToDB(self):
        aux = []
        for i in range(3, self.nrofields):
            aux.append(getattr(self, self.fields[i]))
        aux = str(aux).replace("[", "{").replace("]", "}")
        datos = [self.xcentre, self.ycentre, self.zcentre, aux]
        # Retornar salida
        newReg = RegistroMB_DB()
        newReg.registro(datos)
        return newReg

    def registroToMel(self):
        # TODO: confirmar las variables lito, alter, mnzn y rmr o ver que se puede poner en su lugar
        datos = [self.xcentre, self.ycentre, self.zcentre,
                 self.xlength, self.ylength, self.zlength,
                 self.lito_det, self.alter_det, self.mnzn_det,
                 self.ucs, self.rmu_rat]
        # Retornar salida
        newReg = RegistroMB_MEL()
        newReg.registro(datos)
        return newReg

