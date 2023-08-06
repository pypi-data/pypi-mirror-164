import cv2

class CodeImage:
    def __init__(self, value='1', scale_factor=1, rotation=0):
        self.value = value
        self.scale_factor = scale_factor
        self.rotation = rotation
        
    def rotate_image(self, src, rotation):
        # (h, w) = src.shape[:2]
        # center = (w / 2, h / 2)
        # M = cv2.getRotationMatrix2D(center, angle, 1.0)
        # rotated = cv2.warpAffine(src, M, (w, h))
        # return rotated
        if rotation == cv2.ROTATE_180 or rotation == cv2.ROTATE_90_COUNTERCLOCKWISE or rotation == cv2.ROTATE_90_CLOCKWISE:
            return cv2.rotate(src, rotation)
        else:
            return src
    
    def resize_image(self, src, scale_factor):
        if self.scale_factor == 1:
            return src
        
        width = int(src.shape[1] * scale_factor)
        height = int(src.shape[0] * scale_factor)
        dim = (width, height)
        return cv2.resize(src, dim)
    
    def binarize_image(self, src):
        gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
        bw = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        return cv2.cvtColor(bw, cv2.COLOR_GRAY2BGR)
    
    def generate(self):
        pass