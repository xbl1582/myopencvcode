import  cv2
import numpy as py

def ThresholdTest(src):
    img=cv2.imread(src);
    dst1=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY);
    dst1=cv2.resize(dst1,(300,300));
    cv2.imshow("dst",dst1);
    cv2.waitKey()
    cv2.destroyAllWindows();
    retval,dst2=cv2.threshold(dst1,127,255,cv2.THRESH_BINARY)
    print(retval)
    cv2.imshow("dst", dst2);
    cv2.waitKey()
    cv2.destroyAllWindows();
    retval,dst3=cv2.threshold(dst1,127,255,cv2.THRESH_BINARY_INV)
    print(retval)
    cv2.imshow("dst", dst3);
    cv2.waitKey()
    cv2.destroyAllWindows();
    retval,dst4=cv2.threshold(dst1,127,255,cv2.THRESH_TOZERO)
    print(retval)
    cv2.imshow("dst", dst4);
    cv2.waitKey()
    cv2.destroyAllWindows();

    retval, dst5 = cv2.threshold(dst1, 127, 255, cv2.THRESH_TOZERO_INV)
    print(retval)
    cv2.imshow("dst", dst5);
    cv2.waitKey()
    cv2.destroyAllWindows();


    retval, dst6 = cv2.threshold(dst1, 127, 255, cv2.THRESH_TRUNC)
    print(retval)
    cv2.imshow("dst", dst6);
    cv2.waitKey()
    cv2.destroyAllWindows();

    dst7=cv2.adaptiveThreshold(dst1,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,5,3);
    cv2.imshow("dst", dst7);
    cv2.waitKey();
    cv2.destroyAllWindows();

    t1,dst8=cv2.threshold(dst1,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU);
    cv2.putText(dst8,"520",(0,30),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,1,(0,0,0),2)
    cv2.imshow("dst", dst8);
    print(t1)
    cv2.waitKey();
    cv2.destroyAllWindows();

def main():
    ThresholdTest('a1.jpg');
if __name__=='__main__':
    main();