from PIL import Image
import os
#Source https://www.tutorialspoint.com/python_pillow/Python_pillow_merging_images.htm

if 'placeholder.png' not in os.listdir():
        image = Image.open(os.listdir()[0])
        image_size = image.size
        new_image = Image.new('RGB',(image_size[0], image_size[1]))
        new_image.paste(image,(0,0))
        new_image.save("placeholder.png", "PNG")
for i in os.listdir(): 
    if i.endswith('.png') and 'placeholder' not in i:
        image1 = Image.open("placeholder.png")
        image2 = Image.open(i)
        image1_size = image1.size
        image2_size = image2.size
        new_image = Image.new('RGB',(image1_size[0]+image2_size[0], image1_size[1]))
        new_image.paste(image1,(0,0))
        new_image.paste(image2,(image1_size[0],0))
        new_image.save("placeholder.png", "PNG")
