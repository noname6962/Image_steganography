import color_check
import pixel_move
import random


#codes given string into the photo
def kodowanie(tekst, img):
    x = random.randint(0, 4)
    y = random.randint(2, 4)
    red, green, blue = img.getpixel((0, 0))
    img.putpixel((0, 0), (x, y, blue))

    #adjust coding pixel position
    for i in range(len(tekst)):
        x,y = pixel_move.pixel_move(x, y, img.width)
        kanal = color_check.color_check(img, x, y)
        red, green, blue = img.getpixel((x, y))

        if kanal == "red":
            red = ord(tekst[i])
        elif kanal == "green":
            green = ord(tekst[i])
        else:
            blue = ord(tekst[i])

        img.putpixel((x, y), (red, green, blue))

    #break point pixel
    x,y = pixel_move.pixel_move(x, y, img.width)
    img.putpixel((x, y), (0, 0, 0))

    return img
