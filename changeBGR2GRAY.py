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


def main():
    path="a1.JPG"
    # changeB2G(path);
    changeBGR2HSV(path)

if __name__=='__main__':
    main()