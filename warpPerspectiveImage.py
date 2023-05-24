import  cv2
import  numpy as np

def warpPerspectiveImage(src):
    img = cv2.imread(src);
    img=cv2.resize(img,(300,300))
    rows=300
    cols=300
    p1=np.zeros((4,2),np.float32)
    p1[0]=[0,0]
    p1[1]=[cols-1,0]
    p1[2]=[0,rows-1]
    p1[3]=[cols-1,rows-1]
    p2 = np.zeros((4, 2), np.float32)
    p2[0] = [90, 0]
    p2[1] = [cols - 90, 0]
    p2[2] = [0, rows - 1]
    p2[3] = [cols - 1, rows - 1]
    M=cv2.getPerspectiveTransform(p1,p2)
    dst=cv2.warpPerspective(img,M,(300,300))
    cv2.imshow('dst', dst);
    cv2.resizeWindow("dst", (300, 300))
    cv2.moveWindow("dst", 600, 50)
    cv2.waitKey()
    cv2.destroyAllWindows();

def main():
    # warpaffinelImage('a1.JPG')
    # translationImage('a1.JPG')
   warpPerspectiveImage('a1.JPG')
if __name__=='__main__':
    main();