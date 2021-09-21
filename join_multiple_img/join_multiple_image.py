import cv2
import numpy as np

# read image
img1 = cv2.imread("cat.jpg", 0)
img1 = cv2.resize(img1, (690, 920))
img1 = cv2.cvtColor(img1, cv2.COLOR_GRAY2BGR)
img2 = cv2.imread("meo.jpg")

# print img1.shape and img2.shape
print(img1.shape)
print(img2.shape)

# resize image
img1 = cv2.resize(img1, (0, 0), None, 0.5, 0.5)
img2 = cv2.resize(img2, (0, 0), None, 0.5, 0.5)

ver = np.vstack([img1, img2])  # ghép dọc
hor = np.hstack((img1, img2))  # ghép ngang
# print("ver", ver)
# print("hor", hor)
cv2.imshow("Vstack", ver)
cv2.imshow("Hstack", hor)
cv2.waitKey(0)
