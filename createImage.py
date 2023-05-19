import  numpy as np
import  cv2

def createimage():

    array=np.zeros((100,200),np.uint8);
    array[25:75, 50:100] = 255;
    image=cv2.imshow("img",array);
    cv2.waitKey()
    cv2.destroyAllWindows()


    array2 = np.ones((100, 200), np.uint8)*255;
    image = cv2.imshow("img2", array2);
    cv2.waitKey()
    cv2.destroyAllWindows()


    array3=np.random.randint(0,255,[500,500],np.uint8);
    image = cv2.imshow("img3", array3);
    cv2.waitKey()
    cv2.destroyAllWindows()