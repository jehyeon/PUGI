from PIL import Image, ImageDraw
image = './image.jpeg'

def draw_(image, wRatio, hRatio):
    origin = Image.open(image)
    width, height = origin.size

    w_line = [w for w in range(0, width, int(width/wRatio))]
    h_line = [h for h in range(0, height, int(height/hRatio))]

    draw = ImageDraw.Draw(origin)
    for vl in w_line:
        draw.line((vl,0, vl,height), fill='red')
    
    for hl in h_line:
        draw.line((0,hl, width, hl), fill='blue')

    origin.show()

draw_(image, 20, 16)

# 위 함수를 통해 weapon 좌표를 구함
# weapon1 = (12/17, 2/16), weapon2 = (12/17, 5/16)


original = Image.open(image)
# original.show()

w, h = original.size

# Weapon Info 1
left = w/20 * 14
top = h/16 * 2
right = w/20 * 15
bottom = h/16 * 3
crroped1 = original.crop((left, top, right, bottom))
crroped1.save('./text1.jpg')

# Weapon Info 2
# left = w/20 * 14
# top = h/16 * 5
# right = w/20 * 15
# bottom = h/16 * 6
# crroped2 = original.crop((left, top, right, bottom))

# crroped2.show()
# crroped2.save('./test2.jpg')
