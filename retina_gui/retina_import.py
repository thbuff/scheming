import csv
from retina_model import SimpleRetina, SimpleLayer, SimpleNeuron


# This is a function to import retina structures from a .csv file
def import_retina_csv(csv_file):
    layers = []

    # First I open the file with my csv reader
    with open(csv_file, newline='') as csvfile:
        r = csv.reader(csvfile, delimiter=',', quotechar='|')

        # Each row represents a layer..
        for row in r:

            # And each column is a neuron
            layer = SimpleLayer([SimpleNeuron(neuron_type) for neuron_type in row])
            layers.append(layer)

    return SimpleRetina(layers)

