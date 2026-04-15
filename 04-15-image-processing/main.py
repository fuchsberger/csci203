from PIL import Image
im = Image.open('./myImage.jpg').convert("RGB")
pixelMap = im.load()

img = Image.new( im.mode, im.size)
pixelsNew = img.load()
for i in range(img.size[0]):
    for j in range(img.size[1]):
        r, g, b = pixelMap[i, j]

        pixelsNew[i,j] = (255, g, b)


im.close()
img.show()
img.save("myImage-red.jpg")
img.close()
