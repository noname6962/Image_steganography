from PIL import Image
import random


#funckaj sprawdzajaca ktory kolor na obszarze 4x4 jest najbardziej bliski wartosci 100 poza pixelem "alfa
def kolor_check(img, x_alfa, y_alfa):
    total_red, total_green, total_blue = 0, 0, 0
    for x in range(0, 4):
        for y in range(0, 4):
            if not (x_alfa == x and y_alfa == y):
                pixel_value = img.getpixel((x, y))
                red, green, blue = pixel_value
                total_red += red
                total_green += green
                total_blue += blue

    #sprawdzenie ktory kanal jest najblizej 100
    if abs((total_red/15)-100) < abs((total_green/15)-100) and abs((total_red/15)-100) < abs((total_blue/15)-100):
        return "red"
    elif abs((total_green/15)-100) < abs((total_red/15)-100) and abs((total_green/15)-100) < abs((total_blue/15)-100):
        return "green"
    elif abs((total_blue/15)-100) < abs((total_red/15)-100) and abs((total_blue/15)-100) < abs((total_green/15)-100):
        return "blue"
    else:
        return 0


def kodowanie(tekst, img):
    #wyslosowanie polozenia
    x = random.randint(0, 3)
    y = random.randint(0, 3)

    #zakodowanie polozenia i dlugosci do skrajnego bitu
    pixel_value = img.getpixel((0, 0))
    red, green, blue = pixel_value
    red = x
    green = y
    blue = len(tekst)
    img.putpixel((0, 0), (red, green, blue))

    i = 0
    while len(tekst):
        x = x + 4
        if x > img.width:
            x = x - img.width
            y = y + 4

        #sprawdzenie ktory kanal koduje
        kanal = kolor_check(img, x, y)

        pixel_value = img.getpixel((x, y))
        red, green, blue = pixel_value
        if kanal == "red":
            red = ord(tekst[i])
        elif kanal == "green":
            green = ord(tekst[i])
        else:
            blue = ord(tekst[i])
        img.putpixel((x, y), (red, green, blue))

        i = i + 1

#funkcja dekodowania

def dekodowanie(img):
    #string na ktorym bedziemy zapisywac tekst
    decoded_tekst = ""

    #pobieranie polozenia i dlugosci
    pixel_value = img.getpixel((0, 0))
    x, y, dlugosc = pixel_value

    #dekodowanie tekstu
    for i in range(0, dlugosc):
        x = x + 4
        if x > img.width:
            x = x - img.width
            y = y + 4

        #sprawdzenie ktory kanal koduje
        kanal = kolor_check(img, x, y)

        pixel_value = img.getpixel((x, y))
        red, green, blue = pixel_value
        if kanal == "red":
            decoded_tekst = decoded_tekst + chr(red)
        elif kanal == "green":
            decoded_tekst = decoded_tekst + chr(green)
        else:
            decoded_tekst = decoded_tekst + chr(blue)

    return decoded_tekst


def main():
    wybor = 0
    while wybor != 3:
        print("1. Zakoduj tekst")
        print("2. Dekoduj tekst")
        print("3. Wyjscie")

        #pobranie wyboru
        try:
            wybor = int(input("Wybierz opcje: "))
        except ValueError:
            print("Podaj liczbe")
            wybor = 0

        #Open an image
        name = input("Podaj nazwe zdjecia: ")
        img = Image.open(f"{name}.jpg")
        with Image.open("hopper.jpg") as img:
            #kodowanie
            if wybor == 1:
                #pobieranie tekstu
                tekst = input("Podaj tekst do zakodowania: ")

                #kodowanie
                kodowanie(tekst, img)

                #zapis zdjecia
                img.save("image_mod.jpg")
            #dekodowanie
            elif wybor == 2:
                #dekodowanie
                print('tekst zakodowany w zdjeciu to:')
                print(f'{dekodowanie(img)}')


