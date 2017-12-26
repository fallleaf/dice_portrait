from PIL import Image
import numpy as np
import datetime

start_time = datetime.datetime.now()

# 读入色子图形文件
dice = []
<<<<<<< HEAD
for i in range(9):
    dice.append(Image.open('./dice_image/'+str(i+1)+'w.png'))
#    dice[i].show()
    print(i)
=======
for i in range(6):
    dice.append(Image.open('./dice_image/'+str(i+1)+'w.png'))
#    dice[i].show()
>>>>>>> 6920957e7431c5e37afce5a25847e4deddc8b731
# 初始化
factor = int
for factor in range(7, 13):
    im = Image.open("comic.png")
    im = im.convert("L")
    width, hight = im.size
    im = im.resize((int(width*factor/10),int(hight*factor/10)))
    size = im.size
    width, hight = size
    x_max = int(width/16)
    y_max = int(hight/16)
    x = 0
    y = 0
<<<<<<< HEAD
    dice2_rotate = False
    dice3_rotate = False
    dice6_rotate = False
# 定义数组
    image_data = np.arange(y_max*x_max, dtype="uint8").reshape(y_max, x_max)
    block_data = np.arange(16*16, dtype="uint8").reshape(16, 16)
    dice_data = np.arange(y_max*x_max, dtype="uint8").reshape(y_max, x_max)

=======
    dice_rotate = False
# 定义数组
    image_data = np.arange(y_max*x_max).reshape(y_max, x_max)
    block_data = np.arange(16*16).reshape(16, 16)
    dice_data = np.arange(y_max*x_max).reshape(y_max, x_max)
#   dice_data.dtype = 'int16'
>>>>>>> 6920957e7431c5e37afce5a25847e4deddc8b731
# 灰度对应1-6的值
    p = [53,85,117,139,151,203]#原始分组
#    p = [45, 65, 80, 95, 130, 155]
#    p.reverse()
#   计算每个16x16图块的值
    for j in range(y_max):
        for i in range(x_max):
            block_box = (i*16, j*16, (i+1)*16, (j+1)*16)
            b = im.crop(block_box)  # 获得16x16图片
            for ii in range(16):
                for jj in range(16):
                    block_data[jj, ii] = b.getpixel((ii, jj))
<<<<<<< HEAD
            image_data[j, i] = int(np.median(block_data))
=======
            image_data[j, i] = int(np.mean(block_data))
>>>>>>> 6920957e7431c5e37afce5a25847e4deddc8b731
       
            if (image_data[j, i] < p[0]):
                n = 5
            elif (image_data[j, i] >= p[0]) and (image_data[j, i] < p[1]):
                n = 4
            elif (image_data[j, i] >= p[1]) and (image_data[j, i] < p[2]):
                n = 3
            elif (image_data[j, i] >= p[2]) and (image_data[j, i] < p[3]):
                n = 2
            elif(image_data[j, i] >= p[3]) and (image_data[j, i] < p[4]):
                n = 1
            else:
                n = 0

<<<<<<< HEAD
            if (n == 1):
                dice2_rotate = not( dice2_rotate)
                if (dice2_rotate):
                    n = 6
            if (n == 2):
                dice3_rotate = not( dice3_rotate)
                if (dice3_rotate):
                    n = 7
            if (n == 5):
                dice6_rotate = not( dice6_rotate)
                if (dice6_rotate):
                    n = 8
			
            #    if (n == 1):
            #        n = 6
            #    elif ( n == 2):
            #        n = 7
            #    elif ( n == 5 ):
            #        n = 8
            #    else:
            #        n = n
            #dice_rotate = not(dice_rotate)
=======
            if (dice_rotate):
                if (n == 1):
                    n = 6
                elif ( n == 2):
                    n = 7
                elif ( n == 5 ):
                    n = 8
                else:
                    n = n
            # dice_rotate = not(dice_rotate)
>>>>>>> 6920957e7431c5e37afce5a25847e4deddc8b731
            im.paste(dice[n], (i*16, j*16))
            dice_data[j, i] = n+1

#      plt.hist(image_data)
#      plt.show()

#      im.show()
#      print ('max:',np.max(image_data),'min:',np.min(image_data))
      
    print('x:',x_max,'*y:',y_max,'=',x_max*y_max)
    im.show()
    im.save("comic_w_"+ str(factor)+".png")

# 将色子点数写入文件
#     f = open('comic_dice_'+str(factor)+'.txt', 'wt')
#     for y in range(y_max):
#         f.write((str(y+1)+':'))
#         for x in range(x_max):
#             f.write(str(dice_data[y, x])+',')
#         f.write('\n')
#     f.close()
#     print(str(factor)+'Done!')
print('All Done!')
end_time = datetime.datetime.now()
print(end_time-start_time)
