from PIL import Image, ImageDraw

d1=Image.new('L',(16,16))
draw=ImageDraw.Draw(d1)
draw.rectangle((0,0,15,15),fill=(43))
d1.save('1g.png')

d2=Image.new('L',(16,16))
draw=ImageDraw.Draw(d2)
draw.rectangle((0,0,15,15),fill=(86))
d2.save('2g.png')


d3=Image.new('L',(16,16))
draw=ImageDraw.Draw(d3)
draw.rectangle((0,0,15,15),fill=(129))
d3.save('3g.png')

d4=Image.new('L',(16,16))
draw=ImageDraw.Draw(d4)
draw.rectangle((0,0,15,15),fill=(172))
d4.save('4g.png')

d5=Image.new('L',(16,16))
draw=ImageDraw.Draw(d5)
draw.rectangle((0,0,15,15),fill=(215))
d5.save('5g.png')

d6=Image.new('L',(16,16))
draw=ImageDraw.Draw(d6)
draw.rectangle((0,0,15,15),fill=(255))
d6.save('6g.png')
