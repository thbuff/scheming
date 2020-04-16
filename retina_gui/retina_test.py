from retina_import import import_retina_csv
from retina_rendering import GraphicSet
from retina_viewer import RetinaViewer

# Import my retina from file
retina = import_retina_csv("data/retina_simple.csv")

# Load 2 different rendering sets
graphics_blocks = GraphicSet("graphics/blocks")
graphics_cartoon = GraphicSet("graphics/cartoon")

# Instantiate the viewer
viewer = RetinaViewer(graphics_cartoon)

# Visualize the retina
viewer.plot_retina(retina)

# Change some settings...
viewer.change_spacing(200, 200)
viewer.change_background((255, 200, 200))
viewer.change_image_size(500, 300)
viewer.change_graphic_set(graphics_blocks)

#  ...and visualize again!
viewer.plot_retina(retina)

# You can plug my retina_viewer object inside your interactive gui,
# so you can generate dinamically new images with a few buttons :)
# I did not work on the synapses yet but we can do that!
