import datetime
import os
import sys
import cv2
import numpy as np
#import matplotlib.pyplot as plt

# 获得图片名，色子列数，色子是否旋转
def getvalue():
    if (len(sys.argv) < 2 or len(sys.argv) > 4):
        print("Error, invalid arguments!")
        print("Call with " + sys.argv[0] + " inputimage [tile-size] ")
        sys.exit(1)
    ROTATE = False
    DICE_WIDTH = 50

    if len(sys.argv) == 2:
        imagefile = sys.argv[1]
    elif len(sys.argv) == 3:
        imagefile = sys.argv[1]
        DICE_WIDTH = int(sys.argv[2])
        if (DICE_WIDTH > 150 or DICE_WIDTH < 30):
            print("色子列数不正确，应在30-150之间")
            sys.exit(1)
    else:
        imagefile = sys.argv[1]
        DICE_WIDTH = int(sys.argv[2])
        if (DICE_WIDTH > 150 or DICE_WIDTH < 30):
            print("Dice quality not avialiabe. It betweet 30 and 150")
            sys.exit(1)
        if (sys.argv[3] == '0' or sys.argv[3] == '1'):
            ROTATE = bool(int(sys.argv[3]))
        else:
            print("1:色子旋转, 0:色子不旋转")
            sys.exit(1)
    return imagefile, DICE_WIDTH, ROTATE

def AjustImage(DICE_WIDTH, image):  # 调整图片
    hight, width = image.shape[:2]
    ratio = DICE_WIDTH * 16 / width
    width = int(width * ratio)
    hight = int(hight * ratio)
    image = cv2.resize(image, (width, hight))
    return width, hight, image


def getDice(DICEPATH):  # 读入色子图形文件
    dice = np.zeros((9, 16, 16),dtype='u8')
    for i in range(9):
        dice[i] = cv2.imread('./dice_image/' + str(i + 1) + 'w.png', 0)
    return dice

def calculateDice(im, imagefile, p, dice, ROTATE):  # 处理图片

    x_max = int((im.shape[1]/16))
    y_max = int((im.shape[0]/16))

    #b = np.arange(256, dtype="u8").reshape(16, 16)


    dice_data = np.arange(y_max * x_max, dtype="u8").reshape(y_max, x_max)

    dice2_rotate = False
    dice3_rotate = False
    dice6_rotate = False

    cv2.namedWindow(imagefile, 0)
    cv2.resizeWindow(imagefile, 640, int(640 * y_max / x_max))    


    for j in range(y_max):
        for i in range(x_max):

            # 获得16x16图片的色度平均值/中位数
            #b = im[j * 16:(j + 1) * 16, i * 16:(i + 1) * 16]
            #image_data = int(np.mean(b))
            image_data = int(np.mean(im[j * 16:(j + 1) * 16, i * 16:(i + 1) * 16]))

            # 根据色度值确定色子点数
            if (image_data < p[0]):
                n = 5
                if (ROTATE):
                    dice6_rotate = not (dice6_rotate)
                    if (dice6_rotate):
                        n = 8
            elif (image_data >= p[0]) and (image_data < p[1]):
                n = 4
            elif (image_data >= p[1]) and (image_data < p[2]):
                n = 3
            elif (image_data >= p[2]) and (image_data < p[3]):
                n = 2
                if (ROTATE):
                    dice3_rotate = not (dice3_rotate)
                    if (dice3_rotate):
                        n = 7
            elif (image_data >= p[3]) and (image_data < p[4]):
                n = 1
                if (ROTATE):
                    dice2_rotate = not (dice2_rotate)
                    if (dice2_rotate):
                        n = 6
            else:
                n = 0

            im[j * 16:(j + 1) * 16, i * 16:(i + 1) * 16] = dice[n]
            dice_data[j, i] = n + 1

            #cv2.imshow(imagefile, im)
            #cv2.waitKey(1)
    return im, dice_data


def write_Dice(im, OUTPUTPATH, imagefile, dice_data):  # 将色子点数写入文件
    y_max, x_max = np.shape(dice_data)

    DICE_WIDTH = x_max
    print("色子数量", y_max, '*', x_max, '=', x_max * y_max)
    cv2.imwrite(OUTPUTPATH + str(DICE_WIDTH) + '_hist_' + imagefile, im)
    f = open(OUTPUTPATH + str(DICE_WIDTH) + '_hist_' + imagefile + '.txt', 'wt')

    for y in range(y_max):
        f.write((str(y + 1) + ':'))
        for x in range(x_max):
            f.write(str(dice_data[y, x]) + ',')
        f.write('\n')
    f.close()
    print('文件保存完毕!')
    return 


def main():

    start_time = datetime.datetime.now()

    #初始化文件路径
    EXEC_PATH = os.getcwd()
    DICEPATH = EXEC_PATH + '\\dice_image\\'
    OUTPUTPATH = EXEC_PATH + '\\output\\'
    if not (os.path.exists(OUTPUTPATH)):
        os.mkdir(OUTPUTPATH)

    #获得命令行输入参数 
    imagefile, DICE_WIDTH, ROTATE = getvalue()
    
    #读取要渲染的图片及色子图片
    im = cv2.imread(imagefile, 0)
    dice = getDice(DICEPATH)
    
    
    #调整图片大小
    width, hight, im = AjustImage(DICE_WIDTH, im)

    # 定义数组 可以不定义，自定义函数中已定义，自然继承类型
    #image_data = np.arange(y_max * x_max, dtype="u8").reshape(y_max, x_max)
    #dice_data = np.arange(y_max * x_max, dtype="u8").reshape(y_max, x_max)

    # 灰度对应色子1-6的值
    #p = [53,85,117,139,151,203]#原始分组
    #p = [60, 65, 80, 90, 140, 150]
    #p = [75, 90, 100, 110, 120, 200]
    p = [60, 80, 110, 150, 190, 220]

    im, dice_data = calculateDice(im, imagefile, p, dice, ROTATE)
    write_Dice(im, OUTPUTPATH, imagefile, dice_data)

    end_time = datetime.datetime.now()
    print('程序运行时间:', end_time - start_time,'秒')
    cv2.imshow(imagefile, im)
    cv2.waitKey(0)


if __name__ == "__main__":
    main()