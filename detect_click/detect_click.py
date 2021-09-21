import cv2
import numpy as np

circles = np.zeros((4, 2), np.int)
counter = 0


# hàm check sự kiện
def mousePoints(event, x, y, flags, params):
    global counter
    # check khi người dùng nhấn chuột trái
    if event == cv2.EVENT_LBUTTONDOWN:
        # tạo ra tọa độ x,y và cho vào 1 ma trận
        circles[counter] = x, y
        # biến counter tăng
        counter = counter + 1


img = cv2.imread("anh.jpg")

while True:

    # xử lý khi mà ấn đủ 4 điểm
    if counter == 4:
        width, height = 250, 350

        # lấy ra từng cái tọa độ trong mảng circles
        pts1 = np.float32([circles[0], circles[1], circles[2], circles[3]])
        pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

        # chuyển đổi phối cảnh
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        imgOutput = cv2.warpPerspective(img, matrix, (width, height))
        cv2.imshow("Image Output", imgOutput)

    # lặp qua để vẽ 4 điểm lên ảnh
    for x in range(0, 4):
        # vẽ point lên ảnh được cắt ra
        cv2.circle(img, (circles[x][0], circles[x][1]), 5, (0, 0, 255), cv2.FILLED)

    cv2.imshow("Image", img)
    cv2.setMouseCallback("Image", mousePoints)
    cv2.waitKey(1)
