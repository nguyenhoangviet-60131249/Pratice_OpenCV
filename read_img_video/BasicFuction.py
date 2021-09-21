import cv2
import numpy as np

path = "cat.jpg"
img = cv2.imread(path)
imgCopy = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgCopy, (5, 5), 100)  # ảnh mờ
imgCanny = cv2.Canny(imgBlur, 0, 0)
cv2.imshow("Image", img)
cv2.imshow("Image copy", imgCopy)
cv2.imshow("Image Blur", imgBlur)
cv2.imshow("Image Canny", imgCanny)

cv2.waitKey(0)
