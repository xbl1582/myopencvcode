import cv2
import numpy as np

def yanmo():
    mask=np.zeros((150,150,3),np.uint8)
    mask[50:100,20:80,:]=255
    cv2.imshow("mask1",mask)
    mask[:,:,:]=255
    mask[50:100,20:80,:]=0
    cv2.imshow("mask2",mask)
    cv2.waitKey()
    cv2.destroyAllWindows()
def pitrue():
    img1=np.zeros((150,150,3),np.uint8)
    img1[:,:,0]=255
    img2 = np.zeros((150, 150, 3), np.uint8)
    img2[:, :, 1] = 255
    img3 = np.zeros((150, 150, 3), np.uint8)
    img3[:, :, 2] = 255
    cv2.imshow("1",img1)
    cv2.imshow("2", img2)
    cv2.imshow("3", img3)

    img4=img1+img2;
    cv2.imshow('4',img4)

    img5=img2+img3
    cv2.imshow('5', img5)

    img6=img4+img3
    cv2.imshow('6',img6)
    cv2.waitKey()
    cv2.destroyAllWindows()
def yanmooirtue():
    img1 = np.zeros((150, 150, 3), np.uint8)
    img1[:, :, 0] = 255
    img2 = np.zeros((150, 150, 3), np.uint8)
    img2[:, :, 2] = 255
    img3=cv2.add(img1,img2);
    cv2.imshow('1',img3)

    mask=np.zeros((150,150,1),np.uint8)
    mask[50:100,50:100,:]=255
    cv2.imshow('2',mask)

    img4=cv2.add(img1,img2,mask=mask)
    cv2.imshow('3',img4)

    cv2.waitKey()
    cv2.destroyAllWindows()

def yanmooirtue2():
    img1=cv2.imread('a1.jpg');
    img1=cv2.resize(img1,(200,200))
    cv2.imshow('0', img1)
    img2 = np.zeros((200, 200, 3), np.uint8)
    img2[:, :, 2] =0
    # img3=cv2.add(img1,img2);
    # cv2.imshow('1',img3)

    mask=np.zeros(img1.shape,np.uint8)
    mask[40:135, 65:135, :] = 255
    cv2.imshow('2',mask)

    # img4=cv2.add(img1,img2,mask=mask)
    # img4=cv2.bitwise_and(img1,mask)
    # img4=cv2.bitwise_or(img1,mask)
    # img4=cv2.bitwise_not(img1,mask)
    img4=cv2.bitwise_xor(img1,mask)
    cv2.imshow('3',img4)
    cv2.waitKey()
    cv2.destroyAllWindows()


def tuxiangjiami(src):
    img=cv2.imread(src)
    img=cv2.resize(img,(300,300))

    rows,colmns,channel=img.shape;
    img_key=np.random.randint(0,256,(rows,colmns,3),np.uint8)
    cv2.imshow("1",img)
    cv2.moveWindow("1", 600, 50)
    cv2.imshow('2',img_key)
    cv2.moveWindow("2", 900, 50)
    reslut=encode(img,img_key)
    cv2.imshow('3',reslut)
    cv2.moveWindow("3", 1200, 50)
    reslut2=encode(reslut,img_key);
    cv2.imshow('4', reslut2)
    cv2.moveWindow("4", 300, 50)
    cv2.waitKey()
    cv2.destroyAllWindows()

def encode(img,img_key):
    result=cv2.bitwise_xor(img,img_key);
    return result;


def main():
    # yanmo()
    # pitrue()
    # yanmooirtue();
    # yanmooirtue2();
    tuxiangjiami('a1.jpg')
if __name__=='__main__':
    main();