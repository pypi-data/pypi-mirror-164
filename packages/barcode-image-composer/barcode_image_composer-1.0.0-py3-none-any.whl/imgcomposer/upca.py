from PIL import Image
from pylibdmtx.pylibdmtx import encode, decode
import cv2
import numpy
from .codeimg import CodeImage
from barcode import UPCA
from barcode.writer import ImageWriter

class UPCACode(CodeImage):
    def __init__(self, value, scale_factor, rotation):
        super().__init__(value, scale_factor, rotation)
        
    def generate(self):
        upca_code = UPCA(self.value, writer=ImageWriter())
        upca_code.save(self.value)

        src = cv2.imread(self.value + '.png')
        src = self.rotate_image(src, self.rotation)
        src = self.resize_image(src, self.scale_factor)
        
        return self.binarize_image(src)
        