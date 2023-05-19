# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import cv2
import  numpy
import  imageOperation
import  numpyLearn01
import  createImage


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    imagepath="C:\\Users\\GDWT34\Desktop\\v2-43156cca0de1619a56b7589c82961b76_r.jpg"
    img=cv2.imread(imagepath,0);
    print(img)
    cv2.imshow("2",img);
    # 显示时间
    # cv2.waitKey(0);
    cv2.waitKey(5000);#1000，1秒
    cv2.destroyAllWindows();
    cv2.imwrite("C:\\Users\\GDWT34\Desktop\\思维导图.jpg",img)
    print(img.shape)
    print(img.size)
    print(img.dtype)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # foldername="C:/Users/GDWT34/Desktop/"
    # imagepath = "C:/Users/GDWT34/Desktop/1.jpg"
    # # imageOperation.operationimage(imagepath);
    # imageOperation.changeImage(foldername,imagepath);
    # print_hi('PyCharm')
    # numpyLearn01.arraychange();
    # numpyLearn01.createarray()
    createImage.createimage();
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
