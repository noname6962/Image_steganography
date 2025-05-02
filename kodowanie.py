import color_check
import random


def kodowanie(tekst, img):
    x = random.randint(0, 4)
    y = random.randint(2, 4)
    red, green, blue = img.getpixel((0, 0))
    img.putpixel((0, 0), (x, y, blue))

    for i in range(len(tekst)):
        x = x + 16
        if x + 2 > img.width:
            x = x + 2 - img.width
            y = y + 16
        kanal = color_check.color_check(img, x, y)
        red, green, blue = img.getpixel((x, y))
        if kanal == "red":
            red = ord(tekst[i])
        elif kanal == "green":
            green = ord(tekst[i])
        else:
            blue = ord(tekst[i])
        img.putpixel((x, y), (red, green, blue))

    x = x + 16
    if x + 2 > img.width:
        x = x + 2 - img.width
        y = y + 16
    img.putpixel((x, y), (0, 0, 0))
    return img
