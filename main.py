from PIL import Image
from PIL import ImageOps
from PIL import ImageFilter
import argparse


def get_bw(image):
    image = image.convert("L")
    image.save("result/bw_image.jpg")

def get_contarst(image):
    image = ImageOps.autocontrast(image, cutoff=5)
    image.save("result/contast_image.jpg")

def get_blur(image):
    image = image.filter(ImageFilter.GaussianBlur(radius=3))
    image.save("result/blur.jpg")

def get_median(image):
    image = image.filter(ImageFilter.MedianFilter(size=9))
    image.save("result/image_median.jpg")

def get_frame(image):
    width, height = image.size
    image = image.transform((width + 100, height + 100), Image.EXTENT, (-10, -10, width + 10, height + 10), Image.BILINEAR)
    image.save("result/image_frame.jpg")

def get_sepia(image):
    sepia_r = 112
    sepia_g = 66
    sepia_b = 20
    image_sepia = Image.new("RGB", image.size)
    for pixel_in_x in range (image.width):
        for pixel_in_y in range (image.height):
            r, g, b = image.getpixel((pixel_in_x, pixel_in_y))
            new_r = int(r * 0.393 + g * 0.769 + b * 0.189)
            new_g = int(r * 0.349 + g * 0.686 + b * 0.168)
            new_b = int(r * 0.272 + g * 0.534 + b+ 0.131)
            sepia_r = min(new_r, 255)
            sepia_g = min(new_g, 255)
            sepia_b = min(new_b, 255)
            image_sepia.putpixel((pixel_in_x, pixel_in_y), (sepia_r, sepia_g, sepia_b))
    image_sepia.save("result/image_sepia.jpg")

def main():
    parser = argparse.ArgumentParser()
    


    parser.add_argument('--input', help='Имя начального файла', default='image.jpg')
    parser.add_argument('--bw', action="store_true", help='черно белый фильтр')
    parser.add_argument('--contarst', action="store_true", help='контрастный фильтр')
    parser.add_argument('--blur', action="store_true", help='блюр')
    parser.add_argument('--median', action="store_true", help='медиан')
    parser.add_argument('--frame', action="store_true", help='рамка')
    parser.add_argument('--sepia', action="store_true", help='сепия')

    args = parser.parse_args()

    print(f"""
название файла: {args.input}
черно белый филтр: {args.bw}
контрастный фильтр: {args.contarst}
блюр: {args.blur}
медиана: {args.median}
рамка: {args.frame}
сепия: {args.sepia}""")
    input_file = args.input
    image = Image.open(f"image/{input_file}")

    
    if args.bw:
        get_bw(image)
    if args.contarst:
        get_contarst(image)
    if args.blur:
        get_blur(image)
    if args.median:
        get_median(image)
    if args.frame:
        get_frame(image)
    if args.sepia:
        get_sepia(image)


if __name__ == "__main__":
    main()