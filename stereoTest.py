import numpy as np
import cv2

fx = 942.8          # lense focal length
baseline = 54.8     # distance in mm between the two cameras
disparities = 128   # num of disparities to consider
block = 31          # block size to match
units = 0.001       # depth units

sbm = cv2.StereoBM_create(numDisparities=disparities, blockSize=block)

left_image_path = '.\\real_img\\left.png'
right_image_path = '.\\real_img\\right.png'

left = cv2.imread(left_image_path, cv2.IMREAD_GRAYSCALE)
right = cv2.imread(right_image_path, cv2.IMREAD_GRAYSCALE)

disparity = sbm.compute(left, right)

depth = np.zeros(shape=left.shape).astype(float)
depth[disparity > 0] = (fx * baseline) / (units * disparity[disparity > 0])

cv2.imshow("Left Image", left)
cv2.imshow("Right Image", right)
cv2.imshow("Disparity Map", disparity / np.max(disparity))  # Normalize for display
cv2.imshow("Depth Map", depth / np.nanmax(depth))          # Normalize for display
cv2.waitKey(0)
cv2.destroyAllWindows()