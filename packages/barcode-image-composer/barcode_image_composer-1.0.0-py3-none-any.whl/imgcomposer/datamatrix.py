from PIL import Image
from pylibdmtx.pylibdmtx import encode
import numpy
from .codeimg import CodeImage

class DataMatrixCode(CodeImage):
    def __init__(self, value, scale_factor, rotation):
        super().__init__(value, scale_factor, rotation)
        
    def generate(self):
        encoded = encode(self.value.encode('utf8'))
        img = Image.frombytes('RGB', (encoded.width, encoded.height), encoded.pixels)
        src = numpy.array(img)
        src = self.rotate_image(src, self.rotation)
        src = self.resize_image(src, self.scale_factor)
        
        return self.binarize_image(src)
        