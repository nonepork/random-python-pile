from PIL import Image

global the_code
the_code = []

def box_template(x, y, r, g, b):
    r = round(r * (1/255), 4)
    b = round(b * (1/255), 4)
    g = round(g * (1/255), 4)
    return f'mybox = box(pos=vector({x},{y},0), length=1, height=1, width=1, color=vec({r},{g},{b}))'

# Change current_x and current_y's common difference based on pixel's size of your image
filename = 'bee.png'
image = Image.open(filename).convert('RGB')
width, height = image.size
current_y = 4
vec_y = 0
looptime = 1
temp_x, temp_y, temp_r, temp_g, temp_b = 0, 0, 0, 0, 0

while current_y < height:
    vec_x = 0
    current_x = 0
    while current_x < width:
        r, g, b = image.getpixel((current_x, current_y))
        if temp_r == r and temp_g == g and temp_b == b and temp_y == vec_y:
            looptime += 1
        elif looptime > 1:
            the_code.pop(-1)
            temp = box_template('i', temp_y, temp_r, temp_g, temp_b)
            the_code.append(f'''for i in range({temp_x}, {temp_x+looptime}):
    {temp}''' + '\n')
            the_code.append(box_template(vec_x, vec_y, r, g, b,) + '\n')
            temp_x, temp_y, temp_r, temp_g, temp_b = vec_x, vec_y, r, g, b
            looptime = 1
        else:
            the_code.append(box_template(vec_x, vec_y, r, g, b,) + '\n')
            temp_x, temp_y, temp_r, temp_g, temp_b = vec_x, vec_y, r, g, b
        current_x += 4
        vec_x += 1
    current_y += 4
    vec_y -= 1

the_code = ''.join(i for i in the_code)
with open('code.txt', 'w') as f:
    f.write(the_code)
