import cv2

# read image from file
# img = cv.imread("cat.jpg")
# cv.imshow("Image", img)
# cv.waitKey(0)

# read camera

frameWidth = 640
frameHeight = 400

cap = cv2.VideoCapture("file.mp4")
while True:
    # đọc vào biến success và biến img
    success, img = cap.read()
    img = cv2.resize(img, (frameWidth, frameHeight))
    cv2.imshow("Video", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
