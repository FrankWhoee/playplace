from PIL import Image

im = Image.open("rotated/target.png")

numImages = 24

for i in range(1,numImages):
    rotated = im.rotate(i * int(360/numImages), resample=Image.BICUBIC)
    rotated.save("rotated/rotate{}.png".format(i))
    
