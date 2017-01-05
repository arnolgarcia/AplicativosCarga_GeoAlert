__author__ = 'Arnol'

file = 'C:\Users\Arnol\Dropbox\Proyecto_FruitClassification\data test\cifar-100\cifar-10-batches-py\data_batch_1'


def unpickle(file):
    import cPickle
    fo = open(file, 'rb')
    dict = cPickle.load(fo)
    fo.close()
    return dict

test = unpickle(file)

print 'test'