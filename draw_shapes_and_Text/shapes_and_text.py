import cv2
import numpy as np

# np.uint8 => kieu interger
img = np.zeros((512, 512, 3), np.uint8)

# values BGR2GRAY (Blue,Green,Red)

# img[50:100, 60:200] = 0, 255, 255
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 255), 2)
cv2.rectangle(img, (100, 200), (500, 300), (255, 0, 255), 2)
cv2.circle(img, (100, 500), 5, (255, 0, 0), 3)
cv2.imshow("Image Matrix", img)
cv2.waitKey(0)
