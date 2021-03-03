from PIL import Image
import os
import numpy as np

from imagedegrade import np as degrade

#degrade test:
#img = Image.open('0010_1024.png')
#img.show()

#img = np.asarray(img)

    #jpeg sum
#img = degrade.jpeg(img, jpeg_quality = 7, subsampling = '4:4:4')
    #dodaj blur:
#img = degrade.blur(img, blur_sigma=2.7)
    #dodaj sum:
#img = degrade.noise(img, noise_sigma=7)
    #zasoli i zabiberi njam
#img = degrade.saltpepper(img, 0.01, intensity_range = (0, 255))

#img = Image.fromarray(img.astype(np.uint8))
#img.show()

for f in os.listdir('.'):
    if f.endswith('.png'):
        i = Image.open(f)
        fn, fext = os.path.splitext(f)

        i = np.asarray(i)
        i = degrade.jpeg(i, jpeg_quality = 11, subsampling = '4:4:4')
        i = degrade.blur(i, blur_sigma=2.5)
        i = degrade.noise(i, noise_sigma=0.1)
        i = degrade.saltpepper(i, 0.005, intensity_range = (0, 255))
        i = Image.fromarray(i.astype(np.uint8))

        i.save('degraded_images/{}_degraded{}'.format(fn, fext))