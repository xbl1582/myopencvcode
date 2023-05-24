import random
import time

import cv2
import  numpy as np

def hui_zhi_Line():
    huabu=np.zeros((300,300,3),np.uint8);
    img = cv2.line(huabu, (10,10), (100,200), (255,0,255), 5);
    cv2.imshow("line",img)
    cv2.namedWindow("line", 0)
    cv2.resizeWindow("line", 300, 300)  # 设置窗口大小
    cv2.waitKey()
    cv2.destroyAllWindows()

# 绘制一个王字

def hui_zhi_wuan():
    huabu=np.ones((300,300,3),np.uint8)*255;
    img1 = cv2.line(huabu, (120,30), (170,30), (255,0,255), 5);
    img2 = cv2.line(huabu, (145,30), (145,100), (255,0,255), 5);
    img3 = cv2.line(huabu, (130,60), (160,60), (255,0,255), 5);
    img4 = cv2.line(huabu, (120,100), (170,100), (255,0,255), 5);
    img=np.hstack((img1,img2,img3,img4))
    cv2.imshow("line",img)
    cv2.namedWindow("line", 0)
    cv2.resizeWindow("line", 300, 300)  # 设置窗口大小
    cv2.waitKey()
    cv2.destroyAllWindows()

def hui_zhi_rectangle():
    huabu = np.ones((300, 300, 3), np.uint8) * 255;
    huabu=cv2.rectangle(huabu,(50,50),(100,100),(255,200,200),-1)
    huabu = cv2.rectangle(huabu, (100, 50), (150, 100), (255, 200, 200), 1)
    huabu = cv2.rectangle(huabu, (150, 50), (200, 100), (255, 200, 200), 1)
    huabu = cv2.rectangle(huabu, (200, 50), (250, 100), (255, 200, 200), 1)
    cv2.imshow("rectangle",huabu)
    cv2.namedWindow("rectangle", 0)
    cv2.resizeWindow("rectangle", 300, 300)  # 设置窗口大小
    cv2.waitKey()
    cv2.destroyAllWindows()



def hui_zhi_circle():
    huabu=np.ones((300,300,3),np.uint8)*255;
    c_x=150;
    c_y=150;
    c_r=120
    for i in range(0,10):
        huabu = cv2.circle(huabu, (c_x,c_y), c_r, (0,0, 255), 1);
        c_r-=10;
        if(i==9):
            huabu = cv2.circle(huabu, (c_x, c_y), c_r, (0, 0, 255), -1);
    cv2.imshow("circle", huabu)
    cv2.namedWindow("circle", 0)
    cv2.resizeWindow("circle", 300, 300)  # 设置窗口大小
    cv2.waitKey()
    cv2.destroyAllWindows()


def hui_zhi_randomccircle():
    huabu = np.ones((500, 500, 3), np.uint8) * 255;
    for i in range(0, 27):
        c_x = random.randint(0, 500);
        c_y = random.randint(0, 500);
        c_r = random.randint(11, 70);
        huabu = cv2.circle(huabu, (c_x, c_y), c_r, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), -1);

    cv2.imshow("circle", huabu)
    cv2.namedWindow("circle", 0)
    cv2.resizeWindow("circle", 500, 500)  # 设置窗口大小
    cv2.waitKey()
    cv2.destroyAllWindows()

def hui_zhi_polylines():
    huabu=np.ones((500, 500, 3), np.uint8) * 255;
    pts=np.array([[100,100],[100,200],[200,100],[200,200]]);
    huabu=cv2.polylines(huabu,[pts],False,1);
    cv2.imshow("circle", huabu)
    cv2.namedWindow("circle", 0)
    cv2.resizeWindow("circle", 500, 500)  # 设置窗口大小
    cv2.waitKey()
    cv2.destroyAllWindows()

def hui_zhiwenzi():
    huabu = np.ones((500, 500, 3), np.uint8) * 255;
    huabu=cv2.putText(huabu,"mrsoft",(200,200),cv2.FONT_HERSHEY_TRIPLEX+cv2.FONT_ITALIC,100,(0,0,0),10)
    cv2.imshow("circle", huabu)
    cv2.namedWindow("circle", 0)
    cv2.resizeWindow("circle", 500, 500)  # 设置窗口大小
    cv2.waitKey()
    cv2.destroyAllWindows()
def hui_zhiwenziOnImage():
    # huabu = np.ones((500, 500, 3), np.uint8) * 255;
    image=cv2.imread("a1.JPG");
    huabu=cv2.putText(image,"mrsoft",(20,70),cv2.FONT_HERSHEY_TRIPLEX+cv2.FONT_ITALIC,2,(0,0,0),3,8,True)

    # cv2.namedWindow("circle", 0)
    # cv2.resizeWindow("circle", 300, 300)  # 设置窗口大小
    cv2.imshow("circle", huabu)
    cv2.waitKey()
    cv2.destroyAllWindows()

def dontaicircle():
    width,height=200,200
    r=20
    x=r+20
    y=r+20
    x_offer=y_offer=1
    while cv2.waitKey(1)==-1 :
        if(x>width-r or x<r):
            x_offer*=-1
        if(y>height-r or y<r):
            y_offer*=-1
        x+=x_offer
        y+=y_offer
        img=np.ones((width,height,3),np.uint8)*255
        cv2.circle(img,(random.randint(0,200),random.randint(0,200)),r,(random.randint(0,255),random.randint(0,255),random.randint(0,255)),-1)
        cv2.imshow("img",img)
        time.sleep(1/100);
    cv2.destroyAllWindows();

def main():
    # hui_zhi_Line()
    # hui_zhi_wuan()
    # hui_zhi_rectangle()
    # hui_zhi_circle()
    # hui_zhi_randomccircle()
    # hui_zhi_polylines()
    # hui_zhiwenzi()
    # hui_zhiwenziOnImage()
    dontaicircle()
if __name__=='__main__':
    main()