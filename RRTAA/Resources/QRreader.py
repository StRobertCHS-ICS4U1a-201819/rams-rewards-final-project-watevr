import cv2
cap = cv2.VideoCapture(0)
while True:
    ret,frame = cap.read()
    cv2.imshow("camera",frame)
    k = cv2.waitKey(1)&0xff
    if k==27:
        break
cap.release()#需要放置在while循环体外
cv2.destroyAllWindows()#需要放置在while循环体外