import numpy as np
import cv2

def nothing(x):
    pass

pic="1000.jpg"
background="back.jpg"
cv2.namedWindow('image')

img=cv2.imread(pic, 0)
back=cv2.imread(background, 0)

backMean = cv2.mean(back)
cv2.createTrackbar('R','image',0,255,nothing)

th=0
diff = cv2.subtract(img, backMean)


while(1):
    th=cv2.getTrackbarPos('R','image')
    #_, thresh = cv2.threshold(diff, th, 255, cv2.THRESH_BINARY)
    #cv2.putText(thresh, str(th), (0,400), cv2.FONT_HERSHEY_COMPLEX, 20,(255,255,255),4,cv2.LINE_AA)
    blur = cv2.GaussianBlur(diff, (5, 5), 0)
    ret3, otsu = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    concatHorizontal = np.concatenate((img, diff, blur, otsu), axis=1)
    cv2.imshow('image', concatHorizontal)
    print(str(th))
    k = cv2.waitKey(16) & 0xFF
    if k == 27:         # wait for ESC key to exit
        cv2.destroyAllWindows()
        exit()
    elif k == ord('s'): # wait for 's' key to save and exit
        cv2.destroyAllWindows()
        exit()