import  cv2
import numpy as np

# 图片翻转

def overreturnImage(src,flipcode):
        # 0x轴
        # 正数 y轴
        # 负数 x，y
        img=cv2.imread(src);
        img=cv2.resize(img,(300,300));
        cv2.imshow("image",img);
        cv2.resizeWindow("image",300,300)
        cv2.moveWindow("image", 1, 50)
        dest = cv2.flip(img, flipcode);
        cv2.imshow("dest",dest);
        cv2.waitKey();
        cv2.destroyAllWindows()

def main():
        overreturnImage('a1.jpg', 0)
        overreturnImage('a1.jpg', 1)
        overreturnImage('a1.jpg', -1)

if __name__=='__main__':
    main();