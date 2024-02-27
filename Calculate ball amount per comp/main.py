from PIL import Image

img = Image.open("fixed.png")
img_RGB = img.convert("RGB")

count = 0

for i in range(img_RGB.size[0]):
    colors = img_RGB.getpixel((i, 5))

    if colors[0] == 63 and colors[1] == 63 and colors[2] == 60:
        count += 1

print("Ball count: " + str(count))
