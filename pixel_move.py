def pixel_move(x, y, width):
    x = x + 16
    if x + 2 > width:
        x = x + 2 - width
        y = y + 16

    return x,y