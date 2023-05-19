import  cv2
import  numpy

def operationimage(filepath):
    image=cv2.imread(filepath,1);#读取图片
    px=image[291,218];#读取图片上坐标291，218的像素
    print(px);#打印 得到的是改像素点上的bgr(rgb)值
    #获取单个轨道的b，g，r值
    blue=image[291,218,0];
    green = image[291, 218, 1];
    red = image[291, 218, 2];
    print("红",red);
    print("蓝", blue);
    print("绿", green);
    px=[0,0,0]
    print(px)
    cv2.imwrite(filepath,image)
    blue = image[291, 218, 0];
    green = image[291, 218, 1];
    red = image[291, 218, 2];
    print("红", red);
    print("蓝", blue);
    print("绿", green);

def changeImage(foldname,filepath):
        image=cv2.imread(filepath,1);
        cv2.imshow("2.1",image);
        for i in range(0,250):
            for j in range(0,250):
                image[i,j]=[0,0,0]
        cv2.imshow('2',image);
        cv2.imwrite(foldname+"/2."+filepath.split(".")[1],image);
        cv2.waitKey(0)
        cv2.destroyAllWindows()
