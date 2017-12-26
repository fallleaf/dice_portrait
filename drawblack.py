from PIL import Image, ImageDraw


dice1= Image.new('L',(16,16))
draw= ImageDraw.Draw(dice1)
draw.rectangle((0,0,15,15),fill='black')
draw.rectangle((6,6,9,9),fill='white')
dice1.save('1b.png')


dice2= Image.new('L',(16,16))
draw= ImageDraw.Draw(dice2)
draw.rectangle((0,0,15,15),fill='black')
draw.rectangle((3,3,6,6),fill='white')
draw.rectangle((9,9,12,12),fill='white')
dice2.save('2b.png')



dice3= Image.new('L',(16,16))
draw= ImageDraw.Draw(dice3)
draw.rectangle((0,0,15,15),fill='black')
draw.rectangle((1,1,4,4),fill='white')
draw.rectangle((6,6,9,9),fill='white')
draw.rectangle((11,11,14,14),fill='white')
dice3.save('3b.png')



dice4= Image.new('L',(16,16))
draw= ImageDraw.Draw(dice4)
draw.rectangle((0,0,15,15),fill='black')
draw.rectangle((3,3,6,6),fill='white')
draw.rectangle((9,3,12,6),fill='white')
draw.rectangle((3,9,6,12),fill='white')
draw.rectangle((9,9,12,12),fill='white')
dice4.save('4b.png')


dice5= Image.new('L',(16,16))
draw= ImageDraw.Draw(dice5)
draw.rectangle((0,0,15,15),fill='black')
draw.rectangle((1,1,4,4),fill='white')
draw.rectangle((11,1,14,4),fill='white')
draw.rectangle((6,6,9,9),fill='white')
draw.rectangle((1,11,4,14),fill='white')
draw.rectangle((11,11,14,14),fill='white')
dice5.save('5b.png')


dice6= Image.new('L',(16,16))
draw= ImageDraw.Draw(dice6)
draw.rectangle((0,0,15,15),fill='black')
draw.rectangle((3,1,6,4),fill='white')
draw.rectangle((9,1,12,4),fill='white')
draw.rectangle((3,6,6,9),fill='white')
draw.rectangle((9,6,12,9),fill='white')
draw.rectangle((3,11,6,14),fill='white')
draw.rectangle((9,11,12,14),fill='white')
dice6.save('6b.png')
