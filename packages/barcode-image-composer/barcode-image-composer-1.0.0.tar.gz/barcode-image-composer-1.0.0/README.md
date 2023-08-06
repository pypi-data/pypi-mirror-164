# Barcode Image Composer
The project is used to generate an image set with barcode, QR code and DataMatrix.

![barcode image composer](https://camo.githubusercontent.com/ec18f510ebc070d04389c92bf0d64e5f60e5c2a414260d971f2987c63d2e6184/68747470733a2f2f7777772e64796e616d736f66742e636f6d2f636f6465706f6f6c2f2f696d672f323032322f30382f626172636f64652d696d6167652d636f6d706f7365722e706e67)

## Install Dependencies
```bash 
pip install python-barcode pylibdmtx opencv-python pillow
```

## Supported Barcode Types
- UPCA
- QR Code
- DataMatrix

## Command-line Usage
```bash 
$ imgcompose [-t TIMES] [-o OUTPUT] image-source
```

## Sample Code

```python
import argparse
from imgcomposer import ImageManager
from imgcomposer.upca import UPCACode
from imgcomposer.qrcode import Qrcode
from imgcomposer.datamatrix import DataMatrixCode
import sys
import numpy as np
import os
import cv2

def process_file(imageManager, base, index, input, output):
    bg_image = cv2.imread(input)
    (height, width) = bg_image.shape[:2]
    wRatio = width / 1039; hRatio = height / 591
    upca_renderer = imageManager.Renderer(wRatio * 10, hRatio * 140, (10, 10), UPCACode(base, 0.5, cv2.ROTATE_90_CLOCKWISE))
    dm_renderer = imageManager.Renderer(wRatio * 920, hRatio * 40, (10, 10), DataMatrixCode(str(index), 1.5, -1))
    qr_renderer = imageManager.Renderer(wRatio * 20, hRatio * 390, (10, 10), Qrcode('www.dynamsoft.com', 0.4, -1))
    renderers = [upca_renderer, dm_renderer, qr_renderer]
    composed_image = imageManager.compose(bg_image, renderers)
    # cv2.imshow('composed_image', composed_image)
    outfile = '{0}x{1}_{2}.png'.format(bg_image.shape[1], bg_image.shape[0], index)
    cv2.imwrite(os.path.join(output, outfile), bg_image)
    
parser = argparse.ArgumentParser(description='Compose images with barcode, QR code, and DataMatrix code.')
parser.add_argument('source', help='An image file or a folder containing image files')
parser.add_argument('-t', '--times', default=1, type=int, help='Specify the number of times to compose the image')
parser.add_argument('-o', '--output', default='', type=str, help='Image output folder')
args = parser.parse_args()
# print(args)
try:
    input = args.source
    output = args.output
    times = args.times
    
    if not os.path.exists(input):
        print('Source not found')
        exit(-1)
    
    if output == '':
        output = os.getcwd()
    else:
        if not os.path.exists(output):
            os.mkdir(output)
        
    imageManager = ImageManager()
    base = '10000000000'
    index = 0
    for i in range(times):
        if os.path.isfile(input):
            print('Processing ' + input)
            process_file(imageManager, base, index, input, output)
            base = str(int(base) + 1)
            index += 1
        else:
            filelist = os.listdir(input)
            for file in filelist:
                print('Processing ' + file)
                process_file(imageManager, base, index, os.path.join(input, file), output)
                base = str(int(base) + 1)
                index += 1
            
    # cv2.waitKey(0)
except Exception as err:
    print(err)
    sys.exit(1)
```

## How to Build the Package
- Source distribution:
    
    ```bash
    python setup.py sdist
    ```

- Wheel:
    
    ```bash
    pip wheel . --verbose
    # Or
    python setup.py bdist_wheel
    ```


