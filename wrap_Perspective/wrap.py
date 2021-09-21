import cv2
import numpy as np

width, height = 250, 350
img = cv2.imread("cards.jpg")

# cung cấp tọa độ ảnh
pts1 = np.float32([[111, 219], [287, 188], [154, 482], [352, 440]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

# chuyển đổi phối cảnh
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

# lặp qua để vẽ 4 điểm lên ảnh
for x in range(0, 4):
    # vẽ point lên ảnh được cắt ra
    cv2.circle(img, (pts1[x][0], pts1[x][1]), 5, (0, 0, 255), cv2.FILLED)
    print(pts1[x][1])
cv2.imshow("Cards", img)
cv2.imshow("Image Output", imgOutput)
cv2.waitKey(0)
