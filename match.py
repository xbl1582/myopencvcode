#模板匹配
 # matchTemplate

import cv2
import  os

def matchputrue(path1,modelpath):
    # 读取图片
    img=cv2.imread(path1)
    img=cv2.resize(img,(300,300))
    img2=cv2.imread(modelpath)
    img2=cv2.resize(img2,(200,200))
    # 获取模板图像高度，宽度，通道数
    height,width,c=img2.shape
    # 计算模板匹配方法
    # 按标准平方差方式匹配
    result=cv2.matchTemplate(img,img2,cv2.TM_SQDIFF_NORMED)
    #获取匹配结果的最小值，最大值，最小值坐标，最大值坐标
    minValue,maxValue,minLoc,maxLoc=cv2.minMaxLoc(result)
    resultPont1=minLoc
    # 计算出最佳匹配区域的右下角点坐标
    resultPont2=(resultPont1[0]+width,resultPont1[1]+height)
    # 在最佳匹配区域绘制红色方框，线宽为2像素
    cv2.rectangle(img,resultPont1,resultPont2,(0,0,255),2)
    cv2.imshow("img",img)
    cv2.waitKey()
    cv2.destroyAllWindows()

def matchputrue2(path1,modelpath):
    # 读取图片
    img=cv2.imread(path1)
    img=cv2.resize(img,(300,300))
    img2=cv2.imread(modelpath)
    img2=cv2.resize(img2,(200,200))
    # 获取模板图像高度，宽度，通道数
    height,width,c=img2.shape
    # 计算模板匹配方法
    # 按标准平方差方式匹配
    result=cv2.matchTemplate(img,img2,cv2.TM_SQDIFF)
    #获取匹配结果的最小值，最大值，最小值坐标，最大值坐标
    minValue,maxValue,minLoc,maxLoc=cv2.minMaxLoc(result)
    resultPont1=minLoc
    # 计算出最佳匹配区域的右下角点坐标
    resultPont2=(resultPont1[0]+width,resultPont1[1]+height)
    # 在最佳匹配区域绘制红色方框，线宽为2像素
    cv2.rectangle(img,resultPont1,resultPont2,(0,0,255),2)
    cv2.imshow("img",img)
    cv2.waitKey()
    cv2.destroyAllWindows()
def max_mach(modelpath,sourcepath1,sourcepath2):
#     读入3张图片
    img=cv2.imread(modelpath)
    img2=cv2.imread(sourcepath1)
    height,width,c=img2.shape
    img3=cv2.imread(sourcepath2)
    img3=cv2.resize(img3,(width,height))
# 通过模板方法平方差匹配
#    获取模板的形状以及通道

#   通过模板方法匹配
    result=cv2.matchTemplate(img2,img,cv2.TM_SQDIFF_NORMED)
    result2=cv2.matchTemplate(img3,img,cv2.TM_SQDIFF_NORMED)
    if any(result[0])>any(result2[0]):
        cv2.imshow("result",img3)
    else:
        cv2.imshow("result2",img2)
    cv2.waitKey()
    cv2.destroyAllWindows()


def max_match2(modelpath,images):
#     读取模拟
    modelimage=cv2.imread(modelpath)
    index =-1;
    min=1
    sourceimages=[]
    for i in range(0,len(images)):
        sourceimages.append(cv2.imread(images[i]))

    height, width, c = sourceimages[0].shape
    for i in range(0,len(sourceimages)):
        sourceimages[i]=cv2.resize(sourceimages[i],(height,width))
    for i in range(0,len(sourceimages)):
#         按照平方差方式匹配
        results=cv2.matchTemplate(sourceimages[i],modelimage,cv2.TM_SQDIFF_NORMED)
        minValue, maxValue, minLoc, maxLoc = cv2.minMaxLoc(results);
        if (min > minValue):
            min = minValue
            index = i
    cv2.imshow("result",sourceimages[index])
    cv2.waitKey()
    cv2.destroyAllWindows()

def finsamepiture(filePath):
    files_and_folders=os.listdir(filePath)
    width, height=100,100
    endswith = ['.xbm','.tif','pjp','.svgz','jpg','jpeg','ico','tiff','.gif','svg','.jfif','.webp','.png','.bmp','pjpeg','.avif']
    endswith_tuple = tuple(endswith)
#     遍历文件夹中的所有文件和文件夹
    images=[]
    imagenames=[]
    sameimages=[]
    tempfile = []

    has_sameimagename=[]
    for name in files_and_folders:
#     构建完整的文件路径
        full_path=os.path.join(filePath,name)
        if os.path.isdir(full_path):
            finsamepiture(full_path)
        else:
            if(name.endswith(endswith_tuple)):
                img=cv2.imread(name)
                img=cv2.resize(img,(width,height))
                images.append(img)
                imagenames.append(name)
    for i in range(0,len(images)):
        sameimagesname = set()
        for j in range(0,len(images)):
            if(i!=j):
                results=cv2.matchTemplate(images[j],images[i],cv2.TM_CCORR_NORMED);
                if(results>0.9):
                    sameimages.append(images[i])
                    sameimagesname.add(imagenames[i])
                    sameimagesname.add(imagenames[j])
        if(sameimagesname!=set()):
            has_sameimagename.append(sameimagesname)

    for sam in has_sameimagename:
        if sam not in tempfile :
            tempfile.append(sam)
        else:
            continue
    for sam in tempfile:
        print(sam)


def finsamepitures(modelimage,sourceimage):
#     读取图片
    img=cv2.imread(modelimage);
    height,width,c=img.shape
    img2=cv2.imread(sourceimage);
    result=cv2.matchTemplate(img2,img,cv2.TM_CCORR_NORMED)
    for y in range(len(result)):
        for x in range(len(result[y])):
            if(result[y][x]>0.99):
                cv2.rectangle(img2,(x,y),(x+width,y+height),(0,0,255),2);
    img2=cv2.resize(img2,(300,400))
    cv2.imshow("img",img2)
    cv2.waitKey()
    cv2.destroyAllWindows()

def finsamepitures2(img,img2):
#     读取图片
    height,width,c=img.shape

    # for i in range(-3,3):
    #     print(i)
    #     rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), i, 1)
    #     img = cv2.warpAffine(img, rotation_matrix, (width, height))
    #     name=str(i)
    #     cv2.imshow(name,img)


    result = cv2.matchTemplate(img2, img, cv2.TM_CCORR_NORMED)
    for y in range(len(result)):
        for x in range(len(result[y])):
            if (result[y][x] > 0.99):
                cv2.rectangle(img2, (x, y), (x + width, y + height), (0, 0, 255), 1);

    return img2;
def finsamepitures3(modelimages,sourceimage):
    images=[];
    img2=cv2.imread(sourceimage);
    for i in range(0,len(modelimages)):
        images.append(cv2.imread(modelimages[i]))
    for i in  range(0,len(images)):
        img2=finsamepitures2(images[i],img2)
    img2 = cv2.resize(img2, (300, 400))
    cv2.imshow("img", img2)
    cv2.waitKey()
    cv2.destroyAllWindows()


def main():
    # matchputrue("p1.jpg","p2.jpg")
    # matchputrue2("p1.jpg", "p2.jpg")
    # max_mach("p1.jpg", "p2.jpg", "p3.jpg")
    # max_match2("p2.jpg", ["p1.jpg", "p3.jpg"])
    # finsamepiture("D:/MyCodeLearn/pythonwordkspace/xxnoteproject")
    # finsamepitures("p6.jpg", "p5.jpg")
    finsamepitures3(["p6.jpg","p7.jpg"], "p5.jpg")
if __name__=="__main__":
    main()