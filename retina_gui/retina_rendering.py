from PIL import Image
import os


# This is a class that handles the graphic sets
class GraphicSet:
    def __init__(self, path):

        # When the object is created, all its images are stored in memory
        self.graphic_collection = {}
        for r, d, f in os.walk(path):
            for file in f:
                if '.png' in file:
                    os.path.splitext(file)

                    # I use the filename to identify the cell type shown in the image
                    cell_type = os.path.splitext(file)[0]
                    image_path = os.path.join(r, file)

                    # I store these images ordered by the type they represent
                    image =  Image.open(image_path)
                    self.graphic_collection[cell_type] = image

    def get_cell_img(self, cell_type):
        return self.graphic_collection[cell_type]
