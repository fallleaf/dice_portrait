import numpy as np
import datetime
import cv2
import os, sys



def getInput():# 获得图片名，色子列数，色子是否旋转
    if (len(sys.argv) < 2 or len(sys.argv)> 4):
        print("Error, invalid arguments!")
        print("Call with " + sys.argv[0] + " inputimage [tile-size] ")
        sys.exit(1)

    if len(sys.argv) == 2:
        IMAGEFILE = sys.argv[1]
        DICE_WIDTH = 50
        ROTATE = False
    elif len(sys.argv) == 3 :
        IMAGEFILE = sys.argv[1]
        DICE_WIDTH = int(sys.argv[2])
        if (DICE_WIDTH > 150 or DICE_WIDTH < 30):
            print("Dice quality not avialiabe. It betweet 30 and 150")
            sys.exit(1)
        ROTATE = False
    else:
        IMAGEFILE = sys.argv[1]
        DICE_WIDTH = int(sys.argv[2])
        if (DICE_WIDTH > 150 or DICE_WIDTH < 30):
            print("Dice quality not avialiabe. It betweet 30 and 150")
            sys.exit(1)
        if (sys.argv[3] == '0' or sys.argv[3] == '1'):
            ROTATE = bool(int(sys.argv[3]))
        else:
            print("1:rotate, 0:no rotate")
            sys.exit(1)
    return IMAGEFILE, DICE_WIDTH, ROTATE

def  AjustImage(DICE_WIDTH, image):# 调整图片
    hight, width = image.shape[:2]
    ratio = DICE_WIDTH*16/width
    width = int(width*ratio)
    hight = int(hight*ratio)
    image = cv2.resize(image, (width, hight))
    return width, hight, image
    


def getDice(DICEPATH):# 读入色子图形文件
    dice = []
    for i in range(9):
        dice.append(cv2.imread(DICEPATH + str(i+1) + 'w.png',0))
    return dice

    

def calculateDice(im, IMAGEFILE, p, dice, y_max, x_max, ROTATE):# 计算每个16x16图块的值
    cv2.namedWindow(IMAGEFILE, 0);
    cv2.resizeWindow(IMAGEFILE, 560, 792);
    block_data = np.arange(16 * 16, dtype="uint8").reshape(16, 16)
    b = np.arange(16*16, dtype="uint8").reshape(16,16)
    image_data = np.arange(y_max * x_max, dtype="uint8").reshape(y_max, x_max)
    dice_data = np.arange(y_max * x_max, dtype="uint8").reshape(y_max, x_max)
    dice2_rotate = False
    dice3_rotate = False
    dice6_rotate = False
    for j in range(y_max):
        for i in range(x_max):
            # 获得16x16图片
            b = im[j*16:(j+1)*16, i*16:(i+1)*16]
            for ii in range(16):
                for jj in range(16):
                    block_data[ii, jj] = b[ii, jj]
                image_data[j, i] = int(np.median(block_data))
                # 根据色度值确定色子点数
            if (image_data[j, i] < p[0]):
                n = 5
            elif (image_data[j, i] >= p[0]) and (image_data[j, i] < p[1]):
                n = 4
            elif (image_data[j, i] >= p[1]) and (image_data[j, i] < p[2]):
                n = 3
            elif (image_data[j, i] >= p[2]) and (image_data[j, i] < p[3]):
                n = 2
            elif (image_data[j, i] >= p[3]) and (image_data[j, i] < p[4]):
                n = 1
            else:
                n = 0
            #2，3，6色子是否旋转    
            if (ROTATE):
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
            im[j*16:(j+1)*16, i*16:(i+1)*16] = dice[n]
            dice_data[j, i] = n + 1

            cv2.imshow(IMAGEFILE, im)
            cv2.waitKey(1)
    return im, dice_data
    
def write_Dice(im, OUTPUTPATH, IMAGEFILE, DICE_WIDTH, y_max, x_max, dice_data):# 将色子点数写入文件

    cv2.imwrite(OUTPUTPATH + str(DICE_WIDTH)+IMAGEFILE, im)
    f = open(OUTPUTPATH + str(DICE_WIDTH) + IMAGEFILE + '.txt', 'wt')
    for y in range(y_max):
        f.write((str(y+1)+':'))
        for x in range(x_max):
            f.write(str(dice_data[y, x])+',')
        f.write('\n')
    f.close()
    return 'Job Done!'    
def main():
   
    start_time = datetime.datetime.now()
    EXEC_PATH = os.getcwd()
    IMAGEFILE, DICE_WIDTH, ROTATE = getInput()  
    DICEPATH = EXEC_PATH+'\\dice_image\\'
    OUTPUTPATH = EXEC_PATH +'\\output\\'
    IMAGEPATH = EXEC_PATH+'\\'+IMAGEFILE     
      
    dice = getDice(DICEPATH)
    # 初始化
    im = cv2.imread(IMAGEFILE, 0)
    width, hight ,im = AjustImage(DICE_WIDTH, im)
    x_max = int(width/16)
    y_max = int(hight/16)
    
    


    # 定义数组
    image_data = np.arange(y_max * x_max, dtype="uint8").reshape(y_max, x_max)
    dice_data = np.arange(y_max * x_max, dtype="uint8").reshape(y_max, x_max)
    

    # 灰度对应1-6的值
    # p = [53,85,117,139,151,203]#原始分组
    # p = [45, 65, 80, 95, 130, 155]
    p = [75, 95, 110, 125, 160, 200]


    im, dice_data = calculateDice(im, IMAGEFILE, p, dice, y_max, x_max, ROTATE)

    print(write_Dice(im, OUTPUTPATH, IMAGEFILE, DICE_WIDTH, y_max, x_max, dice_data))
        
    end_time = datetime.datetime.now()
    print(end_time-start_time)

    cv2.imshow(IMAGEFILE, im)
    cv2.waitKey(0)

if __name__ == "__main__":
    main()