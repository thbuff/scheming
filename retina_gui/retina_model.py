# This are some very general simple classes
class SimpleNeuron:
    '''
        Naive class representing a neuron.
        The type has to be a string representing its type
    '''
    def __init__(self, type):
        self.type = type


class SimpleSynapse:
    def __init__(self, type, cell_in, cell_out):
        self.type = type
        self.cell_in = cell_in
        self.cell_out = cell_out


class SimpleLayer:
    def __init__(self, cells=None, synapses=None):
        self.cells = cells

        # Here I am making sure that all the synapses of the layer only connect cells of the layer
        if synapses is not None:
            in_cells = set([synapse.cell_in for synapse in synapses])
            out_cells = set([synapse.cell_out for synapse in synapses])
            if in_cells.issubset(self.cells) and out_cells.issubset(self.cells):
                self.synapses = set(synapses)
            else:
                raise Exception('Some Synapses are connected to cells outside the layer!')


class SimpleRetina:
    def __init__(self, layers):
        self.layers = layers
