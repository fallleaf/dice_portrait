from PIL import Image

img = Image.open('./dice_image/7w.png')
img.show()
rotate_img = img.rotate(90)
rotate_img.show()
rotate_img.save('./dice_image/2w.png')