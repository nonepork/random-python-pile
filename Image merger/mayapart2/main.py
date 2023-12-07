import time
from PIL import Image

original = 1
for i in range(2, 15):
    image = Image.open(f'{original}.png')
    image_2 = Image.open(f'{i}.png')
    print(original, i)

    new_image = Image.new('RGB', (image.width+85, 100))
    new_image.paste(image, (0, 0))
    new_image.paste(image_2, (85*original, 0))

    new_image.save(f'{i}.png')
    original += 1
time.sleep(100)
