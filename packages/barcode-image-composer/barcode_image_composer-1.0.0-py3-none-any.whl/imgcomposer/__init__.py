import numpy

__version__ = '1.0.0'

class ImageManager:
        
    class Renderer:
        def __init__(self, left, top, color_picker, code_type):
            self.left = int(left)
            self.top = int(top)
            self.color_picker = color_picker
            self.code_type = code_type

    def compose(self, bg_image, renderers):
        try:
            for renderer in renderers:
                src = renderer.code_type.generate()
                src[numpy.where((src==[255,255,255]).all(axis=2))] = bg_image[renderer.color_picker[0], renderer.color_picker[1]]
                bg_image[renderer.top:renderer.top + src.shape[0], renderer.left: renderer.left + src.shape[1]] = src
            return bg_image
        except Exception as err:
            print(err)