import qrcode
from .codeimg import CodeImage
import numpy
import cv2

class Qrcode(CodeImage):
    def __init__(self, value, scale_factor, rotation):
        super().__init__(value, scale_factor, rotation)
        
    def generate(self):
        img = qrcode.make(self.value)
        img.save(self.value + '.png')
        
        src = cv2.imread(self.value + '.png')
        src = self.rotate_image(src, self.rotation)
        src = self.resize_image(src, self.scale_factor)
        
        return self.binarize_image(src)