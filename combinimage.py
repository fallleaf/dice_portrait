from PIL import Image
arr = ['cecilia.png','ceciliag.png','ceciliab.png','ceciliaw.png']

toImage = Image.new('L',(2240,3168))
x = 0
for  i in range(2):
       for j in range(2):
              fromImage = Image.open(arr[x])
#              fromImage.show()
#              print(arr[x])
              x+=1
#              print (x)
              location=((j*1120,i*1584,(j+1)*1120,(i+1)*1584))
              toImage.paste(fromImage,location)

toImage.show()
toImage.save('cecilia_orgin.png')
smallImage=toImage.resize((1120,1584),Image.ANTIALIAS)
smallImage.show()
print (smallImage.size)
smallImage.save('cecilia_small.png',quality=95)

