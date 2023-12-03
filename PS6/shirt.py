#Assignment: implement a program that expects exactly two command-line arguments:

    #in sys.argv[1], the name (or path) of a JPEG or PNG to read (i.e., open) as input
    #in sys.argv[2], the name (or path) of a JPEG or PNG to write (i.e., save) as output



import sys
import os
from PIL import Image, ImageOps


def main():
    img1, img2 = get_img(sys.argv)
    img_nw = update_img(img1, img2)


def get_img(arg):
    extensions = {".jpg", ".jpeg", ".png"}

    if len(arg) <= 2:
        sys.exit("Too few command-line arguments")
    elif len(arg) > 3:
        sys.exit("Too many command-line arguments")
    elif os.path.splitext(arg[1].casefold())[1] not in extensions:
         sys.exit("Invalid input")
    elif os.path.splitext(arg[2].casefold())[1] not in extensions:
        sys.exit("Invalid output")
    elif os.path.splitext(arg[1].casefold())[1] != os.path.splitext(arg[2].casefold())[1]:
        sys.exit("Input and output have different extensions")


    try:
        img = Image.open(arg[1])
    except PermissionError:
       sys.exit("Input does not exist")

    return img, arg[2]



def update_img(img, img_name):
    shirt = Image.open("shirt.png")
    size = shirt.size

    img = ImageOps.fit(img, size, method=Image.BICUBIC, bleed=0.0, centering=(0.5, 0.5))
    img.paste(shirt, shirt)

    img.save(img_name)

    return img



if __name__ == "__main__":
    main()
