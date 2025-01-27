import cv2
import numpy as np

# stereo
cap1 = cv2.VideoCapture(0)
# cap1.set(3, 640)
# cap1.set(4, 480)

cap2 = cv2.VideoCapture(1)
# cap2.set(3, 640)
# cap2.set(4, 480)

# ฟังก์ชันสำหรับแสดง disparity (stereo)
def ShowDisparity(imgLeft, imgRight, bSize=5):
    # Initialize the stereo block matching object 
    stereo = cv2.StereoBM_create(numDisparities=32, blockSize=bSize)

    # Compute the disparity image
    disparity = stereo.compute(imgLeft, imgRight)

    # Normalize the image for representation
    min = disparity.min()
    max = disparity.max()
    disparity = np.uint8(255 * (disparity - min) / (max - min))
    
    # Plot the result
    return disparity


while True:

    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()

    # # รูปในเน็ต
    # frame1 = cv2.imread('.\\real_img\\left.png')
    # frame2 = cv2.imread('.\\real_img\\right.png')

    gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    # disparity1 =  ShowDisparity(gray1, gray2, bSize=25)
    

    # แสดงรูปภาพ
    cv2.imshow('Right', gray1)
    cv2.imshow('Left', gray2)
    # cv2.imshow('Disparity', disparity1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# # Save the disparity map
# cv2.imwrite('.\\internet_img\\disparity.png', disparity2)

cap1.release()
cap2.release()
cv2.destroyAllWindows()