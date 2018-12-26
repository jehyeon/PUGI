from PIL import Image, ImageDraw
image = './image.jpeg'

def draw_(image, wRatio, hRatio):
    origin = Image.open(image)
    width, height = origin.size

    w_line = [w for w in range(0, width, int(width/wRatio))]
    h_line = [h for h in range(0, height, int(height/hRatio))]

    draw = ImageDraw.Draw(origin)
    for vl in w_line:
        draw.line((vl,0, vl,h), fill='red')
    
    for hl in h_line:
        draw.line((0,hl, w, hl), fill='blue')

    origin.show()

# draw_(image, 17, 16)

# 위 함수를 통해 weapon 좌표를 구함
# weapon1 = (12/17, 2/16), weapon2 = (12/17, 5/16)


original = Image.open(image)
# original.show()

w, h = original.size

# Weapon Info 1
left = w/17 * 12
top = h/16 * 2
right = w/17 * 13
bottom = h/16 * 3
crroped = original.crop((left, top, right, bottom))

# Weapon Info 2

crroped.save('./test.jpg')
