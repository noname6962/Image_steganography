'''chooses rgb channel for coding/decoding based on color of surrounding pixels
based on mean rgb value of pixels surrounding coding pixel returns in which channel to code next letter'''
def color_check(img_alfa, x_alfa, y_alfa):
    total_red, total_green, total_blue = 0, 0, 0
    for x in range(x_alfa - 1, x_alfa + 1):
        for y in range(y_alfa - 1, y_alfa + 1):
            if x != x_alfa and y != y_alfa:
                red, green, blue = img_alfa.getpixel((x, y))
                total_red += red
                total_green += green
                total_blue += blue

    red = abs(total_red/8 - 98)
    green = abs(total_green/8 - 98)
    blue = abs(total_blue/8 - 98)
    values = {"red": red, "green": green, "blue": blue}

    return min(values, key=values.get)
