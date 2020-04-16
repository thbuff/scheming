from PIL import Image


# This class takes a graphic set, a retina model, and generates a big image representing the retina
class RetinaViewer:

    def __init__(self, graphic_set):
        self.graphic_set = graphic_set
        self.width_spacing = 0  # Pixels
        self.height_spacing = 0  # Pixels
        self.width_size = 1000 # Pixels
        self.height_size = 500 # Pixels
        self.background_color = (200, 255, 255)

    # Here you have some methods to change the settings of the viewer
    def change_graphic_set(self, graphic_set):
        self.graphic_set = graphic_set

    def change_spacing(self, width_spacing, height_spacing):
        self.width_spacing = width_spacing
        self.height_spacing = height_spacing

    def change_background(self, background_color):
        self.background_color = background_color

    def change_image_size(self, width_size, height_size):
        self.width_size = width_size
        self.height_size = height_size

    # This is the main function that plots the retina
    def plot_retina(self, retina):
        retina_image = self._compose_retina_img(retina)
        retina_image = retina_image.resize((self.width_size, self.height_size))
        retina_image.show()


    # This are some private functions that compose the big retina image from the graphic blocks
    def _compose_layer_img(self, layer):

        # Here I calculate how big the layer image has to be
        cell_images = [self.graphic_set.get_cell_img(cell.type) for cell in layer.cells]
        layer_height = max([img.height for img in cell_images])
        layer_width = sum([img.width + self.width_spacing for img in cell_images])
        layer_image = Image.new('RGB', (layer_width, layer_height), color=self.background_color)

        # Here copy paste all the neuron images in a line, to form my layer image
        current_width = int(self.width_spacing / 2)
        for cell_image in cell_images:
            height = int(layer_height/2 - cell_image.height/2)
            layer_image.paste(cell_image, (current_width, height), cell_image.convert('RGBA'))
            current_width += cell_image.width + self.width_spacing

        return layer_image

    def _compose_retina_img(self, retina):
        layer_images = [self._compose_layer_img(layer) for layer in retina.layers]

        # Same here, first  I calculate how big the retina image has to be
        retina_height = sum([img.height + self.height_spacing for img in layer_images])
        retina_width = max([img.width for img in layer_images])
        retina_image = Image.new('RGB', (retina_width, retina_height), color=self.background_color)

        # And then I copy paste all the layers one below the other
        current_height = int(self.height_spacing / 2)
        for layer_image in layer_images:
            width = int(retina_width/2 - layer_image.width/2)
            retina_image.paste(layer_image, (width, current_height), layer_image.convert('RGBA'))
            current_height += layer_image.height + self.height_spacing
        return retina_image


