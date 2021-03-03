from PIL import Image
import os
#test ucitavanja/prikaza slike
#img = Image.open('0001.png')
#img.show()
#print(img.size)

#image resize test
#img = Image.open('0001.png')
#img.show()
#img1 = img.resize((1024, 1024))
#img1.show()
#img = Image.open('0089.png')
#img.show()
#width, height = img.size
#imcrop(left top right bottom)
#left = (width-1024)/2
#right = left + 1024
#top = (height - 1024)/2
#bottom = top + 1024
#img = img.crop((left, top, right, bottom))
#img.show()

for f in os.listdir('.'):
    if f.endswith('.png'):
        i = Image.open(f)
        fn, fext = os.path.splitext(f)

        width, height = i.size
        left = (width - 1024) / 2
        right = left + 1024
        top = (height - 1024) / 2
        bottom = top + 1024
        i = i.crop((left, top, right, bottom))

        i.save('1024_images/{}_1024{}'.format(fn, fext))