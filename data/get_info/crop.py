# Based on 1920x1080 resolution
# Will support multi-resolution later

from PIL import Image, ImageDraw

# For check the image areas 
def draw_(image_src, wRatio, hRatio):
    origin = Image.open(image_src)
    width, height = origin.size

    # Difference between drawn and cropped images may occur because of the use of int()
    w_line = [w for w in range(0, width, int(width/wRatio))]
    h_line = [h for h in range(0, height, int(height/hRatio))]

    draw = ImageDraw.Draw(origin)
    for vl in w_line:
        draw.line((vl,0, vl,height), fill='red')
    
    for hl in h_line:
        draw.line((0,hl, width, hl), fill='blue')

    origin.show()

# area = (((start_x, end_x), xRatio), ((start_y, end_y), yRatio))
def simple_crop_(image_src, area):
    origin = Image.open(image_src)

    w, h = origin.size

    # When divided by xRatio and yRatio, the xy(start~end) region
    left = w/area[0][1] * area[0][0][0]
    right = w/area[0][1] * area[0][0][1]
    top = h/area[1][1] * area[1][0][0]
    bottom = h/area[1][1] * area[1][0][1]

    crroped = origin.crop((left, top, right, bottom))
    
    return crroped

# Get image area using draw_()
weapon_1 = (((14, 15), 20), ((2, 3), 16))
weapon_2 = (((14, 15), 20), ((5, 6), 16))
inventory = (((4,7), 22), ((2, 8), 17))
# Creating additional...

image = 'images/origin.jpeg'
# draw_(image, 22, 17)
simple_crop_(image,weapon_1).show('sample/w1.png')

