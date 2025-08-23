import cv2 as cv
import numpy as np 
import matplotlib.pyplot as plt



l = ['sample2.jpg','sample3.jpg','sample4.jpg','sample5.jpg','sample6.jpg']
issue = []
noissue = []

image = cv.imread('ideal.jpg')
image = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
bl = np.ones((600,600) ,dtype="uint8") *255
circlecomapre = cv.circle(bl.copy(), (300,315) ,100,0,-1)
thresholdsideal , threshsideal = cv.threshold(image,70,255,cv.THRESH_BINARY)
bb = cv.bitwise_or(circlecomapre,threshsideal)
bb = cv.bitwise_not(bb)
z1 = cv.countNonZero(bb)


for i in range(0,len(l),1):
    image1 = cv.imread(l[i])
    image2 = cv.imread('ideal.jpg')
    threshold1 , thresh1 = cv.threshold(image1,45,255,cv.THRESH_BINARY)
    threshold1, thresh2 = cv.threshold(image2,45,255,cv.THRESH_BINARY_INV)
    thresh1 = cv.cvtColor(thresh1,cv.COLOR_BGR2GRAY)
    thresh2 = cv.cvtColor(thresh2,cv.COLOR_BGR2GRAY)
    bcompare = cv.bitwise_or(circlecomapre,thresh1)
    bcompare = cv.bitwise_not(bcompare)
    z2 = cv.countNonZero(bcompare)
    flag = 's'
    if (z2 > z1):
        flag = 'Large inner openning'
    elif (z2 == z1):
        flag = 'ideal inner openning'
    elif (z2 == 0):
        flag = 'Missing inner openning'


    blank = np.zeros((600,600) ,dtype="uint8") *255
    circle = cv.circle(blank.copy(),(300,300),100,255,-1)
    bitwise_or22 = cv.bitwise_or(circle,thresh1)
    bitwise_or33 = cv.bitwise_or(circle,thresh2)







    bitwise_or444 = cv.bitwise_or(bitwise_or22,bitwise_or33)


    if(np.count_nonzero(bitwise_or444) == 360000):
        print(f"The gear {l[i]} is not broken with {flag} ")
        noissue.append(l[i])
    else:
        print(f"the gear {l[i]} is broken or worn with {flag}")
        issue.append(l[i])


print('--------------------------------------------------------------')





for i in range(0,len(issue),1):
    image5 = cv.imread(issue[i])
    image5 = cv.cvtColor(image5,cv.COLOR_BGR2GRAY)
    threshold3 , thresh3 = cv.threshold(image5,70,255,cv.THRESH_BINARY)
    blank5 = np.ones((600,600) ,dtype="uint8") *255
    circle5 = cv.circle(blank5.copy(),(300,315),170,0,-1)
    bitwise_or5 = cv.bitwise_and(circle5,thresh3)
    cleaned = cv.medianBlur(bitwise_or5, 5)
    contours6 , hierarchies6 = cv.findContours(cleaned, cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
    c1 = len(contours6)
    broken= 30 -  c1


    circle8 =cv.circle(blank5.copy(),(300,315),190,0,-1)
    bitwise_orrs = cv.bitwise_and(circle8,thresh3)
    c2 , h2 = cv.findContours(bitwise_orrs, cv.RETR_LIST,cv.CHAIN_APPROX_NONE)

    worn = 30 - (len(c2)) - broken



    print(f'{issue[i]} has {broken} broken teeth and {worn} worn teeth')




