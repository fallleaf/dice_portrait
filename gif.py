from PIL import Image,ImageDraw,ImageFont

# text=['42x59=2478','49x69=3381','56x79=4424','63x89=5607','70x99=6390','77x108=8316','84x118=9912','91x128=11648','98x138=13524']

im =[]

for i in range(8):
        im.append(Image.open('comic_g_'+str(i+5)+'.png'))
img_size = (672, 806)
im[0] = im[0].resize(img_size, Image.ANTIALIAS)
im[0] = im[0].convert('L')

# draw = ImageDraw.Draw(im[0])
# newfont=ImageFont.truetype('C:\Windows\Fonts\simsun.ttc',30)
# draw.text((5,5),text[0],255,font=newfont)
# im[0].show()
images_gif = []
for i in range(1, 8):
#    if i == 4 :
#        print(10)
#    else:
        
        im[i] = im[i].resize(img_size, Image.ANTIALIAS)
        im[i] = im[i].convert('L')

        print(i)
#        draw = ImageDraw.Draw(im[i])
#        newfont=ImageFont.truetype('C:\Windows\Fonts\simsun.ttc',30)
#        draw.text((5,5),text[i],255,font=newfont)
        
#        im[i].show()
        images_gif.append(im[i])

for i in range(3):
        images_gif.append(im[7])

# for i in range(7, 0, -1):
#         print(i)
#         im[i] = im[i].resize(img_size, Image.ANTIALIAS)
#         im[i] = im[i].convert('L')
#         images_gif.append(im[i])
# for i in range(3):
#         images_gif.append(im[0])
im[0].save('comic.gif',save_all=True,append_images=images_gif,loop=0,duration=100)