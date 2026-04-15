from PIL import Image
import random

def main():
    oldPixels, newImage, newPixels = load_image('./myImage.jpg')

    # Apply correct filter
    # Only comment in one of those at a time!
    boost_red(oldPixels, newImage, newPixels)
    # invert(oldPixels, newImage, newPixels)
    # grayscale(oldPixels, newImage, newPixels)
    # set_contrast(oldPixels, newImage, newPixels, 255)
    # grainy(oldPixels, newImage, newPixels)

    # invertSpot(oldPixels, newImage, newPixels, x1, y1, x2, y2)

    # mirrorHalf(oldPixels, newImage, newPixels)

    # combined(oldPixels, newImage, newPixels)

    # blur(oldPixels, newImage, newPixels, window)


def boost_red(oldPixels, newImage, newPixels):
    for i in range(newImage.size[0]):
        for j in range(newImage.size[1]):
            r, g, b = oldPixels[i, j]

            newPixels[i, j] = (255, g, b)

    save_image(newImage, "myImage-red.jpg")

def invert(oldPixels, newImage, newPixels):
    for i in range(newImage.size[0]):
        for j in range(newImage.size[1]):
            # TODO
            pass

    save_image(newImage, "myImage-invert.jpg")

def grayscale(oldPixels, newImage, newPixels):
    for i in range(newImage.size[0]):
        for j in range(newImage.size[1]):
            # TODO
            pass

    save_image(newImage, "myImage-grayscale.jpg")

def set_contrast(oldPixels, newImage, newPixels, C):
    for i in range(newImage.size[0]):
        for j in range(newImage.size[1]):
            # TODO
            pass

    save_image(newImage, "myImage-set-contrast.jpg")

def grainy(oldPixels, newImage, newPixels):
    for i in range(newImage.size[0]):
        for j in range(newImage.size[1]):
            # TODO
            pass
    save_image(newImage, "myImage-set-contrast.jpg")


# Helpers below, do not touch

def load_image(filename):
    oldImage = Image.open(filename).convert("RGB")
    oldPixels = oldImage.load()
    oldImage.close()

    newImage = Image.new(oldImage.mode, oldImage.size)
    newPixels = newImage.load()

    return oldPixels, newImage, newPixels

def save_image(image, name):
    image.show()
    image.save(name)
    image.close()

main()
