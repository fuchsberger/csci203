from PIL import Image
import random

def main():
    oldPixels, newImage, newPixels = load_image('./myImage.jpg')

    # Apply correct filter
    # Only comment in one of those at a time!
    # boost_red(oldPixels, newImage, newPixels)
    # invert(oldPixels, newImage, newPixels)
    # grayscale(oldPixels, newImage, newPixels)
    # set_contrast(oldPixels, newImage, newPixels, 255)
    grainy(oldPixels, newImage, newPixels)

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
            r, g, b = oldPixels[i, j]

            newPixels[i, j] = (255 - r, 255 - g, 255 - b)

    save_image(newImage, "myImage-invert.jpg")

def grayscale(oldPixels, newImage, newPixels):
    for i in range(newImage.size[0]):
        for j in range(newImage.size[1]):
            r, g, b = oldPixels[i, j]

            avg = round((r + g + b) / 3)

            newPixels[i, j] = (avg, avg, avg)

    save_image(newImage, "myImage-grayscale.jpg")

def set_contrast(oldPixels, newImage, newPixels, C):
    for i in range(newImage.size[0]):
        for j in range(newImage.size[1]):
            r, g, b = oldPixels[i, j]

            F = (259 * (C + 255)) / (255 * (259 - C))

            r = round(F * (r - 128) + 128)
            g = round(F * (g - 128) + 128)
            b = round(F * (b - 128) + 128)

            newPixels[i, j] = (r, g, b)

    save_image(newImage, "myImage-set-contrast.jpg")

def grainy(oldPixels, newImage, newPixels):
    for i in range(newImage.size[0]):
        for j in range(newImage.size[1]):

            choice = random.randint(1, 3)
            r, g, b = oldPixels[i, j]

            if choice == 1:
                newPixels[i, j] = (255, g, b)
            elif choice == 2:
                newPixels[i, j] = (r, 255, b)
            else:
                newPixels[i, j] = (r, g, 255)

    save_image(newImage, "myImage-set-contrast.jpg")

def invertSpot(oldPixels, newImage, newPixels, x1, y1, x2, y2):
    for i in range(newImage.size[0]):
        for j in range(newImage.size[1]):
            if x1 <= j <= x2 and y1 <= i <= y2:
                r, g, b = oldPixels[i, j]
                newPixels[i, j] = (255-r, 255-g, 255-b)
            else:
                r, g, b = oldPixels[i, j]
                newPixels[i, j] = (r, g, b)
    save_image(newImage, "myImage-invert-spot.jpg")

def blur(oldPixels, newImage, newPixels, window):
    for i in range(newImage.size[0]-window):
        for j in range(newImage.size[1]):

                sum_r = 0
                sum_b = 0
                sum_g = 0

                for k in range(i, i + window):
                    r, g, b = oldPixels[k,j]
                    sum_r += r
                    sum_g += g
                    sum_b += b


                newPixels[i, j] = (round(sum_r/window), round(sum_g/window), round(sum_b/window))

    save_image(newImage, "myImage-invert-spot.jpg")


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
