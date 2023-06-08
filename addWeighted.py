import  cv2
import  numpy as np

# 图像合并

def addweighted(src1,alpha,src2,beta,gamma):
    img=cv2.imread(src1)
    img=cv2.resize(img,(300,300))
    img2=cv2.imread(src2)
    img2=cv2.resize(img2,(300, 300))
    rows,colmns,channel=img.shape
    img2=cv2.resize(img2,(colmns,rows))
    img=cv2.addWeighted(img,alpha,img2,beta,gamma)
    cv2.imshow('1',img)
    cv2.imshow('2', img2)
    cv2.imshow('3',img)
    cv2.waitKey()
    cv2.destroyAllWindows()

def addweighted2():
    img1 = cv2.imread('a1.jpg');
    img1 = cv2.resize(img1, (200, 200))
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2BGRA)
    cv2.imshow('0', img1)

    img2 = cv2.imread('a2.png')
    img2=cv2.resize(img2,(45,85))
    img2=cv2.cvtColor(img2,cv2.COLOR_BGR2BGRA)
    # img3=cv2.add(img1,img2);
    # cv2.imshow('1',img3)

    mask = np.ones(img1.shape, np.uint8)
    mask=cv2.cvtColor(mask,cv2.COLOR_BGR2BGRA);
    b,g,r,a=cv2.split(mask)
    a[:, :] = 1;
    mask=cv2.merge([b,g,r,a]);
    mask[30:115, 15:60, :] = img2
    cv2.imshow('2', mask)

    # img4=cv2.add(img1,img2,mask=mask)
    # img4=cv2.bitwise_and(img1,mask)
    # img4=cv2.bitwise_or(img1,mask)
    # img4=cv2.bitwise_not(img1,mask)
    img4 = cv2.addWeighted(img1,1,mask,0.6,-20)
    cv2.imshow('3', img4)
    cv2.imwrite('a3.png',img4)
    cv2.waitKey()
    cv2.destroyAllWindows()
def fugai():
    img1 = cv2.imread('a1.jpg');
    img1 = cv2.resize(img1, (200, 200))
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2BGRA)
    cv2.imshow('0', img1)

    img2 = cv2.imread('a2.png')
    img2 = cv2.resize(img2, (45,115))
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2BGRA)
    # img3=cv2.add(img1,img2);
    # cv2.imshow('1',img3)
    rows,colms,channel=img2.shape
    img1[30:145,15:60,:]=img2
    cv2.imshow('2',img1)
    cv2.waitKey()
    cv2.destroyAllWindows()

def main():
    # addweighted('a1.jpg',0.6,'a2.png',0.6,0);
    # addweighted2();
    fugai()
if __name__=='__main__':
    main();


