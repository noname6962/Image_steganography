import color_check


#decodes string from photo
def dekodowanie(img):
    decoded_tekst = ""
    x, y, blue = img.getpixel((0, 0))

    #adjust coding pixel postion
    while True:
        x = x + 16
        if x + 2 > img.width:
            x = x + 2 - img.width
            y = y + 16

        kanal = color_check.color_check(img, x, y)
        red, green, blue = img.getpixel((x, y))

        #rgb=0,0,0 is break point pixel
        if red == 0 and green == 0 and blue == 0:
            break
        if kanal == "red":
            decoded_tekst += chr(red)
        elif kanal == "green":
            decoded_tekst += chr(green)
        else:
            decoded_tekst += chr(blue)

    return decoded_tekst
