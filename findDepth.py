import cv2
import numpy as np
import matplotlib.pyplot as plt

# Constants
focal_length = 700  # Example focal length in pixels
baseline = 0.1      # Baseline in meters (distance between the cameras)

# Load the disparity map (example: normalized disparity map)
disparity_map = cv2.imread('.\\internet_img\\disparity.png', cv2.IMREAD_GRAYSCALE)

# Avoid division by zero
disparity_map[disparity_map == 0] = 0.1

# Calculate depth
depth_map = (focal_length * baseline) / disparity_map

img = cv2.imread('.\\internet_img\\scene1.row3.col1.jpg')

# Display results
plt.figure(figsize=(3,3))
plt.imshow(img)
plt.colorbar(label="Depth (meters)")
plt.title("image")

plt.figure(figsize=(3,3))
plt.imshow(depth_map, cmap='plasma')
plt.colorbar(label="Depth (meters)")
plt.title("gray image")

plt.figure(figsize=(3,3))
plt.imshow(disparity_map, cmap='gray')
plt.colorbar(label="Depth (meters)")
plt.title("Depth Map")
plt.show()

