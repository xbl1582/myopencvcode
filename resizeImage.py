import  cv2
import  numpy as np
# 图片的放大与缩小
def resizeImagedsize(src,dsize):
    img=cv2.imread(src);
    dest1=cv2.resize(img,dsize);
    cv2.imshow("image",img)
    cv2.imshow("dest1", dest1)
    cv2.waitKey(0)
    cv2.destroyAllWindows();

def resizeImageFxFy(src,fx,fy):
    img = cv2.imread(src);
    dest1 = cv2.resize(img, None,fx=fx,fy=fy);
    cv2.imshow("image", img)
    cv2.imshow("dest1", dest1)
    cv2.waitKey(0)
    cv2.destroyAllWindows();

def main():
    # resizeImagedsize('a1.jpg',(300,300));
    resizeImageFxFy('a1.jpg', 1 / 10, 1 / 10)

if __name__=='__main__':
    main()