import  cv2
import numpy as np

def changeB2G(src):
    image=cv2.imread(src);
    cv2.namedWindow("src", 0)
    cv2.resizeWindow("src", 400, 300)  # 设置窗口大小
    cv2.imshow("src", image);
    cv2.waitKey(0)
    cv2.destroyAllWindows();

    # 灰度空间
    dest = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.namedWindow("gray", 0)
    cv2.resizeWindow("gray", 400, 300)  # 设置窗口大小
    cv2.imshow("gray", dest);
    cv2.waitKey(0)
    cv2.destroyAllWindows();

def changeBGR2HSV(src):
    image = cv2.imread(src);
    cv2.namedWindow("src", 0)
    cv2.resizeWindow("src", 400, 300)  # 设置窗口大小
    cv2.imshow("src", image);
    cv2.waitKey(0)
    cv2.destroyAllWindows();

    # BGR转HSV空间
    dest = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    cv2.namedWindow("hsv", 0)
    cv2.resizeWindow("hsv", 400, 300)  # 设置窗口大小
    cv2.imshow("hsv", dest);
    cv2.waitKey(0)
    cv2.destroyAllWindows();

    #  HSV转BGR空间
    image2 = cv2.cvtColor(dest, cv2.COLOR_HSV2BGR)
    cv2.namedWindow("bgr", 0)
    cv2.resizeWindow("bgr", 400, 300)  # 设置窗口大小
    cv2.imshow("bgr", image2);
    cv2.waitKey(0)
    cv2.destroyAllWindows();
#     拆分通道
def splitibgrmage(src):
    image=cv2.imread(src);
    b,g,r=cv2.split(image);
    cv2.namedWindow("B", 0)
    cv2.resizeWindow("B", 400, 300)  # 设置窗口大小
    cv2.imshow('B',b);
    cv2.waitKey()
    cv2.destroyAllWindows()

    cv2.namedWindow("g", 0)
    cv2.resizeWindow("g", 400, 300)  # 设置窗口大小
    cv2.imshow('g', g);
    cv2.waitKey()
    cv2.destroyAllWindows()


    cv2.namedWindow("r", 0)
    cv2.resizeWindow("r", 400, 300)  # 设置窗口大小
    cv2.imshow('r', r);
    cv2.waitKey()
    cv2.destroyAllWindows()

#     合成图片
    dest=cv2.merge([b,g,r])
    cv2.namedWindow("dest", 0)
    cv2.resizeWindow("dest", 400, 300)  # 设置窗口大小
    cv2.imshow('dest',dest)
    cv2.waitKey()
    cv2.destroyAllWindows()
#     拆分通道
def splitibgramage(src):
    image=cv2.imread(src);
    image=cv2.cvtColor(image,cv2.COLOR_BGR2BGRA);
    b,g,r,a=cv2.split(image);
    print(a)
    cv2.namedWindow("B", 0)
    cv2.resizeWindow("B", 400, 300)  # 设置窗口大小
    cv2.imshow('B',b);
    cv2.waitKey()
    cv2.destroyAllWindows()

    cv2.namedWindow("g", 0)
    cv2.resizeWindow("g", 400, 300)  # 设置窗口大小
    cv2.imshow('g', g);
    cv2.waitKey()
    cv2.destroyAllWindows()


    cv2.namedWindow("r", 0)
    cv2.resizeWindow("r", 400, 300)  # 设置窗口大小
    cv2.imshow('r', r);
    cv2.waitKey()
    cv2.destroyAllWindows()
    # a[:, :] = 0;
    a[:,:]=172;
#     合成图片
    dest=cv2.merge([b,g,r,a])
    cv2.namedWindow("dest", 0)
    cv2.resizeWindow("dest", 400, 300)  # 设置窗口大小
    cv2.imshow('dest',dest)
    cv2.imwrite("C:/Users/GDWT34/Desktop/dest.png", dest)
    cv2.waitKey()
    cv2.destroyAllWindows()

    a[:, :] = 0;
    dest2 = cv2.merge([b, g, r, a])
    cv2.namedWindow("dest2", 0)
    cv2.resizeWindow("dest2", 400, 300)  # 设置窗口大小
    cv2.imshow('dest2', dest)
    cv2.imwrite("C:/Users/GDWT34/Desktop/dest2.png",dest2)
    cv2.waitKey()
    cv2.destroyAllWindows()
def splitiHsvmage(src):
    image=cv2.imread(src);
    image=cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h,s,v=cv2.split(image);
    cv2.namedWindow("h", 0)
    cv2.resizeWindow("h", 400, 300)  # 设置窗口大小
    cv2.imshow('h',h);
    cv2.waitKey()
    cv2.destroyAllWindows()

    cv2.namedWindow("s", 0)
    cv2.resizeWindow("s", 400, 300)  # 设置窗口大小
    cv2.imshow('s', s);
    cv2.waitKey()
    cv2.destroyAllWindows()


    cv2.namedWindow("v", 0)
    cv2.resizeWindow("v", 400, 300)  # 设置窗口大小
    cv2.imshow('v', v);
    cv2.waitKey()
    cv2.destroyAllWindows()
    # print(h)
    h[:,:]=180
    # print(h)
    # print(s)
    # s[:, :] =255
    # print(s)
    # print(v)
    # v[:, :] = 0
    # print(v)
#     合成图片
    dest=cv2.merge([h,s,v])
    dest= cv2.cvtColor(dest, cv2.COLOR_HSV2BGR)
    cv2.namedWindow("dest", 0)
    cv2.resizeWindow("dest", 400, 300)  # 设置窗口大小
    cv2.imshow('dest',dest)
    cv2.waitKey()
    cv2.destroyAllWindows()



def main():
    path="a1.JPG"
    # changeB2G(path);
    # changeBGR2HSV(path)
    # splitibgrmage(path)
    # splitibgramage(path)
    splitiHsvmage(path)

if __name__=='__main__':
    main()