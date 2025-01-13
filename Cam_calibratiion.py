import cv2


cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

cap2 = cv2.VideoCapture(2)
cap2.set(3, 640)
cap2.set(4, 480)

num = 0

while cap.isOpened():

    succes, img = cap.read()
    succes2, img2 = cap2.read()

    k = cv2.waitKey(5)

    if k == 27:
        break
    elif k == ord('s'): # wait for 's' key to save and exit
        cv2.imwrite('C:\\Users\\User\\stereoCam\\stereoLeft\\imageL' + str(num) + '.png', img)
        cv2.imwrite('C:\\Users\\User\\stereoCam\\stereoRight\\imageR' + str(num) + '.png', img2)
        print("image saved!")
        num += 1

    cv2.imshow('Img 1',img)
    cv2.imshow('Img 2',img2)

cap.release()
cap2.release()
cv2.destroyAllWindows()