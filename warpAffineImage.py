import random

import  cv2
import  numpy as np

def warpaffinelImage(src):
    img = cv2.imread(src);
    img = cv2.resize(img, (300, 300));
    cv2.imshow("img", img);
    cv2.resizeWindow("img", 300, 300)
    cv2.moveWindow("img",600,50)
    cv2.waitKey()

    # M=np.zeros((2,3),np.float32)
    # M=np.ones((2,3),np.float32)
    M=np.float32([[random.randint(0,5),random.randint(0,5),random.randint(0,2)],
                  [random.randint(0,3),random.randint(0,6),random.randint(0,5)],
                  ])
    img = cv2.resize(img, (100, 100));
    dst=cv2.warpAffine(img,M,(400,400));
    cv2.imshow('dst',dst);
    cv2.resizeWindow("dst", (400, 400))
    cv2.moveWindow("dst", 600, 50)
    cv2.waitKey()
    cv2.destroyAllWindows();

def translationImage(src):
    img = cv2.imread(src);
    img = cv2.resize(img, (300, 300));
    cv2.imshow("img", img);
    cv2.resizeWindow("img", 300, 300)
    cv2.moveWindow("img", 600, 50)
    cv2.waitKey()

    M = np.float32([[1,0,20],[0,1,20]])
    img = cv2.resize(img, (300, 300));
    dst = cv2.warpAffine(img, M, (400, 400));
    cv2.imshow('dst', dst);
    cv2.resizeWindow("dst", (400, 400))
    cv2.moveWindow("dst", 600, 50)
    cv2.waitKey()
    cv2.destroyAllWindows();

def RotationImage(src):
    img = cv2.imread(src);
    center=(300/2,300/2)
    print(center)
    img=cv2.resize(img,(300,300))
    M = cv2.getRotationMatrix2D(center,30,0.8)
    dst=cv2.warpAffine(img,M,(300,300))
    cv2.imshow('dst',dst );
    cv2.resizeWindow("dst", (300, 300))
    cv2.moveWindow("dst", 600, 50)
    cv2.waitKey()
    cv2.destroyAllWindows();

def AffineTransFormImage(src):
    img = cv2.imread(src);
    point1 =   np.float32([[0, 0], [300, 0], [0, 300]]);
    point2=  np.float32([[50,0],[299,0],[0,299]])
    img=cv2.resize(img,(300,300))
    M = cv2.getAffineTransform(point1,point2)
    dst=cv2.warpAffine(img,M,(300,300))
    cv2.imshow('dst',dst);
    cv2.resizeWindow("dst", (300, 300))
    cv2.moveWindow("dst", 600, 50)
    cv2.waitKey()
    cv2.destroyAllWindows();

def main():
    # warpaffinelImage('a1.JPG')
    # translationImage('a1.JPG')
   AffineTransFormImage('a1.JPG')
if __name__=='__main__':
    main();