import cv2
import numpy as np

def pingjie():
    # 水平拼接
    array=np.array
    a=array([1,2,3,4])
    b=array([5,6,7,8])
    c=array([9,10,11,12])
    array=np.hstack((a,b,c))
    print(array)
    
def cuizhipingjie():
    array=np.array
    a=array([1,2,3,4])
    b=array([5,6,7,8])
    c=array([9,10,11,12])
    array=np.vstack((a,b,c))
    print(array)
    
def pingjieimg():
    path= "a1.JPG"
    image=cv2.imread(path)
    cv2.namedWindow("text", 0)
    cv2.resizeWindow("text", 400, 300) #设置窗口大小
    cv2.imshow('text',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    image=np.hstack((image,image))
    cv2.namedWindow("text", 0)
    cv2.resizeWindow("text", 400, 300) #设置窗口大小
    cv2.imshow('text',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    image=np.vstack((image,image))
    cv2.namedWindow("text", 0)
    cv2.resizeWindow("text", 400, 300) #设置窗口大小
    cv2.imshow('text',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def main():
    # pingjie()
    # cuizhipingjie()
    pingjieimg()
    
 
if __name__ == '__main__':
    main()

